from django.urls import path
from .views import CategoryView
urlpatterns = [
    path('category/', CategoryView.as_view())
]