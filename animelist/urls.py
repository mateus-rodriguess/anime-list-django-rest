from django.urls import path
from animelist.views import lista_animes, anime_description, animes_add, anime_edit, anime_delete, animes_list,  animes_detail

urlpatterns = [
    path('animes/', lista_animes, name='animes'),
    path('', lista_animes, name='animes'),
    path('anime/id/<int:pk>/', anime_description, name='animedescription'),
    path('anime/add/', animes_add, name='animeadd'),
    path('anime/edit/<int:pk>/', anime_edit, name='post_update'),
    path('anime/delete/<int:pk>/', anime_delete, name='post_delete'),
    # rotas API
    # listagem e pra add novos animes
    path('api/animes/', animes_list),
    # apagar, editar, axibir
    path('api/animes/<int:pk>/', animes_detail),
]