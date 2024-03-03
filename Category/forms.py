from django import forms
from .models import Categori

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categori
        fields = '__all__'