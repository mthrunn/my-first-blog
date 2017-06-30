from django.contrib import admin
from .models import Post

# Register your models here.
class AdminPost(admin.ModelAdmin):
    list_display = ('title','created_date',)
    search_fields = ['title','text']

admin.site.register(Post, AdminPost)