from django.db import models

class Place(models.Model):
    
	CHOICES = (
          ('MUSEUM', '박물관'),
          ('ART GALLERY', '미술관'),
          ('EXHIBITION', '전시회')
	)

	name = models.CharField(max_length=100)
	place_id = models.AutoField(primary_key=True)
	description = models.TextField()
	category = models.CharField(choices=CHOICES, max_length=50)  # 박물관, 미술관, 전시회 등의 카테고리
	latitude = models.DecimalField(max_digits=9, decimal_places=6)
	longitude = models.DecimalField(max_digits=9, decimal_places=6)
	has_accessible_toilet = models.BooleanField(default=False)  # 장애인 화장실 설치 여부
	has_elevator = models.BooleanField(default=False)  # 엘리베이터 설치 여부

	def __str__(self):
	    return self.name
