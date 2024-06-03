from django.shortcuts import render,HttpResponse

def blog_1(request):
    return render (request , "blog-1.html")


def blog_2(request):
    return render (request , "blog-2.html")


def about(request):
    return render (request , "about.html")


def contact(request):
    return render (request , "contact.html")


def team(request):
    return render (request , "team.html")

def index(request):
    return render (request , "index.html")

def projects(request):
    return render (request , "projects.html")

def projects1(request):
    return render (request , "projects-1.html")

def pricing(request):
    return render (request , "pricing.html")


def comingsoon(request):
    return render (request , "coming-soon.html" )

def faq(request):
    return render (request , "faq.html")

def index2(request):
    return render (request , "index-2.html")

def index3(request):
    return render (request , "index-3.html")

def index4(request):
    return render (request , "index-4.html")

def index5(request):
    return render (request , "index-5.html")

def index6(request):
    return render (request , "index-6.html")

def index7(request):
    return render (request , "index-7.html")

def index8(request):
    return render (request , "index-8.html")

def index9(request):
    return render (request , "index-9.html")

def index10(request):
    return render (request , "index-10.html")


def services(request):
    return render (request , "services.html")

def services1(request):
    return render (request , "services-1.html")

def services2(request):
    return render (request , "services-2.html")

def services3(request):
    return render (request , "services-3.html")


def signup(request):
    return render (request , "sign-up.html")


def singleservices(request):
    return render (request , "single-services.html")


def termscondition(request):
    return render (request , "terms-condition.html")
    

def privacypolicy(request):
    return render (request , "privacy-policy.html")