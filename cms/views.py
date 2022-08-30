from django.shortcuts import render

# Create your views here.


def sessite(request):
    return render(request, 'cms/toppage.html', {})



def originsite(request):
    return render(request, 'cms/origin.html', {})