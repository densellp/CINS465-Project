from django.contrib import admin

# Register your models here.

from .models import testTable, Profile, Comment, Post

admin.site.register(testTable)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)