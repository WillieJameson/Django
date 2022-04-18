from django.http import HttpResponse
from django.views.generic.edit import FormView, UpdateView, CreateView, DeleteView
from django.views.generic import DetailView
from django.views import View
from .models import Book

from .forms import BookForm


# Create your views here.

class BookRecordFormView(FormView):
    template_name = "book_management/book_form.html"
    form_class = BookForm
    success_url = '/book_management/entry_success'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class BookCreateView(CreateView):
    model = Book
    fields = ['name', 'author']
    template_name = 'book_management/book_form.html'
    success_url = '/book_management/entry_success'


class BookUpdateView(UpdateView):
    model = Book
    fields = ['name', 'author']
    template_name = 'book_management/book_form.html'
    success_url = '/book_management/entry_success'


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_management/book_delete_form.html'
    success_url = '/book_management/delete_success'


class BookRecordDetailView(DetailView):
    model = Book
    template_name = 'book_management/book_detail.html'


class DeleteSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Book record deleted successfully")


class FormSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Book record saved successfully")
