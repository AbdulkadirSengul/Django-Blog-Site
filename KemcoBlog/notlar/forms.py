from django import forms 
from .models import Notlar

class NotlarForm(forms.ModelForm):
    class Meta:
        model = Notlar
        fields = ['title_nt','content_nt','not_image']