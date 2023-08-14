from rest_framework_simplejwt.serializers import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.serializers import RegisterSerializer

class RegisterView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=False):
            member = serializer.save(request)
            token = RefreshToken.for_user(member)
            refresh_token = str(token)
            access_token = str(token.access_token)

            res = Response(
                {
                    "member":serializer.data,
                    "message":"register success",
                    "token":{
                        "access_token":access_token,
                        "refresh_token":refresh_token,
                    },
                },
                status=status.HTTP_201_CREATED,
            )
            return res
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from accounts.serializers import AuthSerializer

class AuthView(APIView):
    serializer_class = AuthSerializer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
						
        if serializer.is_valid(raise_exception=False):
            member = serializer.validated_data['member']
            access_token = serializer.validated_data['access_token']
            refresh_token = serializer.validated_data['refresh_token']
            res = Response(
                {
                    "member": {
                            "id":member.id,
                            "email":member.email,
                            "age":member.age,
                    },
                    "message":"login success",
                    "token":{
                        "access_token":access_token,
                        "refresh_token":refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )
            res.set_cookie("access-token", access_token, httponly=True)
            res.set_cookie("refresh-token", refresh_token, httponly=True)
            return res
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        res = Response({
			"message":"logout success"
		}, status=status.HTTP_202_ACCEPTED)
				
		# cookie에서 token 값들을 제거함
        res.delete_cookie("access-token")
        res.delete_cookie("refresh-token")
        return res



from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from django.contrib.auth import get_user_model
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.kakao import views as kakao_view
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework_simplejwt.serializers import RefreshToken
import json

with open('secrets.json') as secrets_file:
    secrets = json.load(secrets_file)

KAKAO_CALLBACK_URI = 'http://localhost:8000/accounts/kakao/callback/'

class KakaoLogin(APIView):
    def get(self, request):
        client_id = secrets.get("CLIENT_ID")
        redirect_uri = "http://localhost:8000/accounts/kakao/callback/"

        return redirect(f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code")

class KakaoCallback(APIView):
    def get(self, request):
        client_id = secrets.get("CLIENT_ID")
        code = request.GET.get('code')

        # 카카오에 access token 요청
        token_req = requests.post(f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={KAKAO_CALLBACK_URI}&code={code}")
        token_req_json = token_req.json()

        # access token으로 카카오 사용자 정보 요청
        access_token = token_req_json.get('access_token')
        user_info_req = requests.get('https://kapi.kakao.com/v2/user/me', headers={'Authorization': f'Bearer {access_token}'})
        user_info_req_json = user_info_req.json()
		
        # 카카오 사용자 정보에서 이메일과 닉네임 가져오기
        kakao_email = user_info_req_json.get('kakao_account', {}).get('email', None)
        kakao_nickname = user_info_req_json.get('properties', {}).get('nickname', None)

        # 카카오 이메일로 회원 확인 및 생성
        User = get_user_model()

        if kakao_nickname:
            username = kakao_nickname
        else:
            # Generate an unused number-based username
            base_username = "user"
            username = self.generate_unused_username(User, base_username)

        user, created = User.objects.get_or_create(email=kakao_email, defaults={'username': username})
        #user, created = User.objects.get_or_create(email=kakao_email, defaults={'username': kakao_nickname})
        
        # # 카카오 닉네임으로 username 설정
        # if created and kakao_nickname:
        #     user.username = kakao_nickname
        #     user.nickname = kakao_nickname
        #     user.save()

        # JWT 토큰 생성
        token = RefreshToken.for_user(user)
        refresh_token = str(token)
        access_token = str(token.access_token)
        
        return Response({
            "access_token": access_token,
            "refresh_token": refresh_token,
            "message": "카카오 소셜 로그인 성공",
            "username" : user.username
        }, status=status.HTTP_200_OK)
    
    def generate_unused_username(self, User, base_username):
        username = base_username
        i = 1
        while User.objects.filter(username=username).exists():
            username = f"{base_username}{i}"
            i += 1
        return username

class KakaoLoginToDjango(SocialLoginView):
    adapter_class = kakao_view.KakaoOAuth2Adapter
    callback_url = KAKAO_CALLBACK_URI
    client_class = OAuth2Client
