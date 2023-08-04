from django.db import models
from placeinfo.models import Place

class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name="작성일시", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="수정일시", auto_now=True)

    class Meta:
        abstract = True
        
class Review(BaseModel):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField(default=0, blank=True, null=True, help_text='별 개수 (0 ~ 5)')
    comment = models.TextField()  # 리뷰 글 작성
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.place.name} - {self.stars} stars"
