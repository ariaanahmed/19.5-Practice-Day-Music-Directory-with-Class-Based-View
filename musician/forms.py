from django import forms
from .models import Musician

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email address'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone'}),
            'instrument': forms.TextInput(attrs={'placeholder': 'Instrument'}),
        }
        
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'phone': '',
            'instrument': '',
        }
