from django.urls import path, include
from . import views

urlpatterns = [
    path('main', views.main),
    path('a', views.a),
]