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


def agenda_page(request,id=0):
    if id == 0:
        page_title = "Adicionar agenda"
        agendaMaster = AgendaMaster()
    else:
        page_title = "Editar agenda"
        agendaMaster = AgendaMaster.objects.get(pk=id)

    if request.method == 'POST':

        form = AgendaForm(request.POST)

        if form.is_valid():
            agendaMaster, created = AgendaMaster.objects.update_or_create(
                id=id, 
                title=request.POST.title, 
                description=request.POST.description
                )

            agendaMaster = AgendaMaster.objects.get(pk=id)
            if created:
                return HttpResponseRedirect('/agendas/')
            else:
                return HttpResponseRedirect('/agenda/' + str(id))

    else:
        form = AgendaForm()

    context  = {"page_title": page_title, "agenda_master": agendaMaster}
    return render(request, "agenda.html", context )

def delete_agenda(request, id):
    agendaMaster = AgendaMaster.objects.get(pk=id)
    agendaMaster.delete()
    return HttpResponseRedirect('/agendas/')