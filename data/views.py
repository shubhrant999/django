from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from .models import Post, Contact, Blog
from django.http import JsonResponse
# from django.forms import modelformset_factory
# from django.contrib import messages     

# from .forms import ImageForm, PostForm

# Create your views here.
def homePage(requests, slug):    
    if slug == 'blog-grid':
        posts = Blog.objects.all()
    else:
        posts = Post.objects.all()

    return render(requests, slug + '.html', {'slug': slug, 'posts': posts})

def singleBlogPage(requests, slug):
    blog = Blog.objects.get(pk=slug)
    return render(requests, 'blog-single.html', {'blog': blog})


def searchPage(requests):
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
        return render(requests, 'property-grid.html', {'data':data})        
    else:
        return render(requests, 'about.html', {})


def submitForm(requests):
    if requests.method == 'POST':       
        post=Contact()
        email = requests.POST.get('email')
        post.name= requests.POST.get('name')
        post.email= email
        post.subject= requests.POST.get('subject')
        post.message= requests.POST.get('message')     
        post.save() 
        if post.id != False:
            res = 'OK'
            return HttpResponse(res) 
        else:
            res = 'Something went wrong.Please try again.'
            return HttpResponse(res) 

def registrationForm(requests):
    if requests.method == 'POST':       
        post=Contact()
        email = requests.POST.get('email')
        post.name= requests.POST.get('name')
        post.email= email
        post.subject= requests.POST.get('subject')
        post.message= requests.POST.get('message')

        data = {
            'is_taken': Contact.objects.filter(email__iexact=email).exists()
        }
        if data['is_taken']:
            res = 'A user with this email already exists.'
            return HttpResponse(res)
        else:
            post.save()     
            res = 'OK'
            return HttpResponse(res)  
