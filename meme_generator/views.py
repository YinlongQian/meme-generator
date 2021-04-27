from django.shortcuts import render

#from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def result_view(request, *args, **kwargs):
    context = {
        'keyword': None
    }

    if request.method == "POST":
        context['keyword'] = request.POST.get("keyword")

    return render(request, "result.html", context)