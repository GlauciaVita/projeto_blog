from django.contrib import admin
from .models import Tag, Author, Post

# Register your models here.

class PostsAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date",)
    list_display = ("title", "date", "author",)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostsAdmin)
admin.site.register(Author)
admin.site.register(Tag)
