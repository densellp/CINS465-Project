from django.forms import ModelForm
from .models import Post

class postForm(ModelForm):
    class Meta:
        model = Post
        fields = ['profile', 'title', 'body', 'image']
        #fields = ['title', 'body', 'image']