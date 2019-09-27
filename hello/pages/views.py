from django.shortcuts import render
from . models import registeringo,logtable

#from . models import listdb
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q

def index(request):
    return render(request,'index.html')


def sidelist(request):
    return render(request,'sidelist.html')

def itemlist(request):
    return render(request,'itemlist.html')

def about(request):
    return render(request,'about.html')

def addbook(request):
    if request.method == 'POST':
        pass


    return render(request,'addbook.html')




def login(request):
    return render(request,'login.html')

def verify_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    param = registeringo.objects.all()

    for i in param:
        if username == i.username:
            if password == i.password:
                return render(request,'index.html')

            else:
                print("password is incorrect ")
                return render(request,'login.html')
        else:
            print("user not exit")
            return render(request,'login.html')



    return render(request,'index.html')




def register(request):
    return render(request,"register.html")

def register_submission(request):
    if request.method == "POST":
        m=registeringo.objects.all()
        k=[]
        for i in m:
            k.append(i.username)

        username=request.POST["Username"]
        password=request.POST["Password"]
        f=1
        if username in k :
            print("Username already exit")
            m = 'user already exist'
            return render(request, "register.html", {'m': m})
        else:

            Registerinfo = registeringo(username=username,password=password)
            m='successfully registered'
            Registerinfo.save()
        return render(request, "register.html", {'m': m})
    return render(request, "register.html")

def mobile(request):
    return render(request,"mobile.html")

def log(request):
    sr=logtable.objects.all()
    return render(request,"log.html",{'sr':sr})

def mail(request):
    print("mail done")
    return render(request,'mail.html')

def mob(request):
    print("mail done")
    return render(request,'mob.html')



