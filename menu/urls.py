from django.urls import path

from . import views

urlpatterns = [
    path('<int:id_menu>', views.visualizza, name='index'),
    path('all', views.all_menus, name='index'),

]
