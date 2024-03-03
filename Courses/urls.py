from django.urls import path
from . import views
urlpatterns = [
    path('coursess/', views.CoursePost.as_view(), name='coursePost'),
    path('course_detail/<int:id>', views.CourseDetailsPost.as_view(), name='course_details'),
    # path('return/<int:id>/', views.returnBook, name='return'),
    path('enroll/<int:id>/', views.enrollCourse, name='enroll'),

]