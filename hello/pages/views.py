from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext

from .models import registeringo, logtable, proregisteringo, feedadd
from django.core.mail import EmailMessage
from django.contrib import messages
from django.http import HttpResponseRedirect
from random import randint

# from . models import listdb
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q


def index(request):
    return render(request, 'index.html')


def sidelist(request):
    return render(request, 'sidelist.html')


def itemlist(request):
    return render(request, 'itemlist.html')


def about(request):
    return render(request, 'about.html')


def addbook(request):
    if request.method == 'POST':
        pass

    return render(request, 'addbook.html')


def login(request):
    if request.method == 'POST':
        service = request.POST['service']
        brand = request.POST['brand']

        return render(request, 'login.html', {'service': service, 'brand': brand})
    else:
        par = '''<script language="javascript">
                    alert('Some thing Gone a wrong reEnter Username and Password  ');
                                                </script>'''

        return render(request, 'index.html', {'par': par})
    # return render(request,'login.html')


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
                    return render(request, 'index.html', {'uname': username})
                    # return render(request, 'index.html',
                    # {'address': i.address, 'name': i.name, 'brand': brand, 'service': service})

                else:
                    print("password is incorrect ")
                    return render(request, 'login.html')

    else:

        par = '''<script language="javascript">
                           alert('Some thing Gone a wrong reEnter Username and Password  ');
                                                       </script>'''

        return render(request, 'index.html', {'par': par})
    # return render(request,'index.html')


def register(request):
    return render(request, "register.html")


def register_submission(request):
    if request.method == 'POST':
        m = registeringo.objects.all()
        k = []
        e = []
        for i in m:
            k.append(i.username)
        for i in m:
            e.append(i.email)

        model = request.POST['model']
        name = request.POST['name']
        Username = request.POST['Username']
        Address = request.POST['Address']
        email = request.POST['email']
        psw = request.POST['psw']
        psw_repeat = request.POST["psw_repeat"]
        print(name)
        if psw == psw_repeat and Username not in k:
            Registerinfo = registeringo(name=name, username=Username, address=Address, email=email, password=psw)
            Registerinfo.save()
            print(Address)
            return render(request, 'last.html', {'address': Address, 'name': name, 'model': model})
        elif psw != psw_repeat:
            print("password not match")
            return render(request, 'register.html',
                          {'name': name, 'username': Username, 'address': Address, 'email': email})

        elif Username in k:
            print("username already exist ")
            return render(request, 'register.html', {'name': name, 'address': Address, 'email': email})

        elif email in e:
            print("username already exist ")
            return render(request, 'register.html', {'name': name, 'address': Address, 'username': Username})

    else:
        par = '''<script language="javascript">
                                   alert('Some thing Gone a wrong!!!  ');
                                                               </script>'''

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
    return render(request, "mobile.html")


def log(request):
    sr = logtable.objects.all()
    sr = list(sr)
    sr = sr[::-1]
    return render(request, "log.html", {'sr': sr})


def mail(request):
    print("mail done")
    return render(request, 'mail.html')


def mob(request):
    print("mail done")
    return render(request, 'mob.html')


def last(request):
    print("mail done")
    return render(request, 'last.html')


def register_d(request):
    if request.method == 'POST':
        brand = request.POST['dropdown']
        service = request.POST['mobile']
        print(service)
        return render(request, 'register.html', {'brand': brand, 'service': service})
    else:
        par = '''<script language="javascript">
                                    alert('First Book a service!!! At below');
                                    </script>'''

        return render(request, 'index.html', {'par': par})

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
        service = request.POST['service']
        servicep = request.POST['dropdown']
        time = request.POST['dropdownt']

        otp = randint(1000, 9999)
        par = '''Your booking has been successfully done!!! and further details has been send to your email'''
        print(otp)
        n = 'on  ' + str(date)
        w = 'will provide you service at ' + str(time) + ' '
        body = 'Your booking has been successfully done !!! and Your OTP is this ' + str(otp) + '  ' + str(
            servicep) + ' ' + w + n
        try:
            email = EmailMessage('Smartcatcher', body, to=[email])
            email.send()
            k = proregisteringo.objects.get(name=servicep)
            l = k.email
            print(l)
            p = 'you have an appointment at ' + str(date) + ' and on time ' + str(time)
            email = EmailMessage(p, p, to=[l])
            email.send()

            k = logtable(otp=otp, name=name, brand=brand, service=service, servicep=servicep, email=email,
                         address=address, des=desc, date=date, time=time)
            k.save()
            messages.success(request, par)
            messages.add_message(request, messages.SUCCESS, par)
            return redirect('/')
            # return render(request,HttpResponseRedirect('/'),{'par':par})
        # return render(request, 'index.html', {'par': par})
        except:

            par = '''<script language="javascript">
        alert('Your Request is submitted but Email is not able to send something gone a wrong ');
                                                        </script>'''

            return render(request, 'index.html', {'par': par})
    else:
        par = '''<script language="javascript">
                                alert('SomeThing Gone a wrong ReEnter details');
                                </script>'''

        return render(request, 'index.html', {'par': par})


def agents(request):
    # m=logtable.objects.all()

    sr = logtable.objects.filter(service="mobile").values('otp', 'name', 'brand', 'service', 'servicep', 'address',
                                                          'des', 'date', 'status', 'time')
    sr = sr[::-1]

    print(sr)
    return render(request, 'agents.html', {'sr': sr})


def update(request):
    newotp = request.POST['newotp']
    otp = request.POST['otp']
    if otp == newotp:
        t = logtable.objects.get(otp=otp)
        t.status = 'Done'  # change field
        t.save()  # thi
        print("done")



    else:
        print("no update")
    return HttpResponseRedirect('/agents/')


def prologin(request):
    return render(request, 'prologin.html')


def proverify_login(request):
    if request.method == 'POST':

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
                    print("i m in user")
                    t = proregisteringo.objects.get(username=username)
                    service = t.service
                    print(service)
                    if service == 'mobile':
                        return HttpResponseRedirect('/agents/')

                else:
                    print("password is incorrect ")
                    return render(request, 'prologin.html')
            # else:
            #     print("user not exit")
            #     return render(request,'prologin.html')
    else:
        par = '''<script language="javascript">
                alert('Invalid Input ReTry Again!!!! ');
                    </script>'''
        return render(request, 'index.html', {'par': par})


def cancel(request):
    return render(request, 'cancel.html')


def cancelsub(request):
    if request.method == 'POST':

        otp = request.POST['otp']
        m = logtable.objects.filter(otp=otp)
        if m:
            m.delete()
            par = '''<script language="javascript">
                                            alert('Your booking has been successfully cancelled');
                                            </script>'''
            return render(request, 'index.html', {'par': par})

        else:
            par = '''<script language="javascript">
                                    alert('Please Enter correct OTP');
                                    </script>'''
            return render(request, 'cancel.html', {'par': par})
    else:
        par = '''<script language="javascript">
                                            alert('Some invalid input start pls do it Again....');
                                            </script>'''
        return render(request, 'cancel.html', {'par': par})


def ac(request):
    return render(request, 'ac.html')


def paint(request):
    return render(request, 'paint.html')


def lap(request):
    return render(request, 'lap.html')


def cctv(request):
    return render(request, 'cctv.html')


def salon(request):
    return render(request, 'salon.html')


def pest(request):
    return render(request, 'pest.html')


def acc(request):
    return render(request, 'acc.html')


def elec(request):
    return render(request, 'elec.html')


def loginh(request):
    return render(request, 'loginh.html')


def verify_loginh(request):
    if request.method == 'POST':
        name = request.POST['uname']
        password = request.POST['psw']

        param = registeringo.objects.all()

        for i in param:
            if name == i.name:
                print("in if")
                if password == i.password:
                    print("in pass")
                    sr = logtable.objects.filter(name=name)
                    print(sr)
                    return render(request, 'history.html', {'sr': sr})

                else:
                    print("password is incorrect ")
                    return render(request, 'loginh.html')

        return render(request, 'index.html')
    else:
        par = '''<script language="javascript">
                            alert('Some invalid Input ReEnter username and password');
                                                </script>'''

        return render(request, 'index.html', {'par': par})


def feedback(request):
    if request.method == 'POST':
        servicep = request.POST['servicep']
        feed = request.POST['feed']
        k = feedadd(servicep=servicep, feed=feed)
        k.save()

        par = '''<script language="javascript">
                alert('Feedback has successfully saved');
                </script>'''

        return render(request, 'index.html', {'par': par})
    else:
        par = '''<script language="javascript">
                        alert('Something gone a wrong ');
                        </script>'''

        return render(request, 'index.html', {'par': par})


def page_not_found(request, exception):
    response = render_to_response('error_404.html')
    response.status_code = 404
    return response


def page_not_found500(request):
    response = render_to_response('error_500.html')
    response.status_code = 500
    return response
