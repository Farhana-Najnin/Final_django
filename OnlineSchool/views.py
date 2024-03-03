from django.shortcuts import render
from Courses.models import courses
from Category.models import Categori

def home(request, category_slug = None):
    data = courses.objects.all()
    courseCategory = Categori.objects.all()

    if category_slug is not None:
        category = Categori.objects.get(slug = category_slug)
        data = courses.objects.filter(category = category)

    return render(request, 'home.html', {'data': data, 'course_category': courseCategory})