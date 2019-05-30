from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.
def homePage(requests):
    return render(requests, 'index.html', {})

# Create your views here.
def aboutPage(requests):
    return render(requests, 'about.html', {})



def homePage(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'index.html', {'form': form})

