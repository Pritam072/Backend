from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from myapp.models import ContactForm, ContactFormSerialzer
from django.conf import settings
from django.core.mail import send_mail
from myapp.models import House,Signup
from django.core.paginator import Paginator
from rest_framework.views import APIView
from rest_framework import mixins,generics
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout


# Create your views here.
# def index(request):
   
#     # return httpresponse('welcome my wbsite')
#     return render(request,'index.html')
def home(request):

    houseData=House.objects.all().order_by('-id')
    paginator = Paginator(houseData,2)
    page_number = request.GET.get('page')
    houseDatafinal=paginator.get_page(page_number)

    data={
        'houseData':houseDatafinal
    }


    

    # return httpresponse('welcome my wbsite')
    return render(request,'index.html',data)
def price(request):
    # return httpresponse('welcome my wbsite')
    return render(request,'price.html')
def house(request):
    houseData=House.objects.all().order_by('-id')[:9]
    if request.method=="GET":
        st=request.GET.get('searchData')
        if st!=None:
            houseData=House.objects.filter(House_title__icontains=st)
    data={
        'houseData':houseData
    }
    

    # return httpresponse('welcome my wbsite')
    return render(request,'house.html',data)
def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        pnumber=request.POST.get('pnumber')
        message=request.POST.get('message')
        contact=ContactForm(ContactForm_name=name,ContactForm_email=email,ContactForm_pnumber=pnumber,ContactForm_message=message)
        subject=name
        message=message
        email_form = settings.EMAIL_HOST_USER
        
        
        send_mail(subject,message,email_form,['pitambar0072@gmail.com'])
        contact.save()
        messages.success(request,'Thanks for contact-US')
        return redirect('showp')
        
    
        
    

    # return httpresponse('welcome my wbsite')
    return render(request,'contact.html')
def about(request):
    # return httpresponse('welcome my wbsite')
    return render(request,'about.html')

def service(request):
    data= service.objects.all()
    if request.method=='GET':
        st=request.GET.get('servicename')
        if st!= None:
            data= service.objects.filter(service_title=st)


    return render (request,'index.html')



def showp(request):
    all_data = ContactForm.objects.all()

    return render(request,'show.html',{'key1':all_data})
def editpage(request,pk):
    get_data = ContactForm.objects.get(id=pk)

    return render(request,'edit.html',{'key2':get_data})

def updatedata(request,pk):
    udata = ContactForm.objects.get(id=pk)
    udata.ContactForm_name=request.POST['name']
    udata.ContactForm_email=request.POST['email']
    udata.ContactForm_pnumber=request.POST['pnumber']
    udata.ContactForm_message=request.POST['message']
    udata.save()
    return redirect('showp')

def deletedata(request,pk):
    ddata=ContactForm.objects.get(id=pk)
    ddata.delete()
    return redirect('showp')


def newdetail(request,new_slug):
   
    newdetail=House.objects.get(House_slug=new_slug)
    datass={
        'newdetail':newdetail
    }
#     # blog =get_objects_or_404(House,pk= house_id)

   
    return render(request,'newdetail.html',datass)




# class ContactListFormView(generics.ListAPIView , generics.CreateAPIView):
#     queryset=ContactForm.objects.all()
#     serializer_class=ContactFormSerialzer


class ContactListFormView(generics.ListCreateAPIView):
    queryset=ContactForm.objects.all()
    serializer_class=ContactFormSerialzer

class ContactDetailFormView(generics.RetrieveUpdateDestroyAPIView):
    queryset=ContactForm.objects.all()
    serializer_class=ContactFormSerialzer




# class ContactDetailFormView(generics.RetrieveAPIView , generics.UpdateAPIView, generics.DestroyAPIView):
#     queryset=ContactForm.objects.all()
#     serializer_class=ContactFormSerialzer

def signup(request):
    if request.method=='POST':

        username = request.POST["username"]
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        user=User.objects.filter(username=username)
       
    
        if user:
            
            return HttpResponse('User is already register')
        
        elif User.objects.filter(email=email):

            return HttpResponse('email is already exist')
        
        else:
            
        

            if  password==password2:
                user=User.objects.create_user(username,email,password)
                user.first_name=fname
                user.last_name=lname
                user.save()
                return redirect('/')
            else:
                return messages.error('loggin error')
    return render(request,'signup.html')

def login(request):
    def myuser(request):
        username=request.POST['username']
        password=request.POST['password']
        User =authenticate(request, username=username,password=password)
        if User is not None:
            # messages.success('welcome')

            login(request,User)
            

        else:
            # messages.error('invalid login')
            return HttpResponse('error login')

    return render(request,'login.html')


def logout(request):
    if request.method=='POST':
        logout(request)
        
    return redirect('/')
    