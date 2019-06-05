"""framework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from data.views import submitForm, searchPage, homePage, singleBlogPage
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^search/$', searchPage, name="search_page"),
    url(r'^submitForm$', submitForm, name="submit_form"),
    url(r'^blog-single/(?P<slug>[\w-]+)/$', singleBlogPage, name="blog_single_page"),
    url(r'^(?P<slug>[\w-]+)/$', homePage, name="home_page"),
    
   
# ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
