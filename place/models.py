from django.db import models

# Create your models here.
class Facility(models.Model):
    
    CHOICES = (
        ('museum', '박물관'),
        ('artGallery', '미술관'),
        ('exhibition', '전시회')
	)
    
    id = models.AutoField(primary_key = True, default = 0)
    name = models.CharField(max_length=50)

    type = models.CharField(choices=CHOICES, max_length=20)
    contact = models.CharField(max_length=20)
    address = models.TextField()
    opening_time = models.TimeField(default='09:00')
    closing_time = models.TimeField(default='18:00')
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    
    def __str__(self):
	    return self.name

class Station(models.Model):
	name = models.CharField(max_length = 50, primary_key = True)

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