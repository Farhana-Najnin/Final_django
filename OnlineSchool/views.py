from django.shortcuts import render
from Courses.models import courses
from Category.models import Categori
from django.views.generic import TemplateView
# Create your views here.

def Contactus(request):
    data = courses.objects.all()
    courseCategory = Categori.objects.all()
    return render(request, 'contact.html')
def Service(request,category_slug = None):
    data = courses.objects.all()
    courseCategory = Categori.objects.all()

    if category_slug is not None:
        category = Categori.objects.get(slug = category_slug)
        data = courses.objects.filter(category = category)
    return render(request, 'services.html', {'data': data, 'course_category': courseCategory})
def Certification1(request):
    data = courses.objects.all()
    courseCategory = Categori.objects.all()
    return render(request, 'certification.html')
def support1(request):
    data = courses.objects.all()
    courseCategory = Categori.objects.all()
    return render(request, 'support.html')
def Aboutus(request):
    data = courses.objects.all()
    courseCategory = Categori.objects.all()
    return render(request, 'about.html')
def Blog(request):
    data = courses.objects.all()
    courseCategory = Categori.objects.all()
    return render(request, 'blog.html')

def home(request, category_slug = None):
    data = courses.objects.all()
    courseCategory = Categori.objects.all()

    if category_slug is not None:
        category = Categori.objects.get(slug = category_slug)
        data = courses.objects.filter(category = category)

    return render(request, 'index.html', {'data': data, 'course_category': courseCategory})
def showCourses(request,category_slug=None):
    data = courses.objects.all()
    courseCategory = Categori.objects.all()

    if category_slug is not None:
        category = Categori.objects.get(slug = category_slug)
        data = courses.objects.filter(category = category)

    return render(request, 'course.html', {'data': data, 'course_category': courseCategory})