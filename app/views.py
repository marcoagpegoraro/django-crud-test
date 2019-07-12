from django.shortcuts import render
from django.http import HttpResponseRedirect
from app.models import AgendaMaster
from django import forms

from .forms import AgendaForm

def home_page(request):
    my_title = "Hello there"
   
    context  = {"title": my_title}
    return render(request, "home.html", context )

def agendas_page(request):
    my_title = "Hello there"
    agendas = AgendaMaster.objects.all().order_by('-pk')

    print(agendas)
    context  = {"title": my_title, "agendas": agendas}
    return render(request, "agendas.html", context )


def agenda_page(request):
    my_title = "Hello there"

    if request.method == 'POST':

        form = AgendaForm(request.POST)

        print(form.errors)

        if form.is_valid():
            
            agendaMaster = AgendaMaster(title=request.POST['title_form'],description=request.POST['description_form'])
            agendaMaster.save()

            return HttpResponseRedirect('/agendas/')

    else:
        form = AgendaForm()

    context  = {"title": my_title}
    return render(request, "agenda.html", context )

def delete_agenda(request, id):
    agendaMaster = AgendaMaster.objects.get(pk=id)
    agendaMaster.delete()
    return HttpResponseRedirect('/agendas/')