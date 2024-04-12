from django.urls import path

from . import views


urlpatterns = [
    path("idman-xəbərləri/",views.Blog,name ="idman-xəbərləri"),
    path("idman-xəbərləri-detallı/<slug:slug>",views.Blog_details,name="idman-xəbərləri-detallı"),


]