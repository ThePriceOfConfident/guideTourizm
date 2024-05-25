from django.http import JsonResponse
from django.shortcuts import redirect, render

from django.shortcuts import render
from .models import CompanyInfo, ContactMessage, NewsLetter
from Destination.models import Destination

def home(request):
    company_info = CompanyInfo.objects.first()
    destinations = list(Destination.objects.all().order_by('created')[:8])
    context = {
        'companyInfo': company_info,
        'destinations': destinations
        
        }
    return render(request, 'home.html', context)


def about(request):
    company_info = CompanyInfo.objects.first()
    
    context = {
        'companyInfo': company_info,
     
        
        }
    return render(request, 'about-us.html', context)



# Create your models here.
def contact(request):
    company_info = CompanyInfo.objects.first()
    if request.method == 'POST':
  
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact_message = ContactMessage(
            company=company_info,
            name=name,
            email=email,
            subject=subject,
            message=message
        )


        contact_message.save()
        
        return redirect('success_message')
    context={
        "company_info" : company_info
    }
    return render(request, 'contact.html',context)


def success_message(request):
    company_info = CompanyInfo.objects.first()
    context={
        "company_info" :company_info
    }
     
    return render(request,'success_message.html',context)



def news_letter(request):
    company_info = CompanyInfo.objects.first()
    if request.method == 'POST':
        email = request.POST.get('email')
        # Save the email to newsletter
        news_letter = NewsLetter.objects.create(email=email)
        news_letter.save()
       
        return redirect('success_News')
    else:
        context={
        "company_info" : company_info
        }
        return render('success_News_letter.html',context)
    

def success_News(request):
    company_info = CompanyInfo.objects.first()
    
    context={
        "company_info" :company_info
    }
     
    return render(request,'success_news_letter.html',context)