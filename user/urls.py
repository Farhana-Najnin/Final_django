from django.urls import path
from .views import SignUpFormView,LoginFormView,LogoutFormView,ActivationView,PasswordUpdateView,manage_course
from . import views
urlpatterns = [
    path('sign_up/',SignUpFormView.as_view(), name = 'signUp'),
    path('profile/',views.ProfileView, name = 'profile'),
    path('activate/<uidb64>/<token>/', ActivationView.as_view(), name='activate'),
    path('login/',LoginFormView.as_view(), name = 'login'),
    path('pass_word/', PasswordUpdateView.as_view(), name='password_change_page' ),
    path('logout/',LogoutFormView, name = 'logout'),
    path('course_manage/', views.manage_course, name='manage_course' ),
]