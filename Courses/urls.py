from django.urls import path
from . import views
urlpatterns = [
    path('coursess/', views.CoursePost.as_view(), name='coursePost'),
    path('course_detail/<int:id>', views.CourseDetails, name='course_details'),
    # path('return/<int:id>/', views.returnBook, name='return'),
    path('enroll/<int:id>/', views.enrollCourse, name='enroll'),
    path('complete/<int:id>/', views.completeCourse, name='complete'),
    path('addcourse/', views.AddCourse.as_view(), name = 'add_course'),
    path('editcourse/<int:id>', views.EditCourse.as_view(), name = 'edit_course'),
    path('deletecourse/<int:id>', views.DeleteCourse.as_view(), name = 'delete_course'),
     

]