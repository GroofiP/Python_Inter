from django.contrib import admin
from django.urls import path

from .views import index, form

urlpatterns = [
    path('', index, name="shop"),
    path('form/', form, name="form"),
]
