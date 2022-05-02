from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views
from . import api_views

router = DefaultRouter()
router.register(r'books', api_views.BookViewSet)
router.register(r'reviews', api_views.ReviewViewSet)


urlpatterns = [
    path('', views.index, name='welcome_view'),
    path('books/', views.book_list, name='book_list'),
    path('book/<int:pk>', views.book_detail, name='book_detail'),
    path('book-search/', views.book_search, name="book-search"),
    path('publishers/<int:pk>/', views.publisher_edit, name='publisher_edit'),
    path('publishers/new/', views.publisher_edit, name='publisher_create'),
    path('books/<int:book_pk>/reviews/new/', views.review_edit, name='review_create'),
    path('books/<int:book_pk>/reviews/<int:review_pk>/', views.review_edit, name='review_edit'),
    path('books/<int:pk>/media/', views.book_media, name="book_media"),
    path('api/', include((router.urls, 'api'))),
    path('api/login', api_views.Login.as_view(), name='login'),
    path('react-example/', views.react_example, name='react_example'),

    # path('api/first_api_view/', api_views.first_api_view, name="api_view"),
    # path('api/all_books/', api_views.AllBooks.as_view(), name="all_books"),
    path('api2/contributors/', api_views.ContributorView.as_view(), name="all_contributor"),
]