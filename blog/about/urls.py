from django.urls import path
from about import views

urlpatterns = [
    path("", views.about, name ="about"),
    path("melina/", views.melina, name ="melina"),
    path("pablo/", views.pablo, name ="pablo"),
]