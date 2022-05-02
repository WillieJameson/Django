from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.views import APIView

from .models import Book, Contributor, Review
from .serializers import BookSerializer, ContributorSerializer, ReviewSerializer


class Login(APIView):
    def post(self, request):
        user = authenticate(username=request.data.get("username"), password=request.data.get("password"))
        if not user:
            return Response({'error': 'Credentials are incorrect or user does not exist'}, status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=HTTP_200_OK)


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    """ curl -X get http://127.0.0.1:8000/api/books/  -H "Authorization: Token 01ae32f68f2595a247cb2309a2e978e592e751f7" 
    run this on command to run if you authenticated the API"""
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    authentication_classes = []
    permission_classes = []


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.order_by('-date_created')
    serializer_class = ReviewSerializer
    pagination_class = LimitOffsetPagination
    authentication_classes = []

class ContributorView(generics.ListAPIView):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer

# @api_view()
# def first_api_view(request):
#     num_books = Book.objects.count()
#     return Response({"num_book": num_books})


# class AllBooks(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# @api_view()
# def all_book(request):
#     books = Book.objects.all()
#     """many=True, which indicates that the books object is a queryset or a list of many objects"""
#     book_serializer = BookSerializer(books, many=True)
#     return Response(book_serializer.data)
