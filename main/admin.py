from django.contrib import admin
from .models import Books
# Register your models here.

class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'is_published')
    list_display_links = ('id', 'title')

admin.site.register(Books, BooksAdmin)