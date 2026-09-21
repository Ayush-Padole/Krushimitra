from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Cropsdetail
from . models import Market_Price
from .models import Farmers
from . form import Farmerform
from KrushiMitra import settings
from django.core.mail import send_mail
from .models import Government
from .form2 import Farmer_registration
from .models import Farmer_training
from .models import Newsupdate

def home(request):
    template = loader.get_template('Home.html')
    return HttpResponse(template.render())

def news(request):
    all_news = Newsupdate.objects.all().order_by('-id').values()
    template = loader.get_template('News.html')
    context = {
        'all_news':all_news,
    }
    return HttpResponse(template.render(context, request))

def market(request):
    p1 = Market_Price.objects.all().values()
    template = loader.get_template('Market_price.html')
    context = {
        'p1':p1,
    }
    return HttpResponse(template.render(context, request))

def crops(request):
    c1 = Cropsdetail.objects.all().values()
    template = loader.get_template('Crops.html')
    context = {
        'c1':c1,
    }
    return HttpResponse(template.render(context, request))


def government(request):
    g1 = Government.objects.all().values()
    template = loader.get_template('Government_schemes.html')
    context = {
        'g1':g1,
    }
    return HttpResponse(template.render(context, request))


def expert(request):
    if request.method == 'POST':
        fm = Farmerform(request.POST)
        if fm.is_valid():
            subject = "Enquiry for Farmer"
            name = fm.cleaned_data['name']
            phone = fm.cleaned_data['phone']
            village = fm.cleaned_data['village']
            taluka = fm.cleaned_data['taluka']
            district = fm.cleaned_data['district']
            problem = fm.cleaned_data['problem']
            to='padoleayush@gmail.com'
            msg = f"\n name  :-{name} \n phone number  :-{phone} \n village name :-{village} \n taluka name :-{taluka} \n district name is:-{district} \n and problems is :-{problem}"
            send_mail(subject, msg, settings.EMAIL_HOST_USER, [to], fail_silently=False,)
            return render(request,'home.html')
    else:
        fm = Farmerform()
    return render(request,'Experts.html',{'form':fm})


def trainning(request):
    if request.method == 'POST':
        fm = Farmer_registration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            age = fm.cleaned_data['age']
            cn = fm.cleaned_data['contact_number']
            vil = fm.cleaned_data['village']
            tal  = fm.cleaned_data['taluka']
            dist = fm.cleaned_data['district']
            cd = fm.cleaned_data['crop_detail']
            print(nm)
            print(age)
            print(cn)
            print(vil)
            print(tal)
            print(dist)
            print(cd)
            reg = Farmer_training(name=nm,age=age,contact_number=cn,village=vil,taluka=tal,district=dist,crop_detail=cd)
            reg.save()
    else:
        fm =Farmer_registration()
    return render(request,'Trainning.html',{'form2':fm})




# Create your views here.
