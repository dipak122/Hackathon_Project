from django.shortcuts import render
from . models import registeringo,logtable,proregisteringo
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from random import randint

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
    if request.method == 'POST':
        service= request.POST['service']
        brand= request.POST['brand']

        return render(request, 'login.html',{'service':service,'brand':brand})

    return render(request,'login.html')

def verify_login(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['psw']
        service = request.POST['service']
        brand = request.POST['brand']

        param = registeringo.objects.all()

        for i in param:
            if username == i.username:
                if password == i.password:
                    return render(request,'last.html',{'address':i.address,'name':i.name,'brand':brand,'service':service})

                else:
                    print("password is incorrect ")
                    return render(request,'login.html')


    return render(request,'index.html')




def register(request):
    return render(request,"register.html")

def register_submission(request):
    if request.method == 'POST':
        m=registeringo.objects.all()
        k=[]
        e=[]
        for i in m:
            k.append(i.username)
        for i in m:
            e.append(i.email)

        model=request.POST['model']
        name=request.POST['name']
        Username=request.POST['Username']
        Address=request.POST['Address']
        email=request.POST['email']
        psw=request.POST['psw']
        psw_repeat=request.POST["psw_repeat"]
        print(name)
        if psw == psw_repeat and Username not in k:
            Registerinfo=registeringo(name=name, username=Username,address=Address,email=email,password=psw)
            Registerinfo.save()
            print(Address)
            return render(request,'last.html',{'address':Address,'name':name,'model':model})
        elif psw != psw_repeat:
            print("password not match")
            return render(request, 'register.html', {'name':name, 'username': Username,'address': Address,'email': email} )

        elif Username in k:
            print("username already exist ")
            return render(request, 'register.html',{'name':name,'address': Address,'email': email} )

        elif email in e:
            print("username already exist ")
            return render(request, 'register.html',{'name':name,'address': Address,'username': Username} )
    return render(request, "register.html")







    #
    #     f=1
    #     if username in k :
    #         par = '''<script language="javascript">
    #                 alert('Already registered please Sign in or use different name');
    #                 </script>'''
    #         print("Username already exit")
    #         m = 'user already exist'
    #         return render(request, "register.html", {'m': par})
    #     else:
    #
    #         Registerinfo = registeringo(username=username,password=password)
    #         m='successfully registered'
    #         Registerinfo.save()
    #     return render(request, "register.html", {'m': m})
    # return render(request, "register.html")

def mobile(request):
    return render(request,"mobile.html")

def log(request):
    sr=logtable.objects.all()
    sr=list(sr)
    sr=sr[::-1]
    return render(request,"log.html",{'sr':sr})

def mail(request):
    print("mail done")
    return render(request,'mail.html')

def mob(request):
    print("mail done")
    return render(request,'mob.html')

def last(request):
    print("mail done")
    return render(request,'last.html')

def register_d(request):
    if request.method == 'POST':
        brand=request.POST['dropdown']
        service=request.POST['mobile']
        print(service)
        return render(request, 'register.html',{'brand':brand,'service':service})

    #     if m.is_valid():
    #         k=m.cleaned_data['value']
    #         print(k)
    # print("mail done")



def last_submission(request):
    if request.method == 'POST':
        name = request.POST['name']
        brand = request.POST['brand']
        email = request.POST['email']
        address = request.POST['Address']
        desc = request.POST['Description']
        date = request.POST['Date']
        time = request.POST['appt']
        service = request.POST['service']



        otp=randint(1000, 9999)
        par = '''<script language="javascript">
                            alert('Your booking has been successfully done!!! and further details has been send to your email');
                            </script>'''
        print(otp)
        body='Your booking has been successfully done!!! and Your OTP is '+str(otp)
        email = EmailMessage('Smartcatcher', body, to=[email])
        email.send()



        k=logtable(otp=otp,name=name,brand=brand,service=service,email=email,address=address,des=desc,date=date,time=time)
        k.save()
        return render(request, 'index.html',{'par':par})

    else:
        return render(request, 'index.html')



def agents(request):
    #m=logtable.objects.all()


    sr=logtable.objects.filter(service="mobile").values('otp','name','brand','service','email','address','des','date','status','time')
    sr=sr[::-1]

    print(sr)
    return render(request,'agents.html',{'sr':sr})

def update(request):
    newotp = request.POST['newotp']
    otp = request.POST['otp']
    if otp==newotp:
        t = logtable.objects.get(otp=otp)
        t.status = 'Done'  # change field
        t.save()  # thi
        print("done")



    else:
        print("no update")
    return HttpResponseRedirect('/agents/')




def prologin(request):

    return render(request,'prologin.html')

def proverify_login(request):

    username = request.POST['uname']
    password = request.POST['psw']
    print(username)
    print(password)
    param = proregisteringo.objects.all()

    for i in param:
        print(i.username)
        print(i.password)
        if username == i.username:
            if password == i.password:
                print("i m inuser")
                t = proregisteringo.objects.get(username=username)
                service = t.service
                print(service)
                if service=='mobile':
                    return HttpResponseRedirect('/agents/')

            else:
                print("password is incorrect ")
                return render(request,'prologin.html')
            # else:
            #     print("user not exit")
            #     return render(request,'prologin.html')

    return render(request,'index.html')


def cancel(request):
    return render(request,'cancel.html')

def cancelsub(request):
    otp=request.POST['otp']
    m=logtable.objects.filter(otp=otp)
    if m:
        m.delete()
        par = '''<script language="javascript">
                                            alert('Your booking has been successfully cancelled');
                                            </script>'''
        return render(request,'index.html',{'par':par})

    else:
        par = '''<script language="javascript">
                                    alert('Please Enter correct OTP');
                                    </script>'''
        return render(request, 'cancel.html', {'par': par})


