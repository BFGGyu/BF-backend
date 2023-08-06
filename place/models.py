from django.db import models

# Create your models here.
class Facility(models.Model):
    
    CHOICES = (
        ('MUSEUM', '박물관'),
        ('ART GALLERY', '미술관'),
        ('EXHIBITION', '전시회')
	)

    name = models.CharField(max_length=50, primary_key=True)

    type = models.CharField(choices=CHOICES, max_length=20)
    contact = models.CharField(max_length=20)
    address = models.TextField()
    opening_time = models.TimeField(default='09:00:00')
    closing_time = models.TimeField(default='18:00:00')
    latitude = models.DecimalField(default = 0, max_digits=9, decimal_places=6)
    longitude = models.DecimalField(default = 0, max_digits=9, decimal_places=6)
    
    def __str__(self):
	    return self.name

class Station(models.Model):
	name = models.CharField(max_length = 50, primary_key = True)

	line = models.IntegerField()
	latitude = models.DecimalField(default = 0, max_digits=9, decimal_places=6)
	longitude = models.DecimalField(default = 0, max_digits=9, decimal_places=6)
	
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