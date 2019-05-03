from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
# Dont Repeat Yourself = DRY

from .forms import ConcatForm

def home_page(request):
    my_title = "hello there..."
    context  =  {"title": "My title"}
    if request.user.is_authenticated:
        context  = {"title": my_title, "my_List": [1, 2, 3, 4 ,5]}
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
