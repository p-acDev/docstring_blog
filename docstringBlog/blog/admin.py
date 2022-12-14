from django.contrib import admin
from .models import Post, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}

# Register your models here.
admin.site.register(Post, PostAdmin)

admin.site.register(Tag)