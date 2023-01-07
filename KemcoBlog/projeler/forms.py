from django import forms 
from .models import Proje

class ProjeForm(forms.ModelForm):
    class Meta:
        model = Proje
        fields = ['title_prj','content_prj','proje_image']