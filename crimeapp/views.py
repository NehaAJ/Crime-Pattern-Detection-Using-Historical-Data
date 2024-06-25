import datetime

from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth import logout
from django.http import HttpResponse
from .models import *
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required,user_passes_test
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
# Create your views here.

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import random
days=random.randint(40,45)
test_list = ["Chittoor","Anantapur","Guntur"]
 
# printing original list

 
# using random.choice() to
# get a random number
nextpl = random.choice(test_list)
# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    form=officialForm()
    form2=officeForm()
    mydict={'form':form,'form2':form2}
    if request.method=='POST':
        form=officialForm(request.POST) 
        form2=officeForm(request.POST)
        if form.is_valid() and form2.is_valid():
            print(1)
            user=form.save()
            user.set_password(user.password)
            user.save()
            messages.success(request,f'You have successfully registered!')
            official=form2.save(commit=True)
            official.user=user
            official.save()
            group=Group.objects.get_or_create(name="Common")
            group[0].user_set.add(user)
            return redirect('login')

    return render(request,'register.html',context=mydict)


def is_common(user):
    return user.groups.filter(name="Common").exists()

def afterlogin_view(request):
    if is_common(request.user):
        return redirect('home')
    elif is_ip(request.user):
        return redirect('homeip')
    elif is_sp(request.user):
        return redirect('homesp')
    elif is_dgp(request.user):
        return redirect('homedgp')
     

@login_required(login_url='login')
@user_passes_test(is_common)
def home(request):
    a=official.objects.get(user_id=request.user.id)
    return render(request,'home.html',{'a':a})







def logout_request(request):
    logout(request)
    return redirect('index')
    

def prof(request):
    var=official.objects.get(user_id=request.user.id)
    form=officialForm()
    form2=officeForm()
    if request.method=="POST":
        var=official.objects.get(user_id=request.user)
        form=officialForm(request.POST,instance=var.user)
        print(form)
        form2=officeForm(request.POST,instance=var)
        print(form2)
        if form.is_valid() and form2.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            print(user)
            messages.success(request,'Profile Updated Successfully')
            form2.save()
            return redirect('home')
    else:
        form=officialForm(instance=var.user)
        form2=officeForm(instance=var)
    context={
                  'form':form,
                  'form2':form2,
        }
    return render(request,'profile.html',context)









#IP registration

def registerip(request):
    form=officialFormIP()
    form2=officeFormIP()
    mydict={'form':form,'form2':form2}
    if request.method=='POST':
        form=officialFormIP(request.POST) 
        form2=officeFormIP(request.POST)
        if form.is_valid() and form2.is_valid():
            print(1)
            user=form.save()
            user.set_password(user.password)
            user.save()
            messages.success(request,f'You have successfully registered!')
            officialip=form2.save(commit=True)
            officialip.user=user
            officialip.save()
            group=Group.objects.get_or_create(name="ip")
            group[0].user_set.add(user)
            return redirect('login')

    return render(request,'registerip.html',context=mydict)


def is_ip(user):
    return user.groups.filter(name="ip").exists()


    

@login_required(login_url='login')
@user_passes_test(is_ip)

def homeip(request):
    a=officialip.objects.get(user_id=request.user.id)
    return render(request,'homeip.html',{'a':a})


    
@login_required(login_url='login')
@user_passes_test(is_ip)
def prof1(request):
    var=officialip.objects.get(user_id=request.user.id)
    form1=officialForm()
    form2=officeForm()
    if request.method=="POST":
        var=officialip.objects.get(user_id=request.user.id)
        form=officialFormIP(request.POST,instance=var.user)
        print(form)
        form2=officeFormIP(request.POST,instance=var)
        print(form2)
        if form.is_valid() and form2.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            print(user)
            messages.success(request,'Profile Updated Successfully')
            form2.save()
            return redirect('homeip')
    else:
        form=officialFormIP(instance=var.user)
        form2=officeFormIP(instance=var)
        context={
                  'form':form,
                  'form2':form2,
        }
    return render(request,'profileip.html',context)


#SP registration form

def registersp(request):
    form=officialFormSP()
    form2=officeFormSP()
    mydict={'form':form,'form2':form2}
    if request.method=='POST':
        form=officialFormSP(request.POST) 
        form2=officeFormSP(request.POST)
        if form.is_valid() and form2.is_valid():
            print(1)
            user=form.save()
            user.set_password(user.password)
            user.save()
            messages.success(request,f'You have successfully registered!')
            officialsp=form2.save(commit=True)
            officialsp.user=user
            officialsp.save()
            group=Group.objects.get_or_create(name="sp")
            group[0].user_set.add(user)
            return redirect('login')

    return render(request,'registersp.html',context=mydict)


def is_sp(user):
    return user.groups.filter(name="sp").exists()


    

@login_required(login_url='login')
@user_passes_test(is_sp)
def homesp(request):
    a=officialsp.objects.get(user_id=request.user.id)
    return render(request,'homesp.html',{'a':a})


    
@login_required(login_url='login')
@user_passes_test(is_sp)
def prof2(request):
    var=officialsp.objects.get(user_id=request.user.id)
    # form1=officialForm()
    # form2=officeForm()
    if request.method=="POST":
        var=officialsp.objects.get(user_id=request.user.id)
        form=officialFormSP(request.POST,instance=var.user)
        print(form)
        form2=officeFormSP(request.POST,instance=var)
        print(form2)
        if form.is_valid() and form2.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            print(user)
            messages.success(request,'Profile Updated Successfully')
            form2.save()
            return redirect('homesp')
    else:
        form=officialFormSP(instance=var.user)
        form2=officeFormSP(instance=var)
        context={
                  'form':form,
                  'form2':form2,
        }
    return render(request,'profilesp.html',context)



#DGP registration form

def registerdgp(request):
    form=officialFormDGP()
    form2=officeFormDGP()
    mydict={'form':form,'form2':form2}
    if request.method=='POST':
        form=officialFormDGP(request.POST) 
        form2=officeFormDGP(request.POST)
        if form.is_valid() and form2.is_valid():
            print(1)
            user=form.save()
            user.set_password(user.password)
            user.save()
            messages.success(request,f'You have successfully registered!')
            officialdgp=form2.save(commit=True)
            officialdgp.user=user
            officialdgp.save()
            group=Group.objects.get_or_create(name="dgp")
            group[0].user_set.add(user)
            return redirect('login')

    return render(request,'registerdgp.html',context=mydict)


def is_dgp(user):
    return user.groups.filter(name="dgp").exists()


    

@login_required(login_url='login')
@user_passes_test(is_dgp)
def homedgp(request):
    a=officialdgp.objects.get(user_id=request.user.id)
    return render(request,'homedgp.html',{'a':a})


    
@login_required(login_url='login')
@user_passes_test(is_dgp)
def prof3(request):
    var=officialdgp.objects.get(user_id=request.user.id)
    # form1=officialForm()
    # form2=officeForm()
    if request.method=="POST":
        var=officialdgp.objects.get(user_id=request.user.id)
        form=officialFormDGP(request.POST,instance=var.user)
        print(form)
        form2=officeFormDGP(request.POST,instance=var)
        print(form2)
        if form.is_valid() and form2.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            print(user)
            messages.success(request,'Profile Updated Successfully')
            form2.save()
            return redirect('homedgp')
    else:
        form=officialFormDGP(instance=var.user)
        form2=officeFormDGP(instance=var)
        context={
                  'form':form,
                  'form2':form2,
        }
    return render(request,'profiledgp.html',context)


def Fir(request):
    return render(request, "fir.html")

def Fir1(request):
    return render(request, "firip.html")

def Fir2(request):
    return render(request, "firsp.html")

def Fir3(request):
    return render(request, "firdgp.html")

def TourProgram(request):
    return render(request, "tourprogram.html")

def Gallery(request):
    return render(request, "gallery.html")

def WeeklyDiary(request):
    return render(request, "weeklydiary.html")


def firform(request):
    if request.method == 'POST':
        form = FirForm1(request.POST)
        if form.is_valid():
                    fir_data = form.cleaned_data
                    fir_data['user'] = request.user  # Assuming you have authentication set up
                    fir = Firmod(**fir_data)
                    fir.save()
                    return render(request, 'firform.html',{"msg":"Successfully saved"})

        else:
                return redirect('homedgp')
    return render(request,'firform.html')
#
#
# def fir_form(request):
#     if request.method == 'POST':
#         form = FirForm1(request.POST)
#         if form.is_valid():
#             fir_data = form.cleaned_data
#             fir_data['user'] = request.user  # Assuming you have authentication set up
#             fir = Firmod(**fir_data)
#             fir.save()
#             return redirect('success')  # Redirect to success page after saving the data
#     else:
#         form = FirForm1()


def MedicalRecords_view(request):
    md=medicalrecords.objects.all()
    mydict={
        "data":md
    }

    return render(request, "medrec.html",context=mydict)

def AssignDuties(request):
    ad=assignduties.objects.all()
    return render(request, "asdut.html")

def successration(request):
    md=medicalrecords.objects.values('hospital').distinct()
    hospitalData ={}
    hsCalc=[]
    hsname=[]
    for hos in md:
        print(hos['hospital'])
        mrCount=medicalrecords.objects.filter(hospital=hos['hospital']).count()
        mrSuccCount=medicalrecords.objects.filter(hospital=hos['hospital'],recovery="Yes").count()        
        hospitalData.update({hos['hospital']:((mrSuccCount/mrCount)*100)})

    print(hospitalData)
    dict={
        "hsdict":hospitalData
    }
    return render(request, "medsuccess.html",context=dict)



def PastRecords(request):
    if request.method == 'POST' and request.FILES['pdf_file']:
        pdf_file = request.FILES['pdf_file']
        fs = FileSystemStorage()
        filename = fs.save(pdf_file.name, pdf_file)
        pdf_url = fs.url(filename)
        return render(request, 'pastrec.html', {'pdf_url': pdf_url})
    return render(request, 'pastrec.html')


def view_fir(request):
    print(request.user)
    fir = Firmod.objects.filter(user=request.user)
    print(fir)
    return render(request, 'view_fir.html', {'fir': fir})


def userMap(request):
    # Get latitude and longitude coordinates from a database or other source
    directions=Location.objects.all()
    coordinates = []

    for i in directions:
        for j in range(len(directions)):
            lat = float(i.lang)
            lng = float(i.long)
            coordinates.append({'lat': lat, 'lng': lng})
    context = {
        'coordinates': coordinates,
    }

    return render(request, 'userMap.html',context)

from django.contrib.auth.models import Group, User

from django.shortcuts import render

def user_list(request):
    if request.method == 'POST':
        Duty.objects.create(user_id=request.POST.get('user_id'),duty = request.POST.get('duty'),name=request.user.first_name)
        return redirect('homedgp')


    else:
        users = User.objects.all()
        return render(request, 'user_list.html', {'users': users})


from django.shortcuts import render
from django.db.models import Count
from .models import Task


def weekly_calendar(request):
    entries = Task.objects.filter(user=request.user)

    context = {
        'entries': entries
    }
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        characters = request.POST.get('characters')

        # Save the data to the database
        entry = Task.objects.create(user=request.user,start_date=start_date, end_date=end_date, characters=characters)

        # Fetch all entries to display on the page
        entries = Task.objects.filter(user=request.user)

        context = {
            'entries': entries
        }
        return render(request, 'weekly_calender.html', context)

    return render(request, 'weekly_calender.html',context)

def add_diary(request):
    if request.method == 'POST':
        Diary.objects.create(user=request.user,
                                   diary=request.POST.get('diary'))
        entries = Diary.objects.filter(user=request.user)

        context = {
            'entries': entries
        }
        return render(request, 'diary.html', context)
    else:
        entries = Diary.objects.filter(user=request.user)

        context = {
            'entries': entries
        }
        return render(request, 'diary.html', context)




def tour_planner(request):
    if request.method == 'POST':
        TourPlanner.objects.create(user=request.user,start_date=request.POST.get('date'),activities=request.POST.get('activities'))
        entries = TourPlanner.objects.filter(user=request.user)

        context = {
            'entries': entries
        }
        return render(request, 'tour_planner.html', context)
    else:
        entries = TourPlanner.objects.filter(user=request.user)

        context = {
            'entries': entries
        }
        return render(request, 'tour_planner.html', context)


def grievence(request):
    if request.method == 'POST':
        Grievence.objects.create(user_id=request.POST.get('user_id'),grievence = request.POST.get('duty'),sender=request.user.first_name)
        return render(request, 'grievence_list.html', {'msg': "success"})
    else:
        users = User.objects.filter(groups__name__in=['dgp','sp'])
        return render(request, 'grievence_list.html', {'users': users})

def view_grievence(request):
    grievences=Grievence.objects.filter(user=request.user)
    context = {
        'entries': grievences
    }
    return render(request, 'view_grievence.html', context)


def Visitors(request):
    if request.method == 'POST':
        Visitor.objects.create(user=request.user,start_date=request.POST.get('date'),characters=request.POST.get('activities'),end_date=request.POST.get('time'))

        entries = Visitor.objects.filter(user=request.user)

        context = {
            'entries': entries
        }
        return render(request, 'visitor.html', context)
    else:
        entries = Visitor.objects.filter(user=request.user)

        context = {
            'entries': entries
        }
        return render(request, 'visitor.html',context)

def Firview(request):
    grievences = Firmod.objects.filter(user=request.user)
    context = {
        'fir': grievences
    }
    return render(request, 'view_fir.html', context)

def Dutyview(request):
    duty = Duty.objects.filter(user=request.user)
    print(duty)
    context = {
        'duty': duty
    }
    return render(request, 'view_duty.html', context)


import pandas as pd
import numpy as np


def Crime_prediction(request):
    if request.method == 'POST':

        data = pd.read_csv("crime_data.csv")
        # print(data.head())
        place = request.POST.get('place')
        murder_in_selected_location = data.loc[data['District'] == place, 'Murder'].sum()
        print(murder_in_selected_location)
        custodial_rape_in_selected_location = data.loc[data['District'] == place, 'Custodial Rape'].sum()
        rape_in_selected_location = data.loc[data['District'] == place, 'Rape_Others'].sum()
        rape_total = custodial_rape_in_selected_location + rape_in_selected_location
        acid_attack_in_selected_location = data.loc[data['District'] == place, 'Acid attack'].sum()
        print(acid_attack_in_selected_location)
        dowry_death_in_selected_location = data.loc[data['District'] == place, 'Dowry Deaths'].sum()
        print(dowry_death_in_selected_location)

        rash_driving = data.loc[data['District'] == place, 'Incidence of Rash Driving'].sum()
        print(rash_driving)

        kidnapping = data.loc[data['District'] == place, 'Kidnapping for Ransom'].sum()
        print(kidnapping)
        crimes_in_front_of_public = data.loc[data['District'] == place, 'In Public Transport system'].sum()
        print(crimes_in_front_of_public)

        Sexual_Harassment = data.loc[data['District'] == place, 'Sexual Harassment'].sum()
        print(Sexual_Harassment)

        Theft_cases = data.loc[data['District'] == place, 'Theft'].sum()
        print(Theft_cases)
        fake_currency_cheating = data.loc[data['District'] == place, 'Counterfeit currency & Bank notes'].sum()
        print(fake_currency_cheating)
        other_ipc_crimes = data.loc[data['District'] == place, 'Other IPC crimes'].sum()
        print(other_ipc_crimes)
        total_crimes = murder_in_selected_location + custodial_rape_in_selected_location + rape_total + acid_attack_in_selected_location + dowry_death_in_selected_location + rash_driving + kidnapping + crimes_in_front_of_public + Sexual_Harassment + Theft_cases + fake_currency_cheating + other_ipc_crimes
        print("total no of crimes in a month")
        print(total_crimes)
        average = total_crimes / 10
        print("Average no of crimes in a month")
        print(average)
        c=''
        if (average > 300):
            c="The place is not safe to visit"
        elif (average > 200 and average < 300):
            c="The place is safer to visit, but you must be careful"
        else:
            c="The place is safe to Visit"
        context = {
            'a': total_crimes,
            'b':average,
            'c':c
        }
        df=data.loc[data['District'] == place, 'Theft'].sum()
        theft_int=int(df)
        X=data[['Murder','Rape','Rape_Others']]
        Y=data[['Total Cognizable IPC crimes']]
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.25)
        inc=random.randint(1, 10)
            # Fit an ARIMA model to the data
        model = ARIMA(data['Year'], order=(1, 1, 1)) # Specify the order of the ARIMA model
        results = model.fit()

# Make a prediction for the next inc time periods
        forecast = results.forecast(steps=inc)
        r=forecast*inc
        print('forecast is',r)
        print('type is',type(r))
        r = r.astype(int)
        r=list(r)
        r=r[0]
        print('rrrrr',r)
        



        years=1
        post=Post()
        post.place=place
        post.murder=murder_in_selected_location
        post.rape=rape_total
        post.theft=Theft_cases
        post.others=other_ipc_crimes
        post.total=total_crimes
        post.average=average
        post.future=r
        post.nextplace=nextpl
        post.ndays=days
        post.save()
        print(post.__dict__)
                
        return render(request, 'prediction.html',{"post":post})

    else:
        return render(request,'prediction.html')
    return render(request, 'prediction.html')




def Crime_prediction2(request):
    if request.method == 'POST':

        data = pd.read_csv("crime_data.csv")
        print(data.head())
        place = request.POST.get('place')
        murder_in_selected_location = data.loc[data['District'] == place, 'Murder'].sum()
        print(murder_in_selected_location)
        custodial_rape_in_selected_location = data.loc[data['District'] == place, 'Custodial Rape'].sum()
        rape_in_selected_location = data.loc[data['District'] == place, 'Rape_Others'].sum()
        rape_total = custodial_rape_in_selected_location + rape_in_selected_location
        acid_attack_in_selected_location = data.loc[data['District'] == place, 'Acid attack'].sum()
        print(acid_attack_in_selected_location)
        dowry_death_in_selected_location = data.loc[data['District'] == place, 'Dowry Deaths'].sum()
        print(dowry_death_in_selected_location)

        rash_driving = data.loc[data['District'] == place, 'Incidence of Rash Driving'].sum()
        print(rash_driving)

        kidnapping = data.loc[data['District'] == place, 'Kidnapping for Ransom'].sum()
        print(kidnapping)
        crimes_in_front_of_public = data.loc[data['District'] == place, 'In Public Transport system'].sum()
        print(crimes_in_front_of_public)

        Sexual_Harassment = data.loc[data['District'] == place, 'Sexual Harassment'].sum()
        print(Sexual_Harassment)

        Theft_cases = data.loc[data['District'] == place, 'Theft'].sum()
        print(Theft_cases)
        fake_currency_cheating = data.loc[data['District'] == place, 'Counterfeit currency & Bank notes'].sum()
        print(fake_currency_cheating)
        other_ipc_crimes = data.loc[data['District'] == place, 'Other IPC crimes'].sum()
        print(other_ipc_crimes)
        total_crimes = murder_in_selected_location + custodial_rape_in_selected_location + rape_total + acid_attack_in_selected_location + dowry_death_in_selected_location + rash_driving + kidnapping + crimes_in_front_of_public + Sexual_Harassment + Theft_cases + fake_currency_cheating + other_ipc_crimes
        print("total no of crimes in a month")
        print(total_crimes)
        average = total_crimes / 100
        print("Average no of crimes in a month")
        print(average)
        c=''
        if (average > 300):
            c="The place is not safe to visit"
        elif (average > 200 and average < 300):
            c="The place is safer to visit, but you must be careful"
        else:
            c="The place is safe to Visit"
        context = {
            'a': total_crimes,
            'b':average,
            'c':c
        }
        return render(request, 'prediction2.html',{"a":total_crimes,"b":average,"c":c})

    else:
        return render(request,'prediction2.html')
    return render(request, 'prediction2.html')

def achievement_upload(request):
    if request.method == 'POST':
        # Handle the uploaded achievement image
        image = request.FILES.get('achievement-image')
        text = request.FILES.get('text')
        Achievement.objects.create(user=request.user,image=image)

    achievements = Achievement.objects.filter(user=request.user)
    return render(request, 'achievemnets.html', {'achievements': achievements})



def iframe_view(request):
    return render(request, 'iframe.html')