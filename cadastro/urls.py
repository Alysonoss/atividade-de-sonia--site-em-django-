from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('pagina1', views.pagina1, name='views.pagina_interna' ), 
    path('pagina2', views.pagina2, ), 
    path('pagina3', views.pagina3, ), 
    path('pagina4', views.pagina4, ), 
]
