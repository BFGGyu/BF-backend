from django.db import models
from placeinfo.models import Place
from obstacle.models import Obstacle

class Path(models.Model):
    start_station = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='outgoing_paths')  # 출발 지하철역 이름
    end_place = models.ForeignKey(Place, on_delete=models.CASCADE, blank=False)  # 도착 장소(박물관, 미술관, 전시회) 정보
    obstacles = models.ManyToManyField(Obstacle, blank=True)  # 경로상의 장애물 정보
    distance = models.DecimalField(max_digits=7, decimal_places=2)  # 경로의 총 거리
    duration = models.DurationField()  # 경로의 총 소요 시간

    def __str__(self):
        return f"{self.start_station} -> {self.end_place.name}"
