from .models import Book
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'synopsis', 'review', 'feature', 'publication_date', 'owner',)


