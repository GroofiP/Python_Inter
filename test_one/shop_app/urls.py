from django.contrib import admin
from django.urls import path

from .views import index, form, save_form

app_name="shop_app"

urlpatterns = [
    path('', index, name="shop"),
    path('form/', form, name="form"),
    path('save_form/', save_form, name="save_form"),
]
