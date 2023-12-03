from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import book
from .serializer import BookSerializer

# Create your views here.

@api_view(['GET'])
def books(req):
    
    all_books = book.objects.all()
    serialized_data = BookSerializer(all_books, many=True)
    return Response(serialized_data.data)


@api_view(['GET'])
def books_by_author(req, author):
    
    all_books = book.objects.filter(author__iexact=author)
    serialized_data = BookSerializer(all_books, many=True)
    return Response(serialized_data.data)


@api_view(['GET'])
def books_by_id(req, id):
    
    all_books = book.objects.get(id=id)
    serialized_data = BookSerializer(all_books, many=True)
    return Response(serialized_data.data)


@api_view(['POST'])
def add_book(req):
    serialized_data = BookSerializer(data=req.date)
    if serialized_data.is_valid():
        serialized_data.save()
        
    return Response(serialized_data.data)


@api_view(['PUT'])
def put(req,id):
    all_book = book.objects.get(id=id)
    serialized_data = BookSerializer(date=req.date)
    if serialized_data.is_valid():
        serialized_data.save()
    return Response(serialized_data.data)


@api_view(['PATCH'])
def put(req,id):
    serialized_data = BookSerializer(date=req.date, partial=True)
    if serialized_data.is_valid():
        serialized_data.save()
    return Response(serialized_data.data)

@api_view(['DELETE'])
def delete(req):
    all_books = book.objects.get.all()
    all_books.delete()
    serialized_data = BookSerializer(all_books, many=True)
    return Response(serialized_data.data)



    