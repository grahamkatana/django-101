
from django.contrib import admin
from .models import Post,Comment

# Register your models here.

class CommentItemInline(admin.TabularInline):
    model=Comment
    raw_id_fields=['post']

class PostAdmin(admin.ModelAdmin):
    search_fields=['title','intro','body']
    list_display = ['title','slug','created_at']
    inlines = [CommentItemInline]
    prepopulated_fields={'slug':('title',)}

class CommentAdmin(admin.ModelAdmin):
    search_fields=['email','body']
    list_display = ['email','name','created_at']
    list_filter = ['email','created_at']


admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
