from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UploadFileForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from docx import Document
from docx.enum.style import WD_STYLE_TYPE


def work_with_docs(request):
    pass


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        document = Document(filename)
        document.save(filename)
        # [[run.text for run in p.runs if run.italic] for p in document.paragraphs]
        variables = []
        for p in document.paragraphs:
            for run in p.runs:
                if run.italic:
                    variables.append(run.text)
        return render(request, 'uploaddocx/upload.html', {'variables': variables})
    return render(request, 'uploaddocx/upload.html')
