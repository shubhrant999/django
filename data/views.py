from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.
def homePage(requests):
    return render(requests, 'index.html', {})

# Create your views here.
def aboutPage(requests):
    return render(requests, 'about.html', {})

# Create your views here.
def aboutPage1(requests):
    return render(requests, 'about.html', {})







