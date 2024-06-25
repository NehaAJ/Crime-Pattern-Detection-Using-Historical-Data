from django.contrib.auth.models import User
from django import forms
from .models import *

class officialForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password']
        widgets={
            'password':forms.PasswordInput()
        }

class officeForm(forms.ModelForm):
    class Meta:
        model=official
        fields=['mob','address','post']

#  IP registration page

class officialFormIP(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password']
        widgets={
            'password':forms.PasswordInput()
        }

class officeFormIP(forms.ModelForm):
    class Meta:
        model=officialip
        fields=['mob','address','post']

#SP registration page

class officialFormSP(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password']
        widgets={
            'password':forms.PasswordInput()
        }

class officeFormSP(forms.ModelForm):
    class Meta:
        model=officialsp
        fields=['mob','address','post']


 #DGP registration page

class officialFormDGP(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password']
        widgets={
            'password':forms.PasswordInput()
        }

class officeFormDGP(forms.ModelForm):
    class Meta:
        model=officialdgp
        fields=['mob','address','post']


class FirForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password']
        widgets={
            'password':forms.PasswordInput()
        }



class FirForm1(forms.ModelForm):
    class Meta:
        model=Firmod
        fields=['fname','age','occupation','residence','casedes','date','time','location','typeofcrime']



class TourPlannerForm(forms.ModelForm):
    class Meta:
        model=TourPlanner
        fields ='__all__'