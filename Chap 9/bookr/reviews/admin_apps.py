from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class ReviewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reviews'


class ReviewsAdminConfig(AdminConfig):
    default_site = 'admin.BookrAdminSite'
