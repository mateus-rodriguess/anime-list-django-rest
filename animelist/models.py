from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class AnimesModel(models.Model):
   
    title = models.CharField(max_length=250, unique=True)
    episodes = models.IntegerField(default=12,blank=True)
    description = models.CharField(max_length=250, default="...",blank=True)
    genres = models.CharField(max_length=250,default="Shonem, comedy, ecchi")
    studios = models.CharField(max_length=250, default="The firm")
    popularity = models.FloatField(default=1,blank=True)
    mean_score = models.FloatField(default=1,blank=True)
    average_score = models.FloatField(default=1,blank=True)
    your_note = models.FloatField(blank=True, default=1, max_length=10)
    created_at = models.DateField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ['-created_at']
    
