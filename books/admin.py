from django.contrib import admin
from .models import Book, User 

# Register your models here.

@admin.register(User)
class BookAdmin(admin.ModelAdmin):

    admin.site.register(Book)
