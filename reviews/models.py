from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    movie_name = models.CharField(max_length=30)
    grade = models.IntegerField(
        default=1,
        help_text="0~5사이 값으로 입력하세요",
        validators=[MinValueValidator(0), MaxValueValidator(5)],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    imgfile = models.ImageField(null=True, upload_to="", blank=True)
