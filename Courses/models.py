from django.db import models
from Category.models import Categori
from django.contrib.auth.models import User 
# Create your models here.

class courses(models.Model):
    name = models.CharField(max_length=60)
    # price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(Categori,on_delete=models.CASCADE)
    description = models.TextField()
    # quantity = models.IntegerField()
    image = models.ImageField(upload_to = 'media/uploads/',blank=True,null=True)
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name


class Enroll(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    course = models.ForeignKey(courses, on_delete = models.CASCADE)
    enroll_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.user.username} - {self.course.name}"