from django.urls import path
from . import views

app_name = 'editor'

urlpatterns = [
    path('', views.home, name="home"),
    path('submit/', views.submit, name="submit"),
    path('fetch_question/', views.fetch_question, name="fetch_question"),
    path('share/', views.share, name="share"),
    path('show/', views.show, name="show"),
    path('tempEdit/', views.edit_temp, name="tempEdit"),
]
