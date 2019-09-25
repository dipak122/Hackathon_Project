from django.shortcuts import render
from . models import listdb
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q

def list(request):
    print("hello")

    if request.method=='POST':
        sr= request.POST['txt']
        print(sr)

        if sr:
            match = listdb.objects.filter(Q(name__icontains=sr)| Q(city__icontains=sr))
            if match:
                return render(request,'list.html',{'sr':match})
            else:
                messages.error(request,'no result found')
        else:
            return HttpResponseRedirect('/list/')

    return render(request,'list.html')


