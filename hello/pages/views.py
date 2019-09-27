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
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('psw')

        param = registeringo.objects.all()

        for i in param:
            if username == i.username:
                if password == i.password:
                    return render(request,'last.html',{'address':i.address})

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
    if request.method == 'POST':
        m=registeringo.objects.all()
        k=[]
        e=[]
        for i in m:
            k.append(i.username)
        for i in m:
            e.append(i.email)

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
            return render(request,'last.html',{'address':Address})
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
        m=request.POST['dropdown']
        print(m)
    #     if m.is_valid():
    #         k=m.cleaned_data['value']
    #         print(k)
    # print("mail done")
    return render(request,'register.html')



