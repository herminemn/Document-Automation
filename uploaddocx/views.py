from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UploadFileForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from docx import Document
import re


def docx_words_replace(doc_obj, regex, replace):

    for p in doc_obj.paragraphs:
        if regex.search(p.text):
            inline = p.runs

            for i in range(len(inline)):
                if regex.search(inline[i].text):
                    text = regex.sub(replace, inline[i].text)
                    inline[i].text = text

    for table in doc_obj.tables:
        for row in table.rows:
            for cell in row.cells:
                docx_words_replace(cell, regex, replace)


my_regex = re.compile(r"\{(.*?)\}")
my_replace = r"replaced_word"


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        document = Document(filename)
        # docx_words_replace(document, my_regex, my_replace)
        variables = []
        for paragraph in document.paragraphs:
            match = re.findall(r"\{(.*?)\}", paragraph.text)
            variables.append(match)
        for table in document.tables:
            for row in table.rows:
                for cell in row.cells:
                    match = re.findall(r"\{(.*?)\}", cell.text)
                    variables.append(match)
        document.save('result.pdf')
        return render(request, 'uploaddocx/upload.html', {'variables': variables})
    return render(request, 'uploaddocx/upload.html')
