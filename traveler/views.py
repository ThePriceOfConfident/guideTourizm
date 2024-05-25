from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from Destination.models import Destination
from traveler.models import Traveler
from utils import helpers
from django.contrib.auth.decorators import login_required
# Create your views here.

def logout_view(request):
    logout(request)
    return redirect('login')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home') 
    else:
        form = UserCreationForm()  
    companyInfo = helpers.getCompanyInfo()
    return render(request, 'signup.html', {'form': form, 'errors': form.errors,'companyInfo':companyInfo })


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            next_url = request.GET.get('next', 'home')
            if(next_url):
                return redirect(next_url)
            else:
                return  redirect('profile')
    else:
        form = AuthenticationForm()
    companyInfo = helpers.getCompanyInfo()
    return render(request, 'login.html', {'form': form, 'errors': form.errors,'companyInfo':companyInfo})



@login_required
def profile(request):
    user = request.user
    companyInfo = helpers.getCompanyInfo()
    destinations = list(Destination.objects.all().order_by('created')[:4])
    for des in destinations:
        print(des.cover_image.url)
    try:
        travelerProfile = Traveler.objects.get(user=user)
    except Traveler.DoesNotExist:
        travelerProfile = Traveler.objects.get_or_create(user=user , email=user.email)

    if request.method == 'POST':
        print(request.POST.get('first_name'))
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        user.save()

        travelerProfile.phone_number = request.POST.get('phone_number', travelerProfile.phone_number)
        travelerProfile.country = request.POST.get('country', travelerProfile.country)
        travelerProfile.address = request.POST.get('address', travelerProfile.address)
        travelerProfile.save()

        travelerProfile.save()
    
    context = {
        'profile_user': travelerProfile,
        'user': user,
        'companyInfo': companyInfo,
        'destinations': destinations
    }
    return render(request, 'profile.html', context)