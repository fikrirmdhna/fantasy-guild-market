from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from main.forms import ProductForm
from django.urls import reverse
from .models import Items


# Create your views here.
def show_main(request):
    items = Items.objects.all()

    context = {
        'name': 'Fikri Dhiya Ramadhana',
        'class': 'PBP C',
        'amount': 0,
        'items' : items,
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Items.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Items.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Items.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Items.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def delete(request, id):
    Items.objects.get(pk=id).delete()
    return HttpResponseRedirect(reverse('main:show_main'))