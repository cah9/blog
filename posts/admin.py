from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']
    list_editable = ['title']

admin.site.register(Post, PostAdmin)