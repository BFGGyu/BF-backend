from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
urlpatterns = [
    #회원가입/로그인/로그아웃
    path('join/', RegisterView.as_view()),
    path('login/', AuthView.as_view()),
    #토큰
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # 구글 소셜로그인
    path('kakao/login/', KakaoLogin.as_view(), name='kakao_login'),
    path('kakao/callback/', KakaoCallback.as_view(), name='kakao_callback'),
    path('kakao/login/finish/', KakaoLoginToDjango.as_view(), name='kakao_login_todjango'),
    
	path('bookmark/<str:arrival>/', UserBookmarkView.as_view(), name='user_bookmark'),
]