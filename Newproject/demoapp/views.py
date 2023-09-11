from django.shortcuts import render
from django.http import HttpResponse
from .models import Place


# Create your views here.
def demo(request):
    content = Place.objects.all()
    return render(request, "index.html", {'content': content})
