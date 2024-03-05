from django.shortcuts import render
from Courses.models import courses
from Category.models import Categori
from django.views.generic import TemplateView
# Create your views here.

def Contactus(request):
    data = courses.objects.all()
    courseCategory = Categori.objects.all()
    return render(request, 'contactUs.html')
def Aboutus(request):
    data = courses.objects.all()
    courseCategory = Categori.objects.all()
    return render(request, 'aboutus.html')
def home(request, category_slug = None):
    data = courses.objects.all()
    courseCategory = Categori.objects.all()

    if category_slug is not None:
        category = Categori.objects.get(slug = category_slug)
        data = courses.objects.filter(category = category)

    return render(request, 'home.html', {'data': data, 'course_category': courseCategory})
def showCourses(request,category_slug=None):
    data = courses.objects.all()
    courseCategory = Categori.objects.all()

    if category_slug is not None:
        category = Categori.objects.get(slug = category_slug)
        data = courses.objects.filter(category = category)

    return render(request, 'course.html', {'data': data, 'course_category': courseCategory})