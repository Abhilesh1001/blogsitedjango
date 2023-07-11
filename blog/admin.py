from django.contrib import admin

# Register your models here.
from .models import Post,BlogComment

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ['sno','title','author','content','timestamp']


@admin.register(BlogComment)
class AdminBlogComment(admin.ModelAdmin):
    list_display = ['sno','comment','user','post','parent','timestamp']
