from django.http import HttpResponse
from django.shortcuts import render

# Dont Repeat Yourself = DRY

def home_page(request):
    my_title = "hello there..."
    return render(request, "hello_word.html", {"title": my_title})


def about_page(request):
    return render(request, "about.html", {"title": "About"})


def contact_page(request):
    return render(request, "hello_word.html", {"title": "Contact"})
