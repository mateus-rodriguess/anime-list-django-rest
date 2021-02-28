from django.shortcuts import render,redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from animelist.api.serializers import AnimesSerializers
from .models import AnimesModel, User
from .forms import Animes_Form
from django.core.paginator import Paginator

# Create your views here.
@login_required
def lista_animes(request):
    """
    lists the anime related to the logged in user
    """
    animes = AnimesModel.objects.filter(user=request.user)
    # paginação
    paginator = Paginator(animes, 20)
    page = request.GET.get('page')
    animes = paginator.get_page(page)

    return render(request, 'animes/animeslist.html', {'animes': animes})

@login_required
def anime_description(request, pk):
    """
    shows anime description more results
    """
    animedesc = AnimesModel.objects.filter(user=request.user, pk=pk)

    return render(request, 'animes/animesdesc.html', {'animedesc': animedesc})


@login_required
def animes_add(request):
    """
    view to add new animes by form
    """
    if request.method == "POST":
        form = Animes_Form(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('animes')
    else:
        form = Animes_Form()
    return render(request, 'animes/animeadd.html', {'form': form})


@login_required
def anime_edit(request, pk):
    """
    view to edit the data of an anime
    """
    anime = AnimesModel.objects.get(pk=pk, user=request.user)
    form = Animes_Form(request.POST or None, instance=anime)
    if form.is_valid():
        form.save()
        return redirect('animes')
    return render(request, 'animes/animeadd.html', {'form': form})


@login_required
def anime_delete(request, pk):
    """
    view to delete an anime
    """
    anime = AnimesModel.objects.get(pk=pk, user=request.user)
    if request.method == "POST":
        anime.delete()
        return redirect('animes')
    return render(request, 'animes/animedelete.html', {"anime": anime})


# views da API
@api_view(['GET', 'POST'])
def animes_list(request):
    """
    List all animes_details, or create a new animes_detail.
    """
    if request.method == 'GET':
        animes_list = AnimesModel.objects.filter(user=request.user)
        serializer = AnimesSerializers(animes_list, many=True,context={'request': request})
        return Response(serializer.data)
        
    elif request.method == 'POST':
        serializer = AnimesSerializers(data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    
@api_view(['GET', 'PUT', 'DELETE'])
def animes_detail(request, pk):
    """
    Retrieve, update or delete a animes_detail instance.
    """
    try:
        animes_detail = AnimesModel.objects.get(pk=pk,user=request.user)
    except AnimesModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AnimesSerializers(animes_detail)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AnimesSerializers(animes_detail, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        animes_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
   