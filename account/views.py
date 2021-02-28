from .forms import UserCreationFormCustom
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render,redirect
from animelist.models import AnimesModel
from django.core.paginator import Paginator
# Create your views here.
class CreateUser(generic.CreateView):
    """
    view that rederizes the template for user registration
    """
    form_class = UserCreationFormCustom
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


def profile(request):
    """
    user profile view
    """
    animes = AnimesModel.objects.filter(user=request.user)
    animestotais = AnimesModel.objects.filter(user=request.user).count()
    # paginação
    paginator = Paginator(animes, 20)
    page = request.GET.get('page')
    animes = paginator.get_page(page)

    return render(request, 'profile/profile.html', {'animes': animes, 'animestotais': animestotais})