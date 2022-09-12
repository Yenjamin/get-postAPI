from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.dogs, name = 'dogs'),
    # path('add/', views.echoing, name="formPage")
    path('add/', views.profilePic, name="formPage")
]