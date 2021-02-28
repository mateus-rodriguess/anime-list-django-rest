from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import CreateUser, profile

# urls
urlpatterns = [
   path('register/', CreateUser.as_view(), name="register"),
   path('login/', auth_views.LoginView.as_view(), name='login'),
   path('logout/', auth_views.LogoutView.as_view(), name='logout'),  
   path('profile/', profile, name='profile'),
]
