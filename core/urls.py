from django.urls import path

from . import views


urlpatterns = [
    path("Haqqımızda/",views.about,name ="Haqqımızda"),
    path("",views.index,name ="Ana-Səhifə"),
    path("Xidmətlər/",views.services,name ="Xidmətlər"),
    path("Müəllimlərimiz/",views.team,name ="Müəllimlərimiz"),
    path("Fotoqalereya/",views.gallery,name ="Fotoqalereya"),
    path("Əlaqə/",views.contact,name ="Əlaqə"),


]