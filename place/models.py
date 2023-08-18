from django.db import models

# Create your models here.
class Facility(models.Model):
    
    CHOICES = (
        ('museum', '박물관'),
        ('artGallery', '미술관'),
        ('exhibition', '전시회')
	)
	
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    type = models.CharField(choices=CHOICES, max_length=20)
    contact = models.CharField(max_length=20)
    address = models.TextField()
    opening_time = models.CharField(max_length=10)
    closing_time = models.CharField(max_length=10)
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    imageSrc = models.TextField(default="")
    
    def __str__(self):
	    return self.name

class Station(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length = 50)
	fac_name = models.ForeignKey(Facility, on_delete=models.CASCADE)

	line = models.IntegerField()
	latitude = models.CharField(max_length=20)
	longitude = models.CharField(max_length=20)
	
	def __str__(self):
	    return self.name

class FacAmenity(models.Model):
	id = models.AutoField(primary_key = True)
	fac_name = models.ForeignKey(Facility, on_delete=models.CASCADE)
	
	name = models.CharField(max_length=50)
	quantity = models.IntegerField(default='1')
	
	def __str__(self):
	    return f'{self.fac_name.name}: {self.name}'
	
class StatAmenity(models.Model):
	id = models.AutoField(primary_key = True)
	stat_name = models.ForeignKey(Station, on_delete=models.CASCADE)
	
	name = models.CharField(max_length=50)
	quantity = models.IntegerField(default='1')   
	
	def __str__(self):
	    return f'{self.stat_name.name}: {self.name}'
	
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings

class UserBookmark(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'facility')

    def __str__(self):
        return f'{self.user.username} - {self.facility.name}'

    
	
	
	