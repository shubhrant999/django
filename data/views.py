from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from .forms import ProductForm

# Create your views here.
def homePage(requests):
    return render(requests, 'index.html', {})

# Create your views here.
def aboutPage(requests):
    return render(requests, 'about.html', {})

def searchPage(requests):
    productform = ProductForm()

    if requests.method == 'POST':
        data = {
            'keyword': requests.POST['keyword'],
            'type': requests.POST['type'],
            'city': requests.POST['city'],
            'bedroom': requests.POST['bedroom'],
            'garage': requests.POST['garage'],
            'bathroom': requests.POST['bathroom'],
            'price': requests.POST['price'],
        }


        return render(requests, 'property-grid.html', {'form': productform, 'data':data})       
    else:
        return render(requests, 'about.html', {})




