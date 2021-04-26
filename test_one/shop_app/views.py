from django.conf.global_settings import STATIC_URL
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse

from .forms import Shop_Add
from .models import Shop_Item


def index(request):
    products = Shop_Item.objects.all()
    context = {
        "products": products,
        "data": "hello"
    }
    return render(request, template_name="index.html", context=context)


def form(request):
    if request.method == "POST":
        product_form = Shop_Add(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse("shop_app:shop"))
    else:
        product_form = Shop_Add()

    content = {"product_form": product_form}
    return render(request, "form.html", content)


def save_form(request):
    if request.method == "GET":
        product_form = Shop_Add()

        content = {"product_form": product_form}
        return render(request, "save_form.html", content)
    else:
        product_form = Shop_Add(request.POST, request.FILES)
        products = Shop_Item.objects.all()
        content = {
            "product_form": product_form,
            "products" : products
                   }

        return render(request, "index.html", content)

