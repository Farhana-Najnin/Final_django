from django.shortcuts import render
from django.urls import reverse_lazy
from .import models 
from .import forms
from django.views.generic import View
# Create your views here.

class CategoryView(View):
    model = models.Categori
    form_class = forms.CategoryForm
    template_name = 'home.html'
    success_url = reverse_lazy('category_course')
    
    def form_valid(self, form):
        return super().form_valid(form)