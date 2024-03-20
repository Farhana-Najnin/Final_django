from django.db import models
from Category.models import Categori
from django.contrib.auth.models import User 
from user.models import UserAccount
from .choice import ENROLLMENT_TYPE
# Create your models here.

class courses(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    category = models.ManyToManyField(Categori)
    image = models.ImageField(upload_to = 'media/uploads/',blank=True, null=True)
    borrowers = models.ManyToManyField(User, related_name='entrollers_course', blank=True, null=True)
    
    def __str__(self):
        return self.name


class Enroll(models.Model):
    user1 = models.ForeignKey(UserAccount,related_name='enrolls', on_delete = models.CASCADE)
    enrollment_type = models.IntegerField(choices=ENROLLMENT_TYPE, null=True)
    course = models.ForeignKey(courses, on_delete = models.CASCADE)
    enroll_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.enrollment_type}"