from django.contrib import admin
from .models import CompanyInfo, ContactMessage, NewsLetter

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email','address']
    search_fields = ['name', 'email']
    

@admin.register(ContactMessage)
class ContactMessageoAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'email']
    search_fields = ['name', 'email']
    

@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ['created','email']
    search_fields = [ 'email']