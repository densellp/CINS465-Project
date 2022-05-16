from django.forms import ModelForm
from .models import Post, Comment

class postForm(ModelForm):
    class Meta:
        model = Post
        #fields = ['profile', 'title', 'body', 'image']
        fields = ['title', 'body', 'image']
        
class commentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

# Dedicated to Justin Peters, Rest in Peace 2000-2022