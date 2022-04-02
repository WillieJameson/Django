from django.shortcuts import render
# from django.conf import settings
from .forms import UploadForm
from .models import ExampleModel


# from PIL import Image
# import os


# Create your views here.
# def media_example(request):
#     if request.method == 'POST':
#         form = UploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             save_path = os.path.join(settings.MEDIA_ROOT, request.FILES["file_upload"].name)
#             with open(save_path, "wb") as output_file:
#                 for chunk in form.cleaned_data['file_upload'].chunks():
#                     output_file.write(chunk)
#     else:
#         form = UploadForm()
#     return render(request, "media_example/media-example.html", {"form":form})
#
# def media_example(request):
#     if request.method == 'POST':
#         form = UploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             save_path = os.path.join(settings.MEDIA_ROOT, request.FILES["file_upload"].name)
#             image = Image.open(form.cleaned_data["file_upload"])
#             image.thumbnail((50, 50))
#             image.save(save_path)
#     else:
#         form = UploadForm()
#     return render(request, "media_example/media-example.html", {"form":form})

# def media_example(request):
#     instance = None
#     if request.method == 'POST':
#         form = UploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             instance = ExampleModel()
#             instance.image_field = form.cleaned_data["image_upload"]
#             instance.file_field = form.cleaned_data["file_upload"]
#             instance.save()
#     else:
#         form = UploadForm()
#     return render(request, "media_example/media-example.html", {"form": form, "instance": instance})

def media_example(request):
    instance = None
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            print(instance)
    else:
        form = UploadForm()
    return render(request, "media_example/media-example.html", {"form": form, "instance": instance})
