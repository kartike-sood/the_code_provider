from django.urls import path
from . import views

app_name = 'userCodes'

urlpatterns = [
    path('', views.home, name="userCodes"),
    path('edit/', views.edit, name="editCode"),
]
