from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

# Create your views here.
def homePage(requests):
    return render(requests, 'index.html', {})

# Create your views here.
def aboutPage(requests):
    return render(requests, 'about.html', {})

def searchPage(requests):
    if requests.method == 'POST':
        data = {
            'type': requests.POST['type'],
        } 

        return render(requests, 'property-grid.html', {'listp': data})
    else:
        return render(requests, 'about.html', {})




