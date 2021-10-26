from django.urls import path

from . import views

urlpatterns = [
    path('hello/', views.hello_world_view),
    path('promote/<str:name>/', views.class_members_view),
]
