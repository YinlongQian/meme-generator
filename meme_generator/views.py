from django.shortcuts import render

#from django.http import HttpResponse
from .logic import search_images, extract_urls

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def result_view(request, *args, **kwargs):
    context = {
        'keyword': None
    }

    if request.method == "POST":
        image_keyword = request.POST.get("keyword")
        images = search_images(image_keyword)
        image_urls = extract_urls(images)

        context['keyword'] = image_keyword
        context['urls'] = image_urls

    return render(request, "result.html", context)

def complete_view(request, *args, **kwargs):
    image_url = kwargs['image_url']
    context = {}
    context['image_url'] = image_url

    return render(request, "complete.html", context)