from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path
# from django.contrib.admin.apps import AdminConfig
# from django.contrib.auth.admin import User


# Register your models here.
class BookrAdmin(admin.AdminSite):
    site_header = "Bookr Administration Portal"
    site_title = "Bookr Administration Portal"
    index_title = "Bookr Administration"
    logout_template = 'admin/logout.html'

    def get_urls(self):
        urls = super().get_urls()
        urlpatterns = [path("admin_profile/", self.admin_view(self.profile_view))]
        return urls + urlpatterns

    def profile_view(self, request):
        request.current_app = self.name
        context = self.each_context(request)
        return TemplateResponse(request, "admin/admin_profile.html", context)

# admin_site = BookrAdmin(name='bookr_admin')
# admin_site.register(User)




