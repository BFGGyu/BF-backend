from django.db import models
from place.models import Station, Facility

# Create your models here.
class Path(models.Model):
    id = models.AutoField(primary_key=True)
    departure = models.ForeignKey(Station, on_delete=models.CASCADE)     # 출발지(지하철 역)
    arrival = models.ForeignKey(Facility, on_delete=models.CASCADE)                        # 도착지(박물관, 미술관 등)

    distance = models.FloatField(null=True)          # 경로 길이
    duration = models.DurationField(null=True)       # 총 소요 시간

    def __str__(self):
        return f'{self.departure.name}-{self.arrival.name}'

class Route(models.Model):
    id = models.AutoField(primary_key = True)
    path_id = models.ForeignKey(Path, on_delete=models.CASCADE)
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    
    def __str__(self):
        path_name = f'{self.path_id.departure.name}-{self.path_id.arrival.name}'
        return f"Route of {path_name} ({self.id})"    