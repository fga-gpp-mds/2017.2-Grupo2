from django import forms
from medication.models import Medication


class EditForm(forms.ModelForm):

    name = forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'type': 'text',
                                                         'placeholder': 'Nome'}))

    laboratory = forms.CharField(max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'type': 'text',
                                                               'placeholder': 'Laboratório'}))

    active_ingredient = forms.CharField(max_length=100,
                                        widget=forms.TextInput(attrs={'class': 'form-control',
                                                                      'type': 'text',
                                                                      'placeholder': 'Ingrediente Ativo'}))
    description = forms.CharField(widget=forms.Textarea(
                                  attrs={'class': 'form-control',
                                         'cols': '10',
                                         'rows': '5'}))
    is_restricted = forms.BooleanField(required=False)

    class Meta:
        model = Medication
        fields = ['name', 'active_ingredient', 'laboratory', 'description']
