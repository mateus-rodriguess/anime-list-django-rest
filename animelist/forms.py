from django import forms
from django.contrib.auth.models import User
from .models import AnimesModel

class Animes_Form(forms.ModelForm):
   
   class Meta:
      model = AnimesModel
      fields = ['title', 'episodes', 'description', 'genres', 'studios','mean_score', 'popularity', 'average_score','your_note',]

    