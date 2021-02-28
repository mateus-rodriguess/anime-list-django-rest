from rest_framework import serializers
from animelist import models
from rest_framework.fields import CurrentUserDefault

class AnimesSerializers(serializers.ModelSerializer):
    # pegando o user logado 
    user = serializers.HiddenField(write_only=True, default=serializers.CurrentUserDefault())
   
    class Meta:
        model = models.AnimesModel
        fields = '__all__'
       