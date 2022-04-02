from django import forms
from .models import ExampleModel


# class UploadForm(forms.Form):
#     image_upload = forms.ImageField()
#     file_upload = forms.FileField()

class UploadForm(forms.ModelForm):
    class Meta:
        model = ExampleModel
        fields = "__all__"