from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from travel_app.models import Employee,BookTrip
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect,Http404
from django.shortcuts import reverse
import datetime


def index(request):
    employee=Employee.objects.all()
    my_context ={'title':'Travel App','emp':employee}
    return render(request,'travel_app/index.html',context=my_context)


def signUp(request):
    if request.method=='POST':
        username = request.POST['username']
        password=request.POST['password']
        name= request.POST['name']
        carmod=request.POST['carmod']
        carnum=request.POST['carnum']
        contact=request.POST['phno']
        location=request.POST['loc']
        employee =Employee(username=username,password=password,name=name,carmodel=carmod,carnum=carnum,contactnum=contact,location=location)
        employee.save()
        return HttpResponseRedirect(reverse('travel_app:index'))
    return render(request,'travel_app/signup.html',context=None)



def bookTravel(request):
    if request.method=='POST':
        d = request.POST['cars']
        driver=Employee.objects.get(id=d)
        name=request.POST['p_name']
        time=request.POST['time']
        pp=request.POST['pp']
        dest=request.POST['dest']
        phone=request.POST['phoneno']
        booking=BookTrip(driver=driver,p_name=name,pickup_time=time,p_pickup=pp,p_destination=dest,p_phone=phone)
        booking.save()

    return index(request)

def summery(request):
        sum = BookTrip.objects.all()
        t_context={'sum':sum}
        return render(request,'travel_app/summery.html',context=t_context)


def apiDisp(request):
    return render(request,'travel_app/api.html',context=None)


def emplist(request):
    emp=Employee.objects.all()
    return render(request,'travel_app/emplist.html',context={'emp':emp})
