from django.db import models
from path.models import Path

# Create your models here.
class Obstacle(models.Model):
    id = models.AutoField(primary_key=True)
    path_id = models.ForeignKey(Path, on_delete=models.CASCADE)
    type = models.ForeignKey('ObsType', on_delete=models.CASCADE)

    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    explanation = models.TextField(blank=True, null=True)

    def __str__(self):
        path_name = f'{self.path_id.departure.name}-{self.path_id.arrival.name}'
        return f"Obstacle of {path_name} ({self.id})"

class ObsType(models.Model):
    type = models.CharField(max_length=50, primary_key=True)
    icon = models.ImageField(upload_to='./obstacle/obsIcon')

    def __str__(self):
        return self.type