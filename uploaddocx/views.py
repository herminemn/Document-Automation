from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UploadFileForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from docx import Document
from docx.enum.style import WD_STYLE_TYPE


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        document = Document(filename)
        document.save(filename)
        my_list = []
        for p in document.paragraphs:
            for run in p.runs:
                if run.italic:
                    my_list.append(run.text)

        return HttpResponse(my_list)

        # return render(request, 'uploaddocx/upload.html', {
        #     'filename': filename
        # })
    return render(request, 'uploaddocx/upload.html')
