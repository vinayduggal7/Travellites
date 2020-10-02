from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def destination(request):
    return render(request,'destination.html')

def hotel(request):
    return render(request,'hotel.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

