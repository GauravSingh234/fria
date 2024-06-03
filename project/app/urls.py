from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('blog-1.html', views.blog_1 , name="blog_1"),
    path('blog-2.html', views.blog_2 , name="blog_2"),
    path('about.html', views.about , name="about"),
    path('contact.html', views.contact , name="contact"),
    path('team.html', views.team , name="team"),
    path('index.html', views.index , name="index"),
    path('projects.html', views.projects , name="projects"),
    path('projects-1.html', views.projects1 , name="projects1"),
    path('pricing.html', views.pricing , name='pricing'),
    path('coming-soon.html' , views.comingsoon , name='coming-soon'),
    path('faq.html' , views.faq , name="faq"),
    path('index-2.html', views.index2 , name="index"),
    path('index-3.html', views.index3, name="index"),
    path('index-4.html', views.index4 , name="index"),
    path('index-5.html', views.index5 , name="index"),
    path('index-6.html', views.index6 , name="index"),
    path('index-7.html', views.index7 , name="index"),
    path('index-8.html', views.index8 , name="index"),
    path('index-9.html', views.index9 , name="index"),
    path('index-10.html', views.index10 , name="index"),
    path('services.html' , views.services , name= "services"),
    path('services-1.html' , views.services1 , name= "services-1"),
    path('services-2.html' , views.services2 , name= "services-2"),
    path('services-3.html' , views.services3 , name= "services-3"),
    path('sign-up.html' , views.signup , name= "sign-up"),
    path("single-services.html" , views.singleservices , name= "single-services"),
    path("terms-condition.html" , views.termscondition , name ="terms-condition"),
    path("privacy-policy.html" , views.privacypolicy , name="privacy-policy")


]