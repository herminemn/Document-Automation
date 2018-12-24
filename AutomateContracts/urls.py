from django.conf.urls import url
from django.contrib import admin
from django.urls import path
import uploaddocx.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', uploaddocx.views.doc_list, name='doc_list'),
    path('upload/', uploaddocx.views.upload_doc, name='upload_doc'),
    path('upload/<int:pk>/', uploaddocx.views.delete_uploaded_doc, name='delete_uploaded_doc'),
    path('modify/', uploaddocx.views.modify, name='modify')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)