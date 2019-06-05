from django import forms
from .models import Post
from django.contrib import admin

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=128)
    body = forms.CharField(max_length=245, label="Item Description.")

    class Meta:
        model = Post
        fields = ('title', 'body', )

        
# class BannerAdminForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(BannerAdminForm, self).__init__(*args, **kwargs)
#         self.fields['bannerfile'].widget = admin.widgets.AdminFileWidget()