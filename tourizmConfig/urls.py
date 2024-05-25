from django.urls import path
from .views import home, about,contact,success_message,news_letter,success_News

urlpatterns = [
    path('', home, name='home'), 
    path('about-us/', about, name='about-us'), 
     
    path('contact-us/',contact,name='contact-us'),
    path('newsLetter/', news_letter,name="add_news_letter"),
    path('success-message/',success_message,name="success_message"),
    path('success_News_letter/',success_News,name="success_News"),
]