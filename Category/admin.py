from django.contrib import admin
from .models import Categori
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ['category_name', 'slug']

admin.site.register(Categori,CategoryAdmin)