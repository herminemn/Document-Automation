from django import forms
from .models import DocFile


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = DocFile
        fields = ('contract_Title', 'contract_Doc_File')
