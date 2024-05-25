from django.db import models
from django.shortcuts import render
 
class CompanyInfo(models.Model):
    name = models.CharField(max_length=255, verbose_name="Company Name")
    description = models.TextField(verbose_name="Company Description")
    address = models.CharField(max_length=255, verbose_name="Company Address")
    website = models.CharField(max_length=255, verbose_name="Company Address", default="www.travela.com")
    phone = models.CharField(max_length=20, verbose_name="Phone Number")
    email = models.EmailField(verbose_name="Email Address")
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True, verbose_name="Company Logo")
    about_us = models.TextField(blank=True, verbose_name="About Us")
    facebook_url = models.URLField(blank=True, verbose_name="Facebook Page URL")
    twitter_url = models.URLField(blank=True, verbose_name="Twitter Handle URL")
    instagram_url = models.URLField(blank=True, verbose_name="Instagram Page URL")
    linkedin_url = models.URLField(blank=True, verbose_name="LinkedIn Page URL")
    youtube_url = models.URLField(blank=True, verbose_name="YouTube Channel URL")

    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    name = models.CharField("Name", max_length=100)
    email = models.EmailField("Email Address", blank=True)
    subject = models.CharField("Subject", max_length=100, blank=True)
    message = models.TextField("Message", blank=True, null=True)
    company = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE, related_name='Contact',blank=True)
    def __str__(self):
        return self.name


class NewsLetter(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated")
    email = models.CharField(verbose_name="email", max_length=200)
    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "Email News Letter"
        verbose_name_plural = "Email News Letters"