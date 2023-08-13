from django.db import models
from path.models import Path
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name='작성 일시', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='수정 일시', auto_now=True)

    class Meta:
        abstract = True
        
class Review(BaseModel):
    id = models.AutoField(primary_key=True)
    path_id = models.ForeignKey(Path, on_delete=models.CASCADE)

    writer = models.CharField(max_length=30)   # unique=True 제거
    rating = models.PositiveIntegerField(default=5, blank=True, validators=[MinValueValidator(0), MaxValueValidator(5)])
    comment = models.TextField(null=True) 

    def __str__(self):
        return f'Writer: {self.writer}, Rating: {self.rating}'