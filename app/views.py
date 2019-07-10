from django.shortcuts import render
from app.models import AgendaMaster
# Create your views here.

def home_page(request):
    my_title = "Hello there"
    agendas = AgendaMaster.objects.all()

    context  = {"title": my_title, "agendas": agendas}
    return render(request, "home.html", context )
