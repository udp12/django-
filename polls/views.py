from django.shortcuts import render, redirect,render_to_response,get_object_or_404
from django.http import HttpResponse
from polls.forms import ContactForm,UserLogin,EntryForm,User_Login_Form,UserRegistrationForm,ContactEmailForm,Uday_Login_form,File_Upload_Form,Audio_Video_Form
from polls.models import Contact,Address,Login,Entry,Bhavcopy,Files_Upload_Model,Audio_Video_models
from django.contrib.auth import authenticate, login,logout,get_user_model
from django.core.mail import send_mail
from django.conf import settings
from django.db import connection
from django.http import HttpResponse, JsonResponse
import datetime
from django import forms
import json
from django.template import *

import logging as log

def home_view(request):
    context ={}
    return render(request, 'home.html',context)


def index(request):
    return HttpResponse("Hello uday")

def html(request):
    context ={}
    return render(request, 'hello1.html',context)

def html1(request):
    context ={}
    return render(request, 'new.html',context)

def modify_html(request):
    context={'Name':'uday','location':'Hyderabad'}
    return render(request,'hello1.html',context)

def hello_1(request):
    context={'namesdb':[{'Name':'uday','Location':'Miryalaguda'},{'Name':'kumar','Location':'Delhi'}]}
    return  render(request,'hello1.html',context)




def Contact_Form (request):
    if request.method == 'POST':
        Contact.objects.create(name=request.POST['name'],location=request.POST['location'],age=request.POST['age'])
        return redirect('/home/')
    else:
        form=ContactForm()
        context={'form':form}
        return render(request,'form.html',context)


def User_Login(request):
    if request.method == 'POST':
        Login.objects.create(name=request.POST['name'],email=request.POST['email'],password=request.POST['password'])
        return redirect('/home/')
    else:
        form=UserLogin()
        context={'form':form}
        return render(request,'contact.html',context)


def Entry_one(request):
    if request.method == 'POST':
        Entry.objects.create(name=request.POST['name'],password=request.POST['password'],age=request.POST['age'],email=request.POST['email'],phone_number = request.POST['phone_number'])
        return redirect('/home/')
    else:
        form=EntryForm()
        context={'form':form}
        return render(request,'entry.html',context)

def uday_login(request):
    if request.method == 'POST':
        Entry.objects.create(name=request.POST['name'], password=request.POST['password'], age=request.POST['age'],
                             email=request.POST['email'], phone_number=request.POST['phone_number'])


        return redirect('/html/')
    else:
        form = EntryForm()
        context = {'form': form}
        return render(request, 'udaylogin.html', context)




def uday_authenticate(request):
    title='Submit'
    form=Uday_Login_form(request.POST or None)
    if form.is_valid():

        ''' without getting all the data of table this can filter fastly'''
        cursor=connection.cursor()
        cursor.execute("select name,password from polls_entry where name='%(name)s' and password='%(password)s' "%form.cleaned_data )
        row=cursor.fetchall()
        ''' getting all the data of table '''
        #row=Entry.objects.all()
        if row:
            return redirect('/home_view/')
        else:
            return HttpResponse('Not valid')
    return render(request,'udaylogin2.html',{'form':form,'title':title})

def login_view(request):
    print (request.user.is_authenticated())
    form=User_Login_Form(request.POST or None)
    title='Login'
    if form.is_valid():
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        user=authenticate(username=username,password=password)
        login(request,user)
        return redirect('/html/')
        print (request.user.is_authenticated())

    return render(request,'form.html',{'form':form, 'title':title})



def register_view(request):
    title='Register'
    form=UserRegistrationForm(request.POST or None)
    if form.is_valid():
        user=form.save(commit=False)
        password=form.cleaned_data.get('password')
        user.set_password(password)
        user.save()

        new_user = authenticate(username=user.username, password=password)
        login(request,new_user)
        return redirect('/')

    context={'form':form, 'title':title}
    return render(request,'form.html',context)


def logout_view(request):
    logout(request)
    return render(request,'form.html',{})

def contact(request):
    form =ContactEmailForm(request.POST or None)
    if form.is_valid():
        email=form.cleaned_data.get('email')
        name=form.cleaned_data.get('name')
        message=form.cleaned_data.get('message')
        subject='site contact form message'
        from_email=settings.EMAIL_HOST_USER
        to_email=[from_email,email]
        contact_message='%s: %s via %s ' %(email,name,message)
        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  fail_silently=False)
        return redirect('/html/')

    context={'form':form}
    return render(request,'contactemail.html',context)

def mainpage(request):
    context={}
    return render(request,'mainpage.html',context)





def detailedRange(request):
    code= request.GET.get('code')
    stdate = request.GET.get('stdate')
    enddate = request.GET.get('enddate')
    sdate = datetime.datetime.strptime(stdate, '%d%m%Y')
    edate = datetime.datetime.strptime(enddate, '%d%m%Y')
    scrips = Bhavcopy.objects.filter(sc_code=code, bhav_date__gte=sdate, bhav_date__lte=edate)
    response ={}
    for scrip in scrips:
        response[str(scrip.bhav_date)] = {'open':scrip.open, 'close':scrip.close}
    #return JsonResponse(response)
    #return render(request,'samba.html',{'res':response})
    return render_to_response('samba.html',{'res':response})



def samba_html(request):
    context ={}
    return render(request, 'samba.html',context)


def File_Upload_View(request):
    if request.method == 'POST':
        form=File_Upload_Form(request.POST,request.FILES)
        if form.is_valid():
            new_form=Files_Upload_Model(files=request.FILES['files'])

            new_form.save()
            return  HttpResponse('Uploaded........')
    else:
        form=File_Upload_Form()
    documents=Files_Upload_Model.objects.all()
    return render(request,'fileupload.html',{'documents':documents, 'form':form })

def File_Upload_Html_To_Other(request):
    print '************************************1111'
    #sell=get_object_or_404(Files_Upload_Model)
    sell=Files_Upload_Model.objects.all()
    print '*************************************',sell

    return render_to_response('display.html',{'sell':sell})




def Audio_Video_View(request):
    if request.method == 'POST':
        form=Audio_Video_Form(request.POST, request.FILES)
        if form.is_valid():
            new_form=Audio_Video_models(audio=request.FILES['audio'],video=request.FILES['video'])

            print new_form,'***************'
            new_form.save()
            return HttpResponse('yes uploaded......')
    else:
        form=Audio_Video_Form()
    documents=Audio_Video_models.objects.all()

    return render_to_response('audio_video.html',{'documents':documents, 'form':form},context_instance=RequestContext(request))






