from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('archive/', views.archive, name='archive'),
    path('download/', views.download_video_file, name='download_video_file'),
]