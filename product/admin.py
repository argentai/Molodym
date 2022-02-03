from django.contrib import admin
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms



class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Product
        fields = '__all__'

class ContactAdminForm(forms.ModelForm):
    message = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Contact
        fields = '__all__'

class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ('id', 'title', 'description', 'price', 'image', 'image')
    list_display_links = ('id', 'title')


class ContactAdmin(admin.ModelAdmin):
    form = ContactAdminForm
    list_display = ('id', 'name', 'phone', 'email', 'message',)
    list_display_links = ('id', 'name')



admin.site.register(Product,ProductAdmin)
admin.site.register(Contact,ContactAdmin)

# Register your models here.
