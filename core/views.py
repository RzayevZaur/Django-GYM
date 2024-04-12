from django.shortcuts import render
from .models import Index,Haqqında
# Create your views here.


def about(request):
    haqqında_views = Haqqında.objects.all()

    Context={
        'haqqında_views':haqqında_views
    }

    return render(request,"about-us.html", context=Context)


def index(request):
    index_views = Index.objects.all()
    Context={
        'index_views':index_views,
    }

    return render(request,"index.html", context=Context)



def services(request):
    About_views = Index.objects.all()
    Context={
        'About_views':About_views
    }

    return render(request,"services.html", context=Context)


def team(request):
    About_views = Index.objects.all()
    Context={
        'About_views':About_views
    }

    return render(request,"team.html", context=Context)



def gallery(request):
    About_views = Index.objects.all()
    Context={
        'About_views':About_views
    }

    return render(request,"gallery.html", context=Context)


def contact(request):
    About_views = Index.objects.all()
    Context={
        'About_views':About_views
    }

    return render(request,"contact.html", context=Context)


def page_404(request):
    About_views = Index.objects.all()
    Context={
        'About_views':About_views
    }

    return render(request,"404.html", context=Context)


