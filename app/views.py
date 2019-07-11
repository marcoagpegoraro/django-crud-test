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
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AgendaForm(request.POST)
        # check whether it's valid:
        print(form.errors)

        if form.is_valid():
            # process the data in form.cleaned_data as required
            
            agendaMaster = AgendaMaster(title=request.POST['title_form'],description=request.POST['description_form'])
            agendaMaster.save()

            return HttpResponseRedirect('/agendas/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AgendaForm()

    context  = {"title": my_title}
    return render(request, "agenda.html", context )