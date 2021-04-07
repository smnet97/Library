from rest_framework import serializers
from . import models
from .models import Book, LibUser, RentBook


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        models = Book
        fields = '__all__'


class LibUserSerializer(serializers.ModelSerializer):

    class Meta:
        models = LibUser
        fields = '__all__'


class RentBookSerializer(serializers.ModelSerializer):

    class Meta:
        models = RentBook
        fields = '__all__'
