from django import forms

class AgendaForm(forms.Form):
    title = forms.CharField(label='title', max_length=100)
    description = forms.CharField(label='description', max_length=100)