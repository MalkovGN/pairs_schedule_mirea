from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('api/all_groups', views.GroupsScheduleView.as_view()),
    path('api/group/<str:group_name>/', views.GroupScheduleView.as_view()),
]
