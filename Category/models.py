from django.db import models

# Create your models here.

class Categori(models.Model):
    category_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length = 200,unique=True, null=True, blank=True)
    
    def __str__(self):
        return self.category_name