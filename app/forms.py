from django import forms

class AgendaForm(forms.Form):
    title_form = forms.CharField(label='title_form', max_length=100)
    description_form = forms.CharField(label='description_form', max_length=100)