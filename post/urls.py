from .views import *
from django.urls import path, URLPattern
from django.conf import settings
from django.conf.urls.static import static

app_name = 'post'
urlpatterns = [
    path("postlist/",postlist,name="postlist"),
    path("upload/",uploadFile,name="uploadFile"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )