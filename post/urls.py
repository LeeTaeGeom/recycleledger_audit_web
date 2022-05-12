from django.urls import URLPattern, path
from .views import *


app_name = 'post'
urlpatterns = [
    path("postlist/",postlist,name="postlist"),
]