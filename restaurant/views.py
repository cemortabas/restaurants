from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):

    some_list = [random.randint(0, 1000), random.randint(0, 1000), random.randint(0, 1000), random.randint(0, 1000)]

    if len(some_list)>0:
        run = True


    context = {
        "html_name":"random number",
        "some_list":some_list,
        "run":run
    }

    return render(request, "home.html", context)

def about(request):
    context = {}
    return render(request, "about.html", context)

def contact(request):
    context = {}
    return render(request, "contact.html", context)