from django.shortcuts import render ,HttpResponse
from myapp.models import Category,Image
# Create your views here.

def show_home_page(request):
    images = Image.objects.all()
    cat = Category.objects.all()
    data={'images':images,'cat':cat}

    return render(request,'myapp/home.html',data)

def show_category_page(request,id):
    images = Image.objects.filter(cat=id)
    cat = Category.objects.all()
    data={'images':images,'cat':cat}

    return render(request,'myapp/home.html',data)