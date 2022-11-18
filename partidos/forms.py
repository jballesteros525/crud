from django import forms
from .models import Partidos

class PartidosForm(forms.ModelForm):
    class Meta:
        model= Partidos
        fields =['title','description','important']
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Write a title'}),
            'description':forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Write a descriptión'}),
            'important':forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'}),
        }