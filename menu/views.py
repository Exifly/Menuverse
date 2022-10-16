from django.shortcuts import render
from .models import Menu
from .forms import FeedBackeForm

def visualizza(request, id_menu):
    menus = Menu.objects.filter(visualizza=True, id=id_menu)
    return render(request, 'home.html', {'menus': menus})


def all_menus(request):
    menus = Menu.objects.filter(visualizza=True)
    forms =  FeedBackeForm()
    return render(request, 'home.html',
    context={
        'menus': menus,
        'form': forms
    })
