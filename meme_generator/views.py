from django.shortcuts import render

#from django.http import HttpResponse
from .logic import search_images, extract_urls, download_image, generate_meme

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

def text_view(request, *args, **kwargs):
    image_url = kwargs['image_url']
    context = {}
    context['image_url'] = image_url

    return render(request, "text.html", context)

def complete_view(request, *args, **kwargs):
    if request.method == "POST":
        image_url = kwargs['image_url']
        image_dir = "meme_background.jpg"
        meme_text = request.POST.get("memetext")
        meme_dir = "meme.png"

        download_image(image_url, image_dir)
        generate_meme(image_dir, meme_text, meme_dir)

        context = {}
        context['meme_dir'] = meme_dir

        return render(request, "complete.html", context)