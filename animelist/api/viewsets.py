from rest_framework import viewsets
from animelist.api import serializers
from animelist.models import AnimesModel
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class AnimesViewset(viewsets.ModelViewSet):
    # filtragem que so mostra os animes do user logado 
    def get_queryset(self):
        user = self.request.user
        # filtro pelo user logado
        queryset = AnimesModel.objects.filter(user=user)
        return  queryset
    
    # sistema de autenticação 
    serializer_class = serializers.AnimesSerializers
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,SessionAuthentication,)

