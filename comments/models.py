from django.db import models
from tours.models import Tour
from datetime import datetime  
from core import settings
from django.db.models import Avg
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

class Rating(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rated_object_id = models.ForeignKey(Tour, on_delete=models.CASCADE)  
    rating = models.PositiveIntegerField()

    class Meta:  
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"

    def str(self) -> str:
        return f'Rated by {self.user_id} on {self.rated_object_id}'

