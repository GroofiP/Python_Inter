from django.conf.global_settings import STATIC_URL
from django.http import HttpResponseRedirect, JsonResponse
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


def save_form(request, form=Shop_Add()):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            goods = Shop_Item.objects.all()
            data['html_good_list'] = render_to_string('index.html', {
                'goods': goods
            })
        else:
            data['form_is_valid'] = False
    context = {'product_form': form}
    data['html_form'] = render_to_string("save_form.html", context, request=request)
    return JsonResponse(data)
