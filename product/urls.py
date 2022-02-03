from  django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
from .views import main,contact,shoes,collection,racing_boots
urlpatterns = [
    path('',main),
    path('contact/',contact),
    path('shoes/',shoes),
    path('collection/',collection),
    path('product/',racing_boots),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
]
