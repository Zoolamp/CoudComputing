from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<marquee><h1>This is the cloud computing class</h1></marquee>")
