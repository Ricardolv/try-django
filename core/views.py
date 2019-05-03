from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
# Dont Repeat Yourself = DRY

from .forms import ConcatForm
from blog.models import BlogPost

def home_page(request):
    my_title = "hello there..."
    qs = BlogPost.objects.all()[:5]
    context  =  {"title": "Welcome to Try Django 2.2", 'blog_list': qs}
    return render(request, "home.html", context)


def about_page(request):
    return render(request, "about.html", {"title": "About"})


def contact_page(request):
    form = ConcatForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ConcatForm()

    context = {
        "title": "Contact us",
        "form": form
    }
    return render(request, "form.html", context)


def example_page(request):
    context       = {"title": "Example"}
    template_name = "hello_word.html"
    template_obj  = get_template(template_name)
    rendered_item = template_obj.render(context)
    return HttpResponse(rendered_item)
