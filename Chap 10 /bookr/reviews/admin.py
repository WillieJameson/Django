from django.contrib import admin
from reviews.models import Publisher, Contributor, Book, BookContributor, Review


# class BookrAdminSite(admin.AdminSite):
#     title_header = 'Bookr Admin'
#     site_header = 'Bookr administration'
#     index_title = 'Bookr site admin'
#
#
# admin_site = BookrAdminSite(name='bookr')


class Bookadmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'
    list_display = ('title', 'isbn13', 'publication_date', 'publisher_name')
    list_filter = ('publisher', 'publication_date')
    search_fields = ['title', 'publisher__name']

    def publisher_name(self,obj):
        return obj.publisher.name


class ContributorAdmin(admin.ModelAdmin):
    list_display = ('last_names', 'first_names')
    list_filter = ('last_names',)
    search_fields = ('last_names__startswith', 'first_names')


# Register your models here.
admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, Bookadmin)
admin.site.register(BookContributor)
admin.site.register(Review)
