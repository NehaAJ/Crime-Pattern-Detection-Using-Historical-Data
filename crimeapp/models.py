from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class official(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    mob=models.CharField(max_length=20,null=True)
    address=models.CharField(max_length=200,null=True)
    post=models.CharField(max_length=200,null=True)
    
class officialip(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    mob=models.CharField(max_length=20,null=True)
    address=models.CharField(max_length=200,null=True)
    post=models.CharField(max_length=200,null=True)

class officialsp(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    mob=models.CharField(max_length=20,null=True)
    address=models.CharField(max_length=200,null=True)
    post=models.CharField(max_length=200,null=True)


class officialdgp(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    mob=models.CharField(max_length=20,null=True)
    address=models.CharField(max_length=200,null=True)
    post=models.CharField(max_length=200,null=True)

class Firmod(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    fname=models.CharField(max_length=20,null=True)
    age=models.CharField(max_length=200,null=True)
    occupation=models.CharField(max_length=200,null=True)
    residence=models.CharField(max_length=200,null=True)
    casedes=models.CharField(max_length=200,null=True)
    date=models.CharField(max_length=200,null=True)
    time=models.CharField(max_length=200,null=True)
    location=models.CharField(max_length=200,null=True)
    typeofcrime=models.CharField(max_length=200,null=True)

class medicalrecords(models.Model):
    user=models.CharField(max_length=200,null=True)
    hospital=models.CharField(max_length=200,null=True)
    mob=models.CharField(max_length=20,null=True)
    address=models.CharField(max_length=200,null=True)
    date=models.CharField(max_length=20,null=True)
    injury=models.CharField(max_length=200,null=True)
    recovery=models.CharField(max_length=200,null=True)

class assignduties(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    post=models.CharField(max_length=200,null=True)
    duty=models.CharField(max_length=20,null=True)
    date=models.CharField(max_length=20,null=True)


class Location(models.Model):
    lang = models.FloatField()
    long = models.FloatField()
    address = models.TextField()

class Duty(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    duty=models.CharField(max_length=200,null=True)
    name=models.CharField(max_length=200,null=True)



class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    characters = models.CharField(max_length=200)


class Diary(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    diary = models.CharField(max_length=200)



class TourPlanner(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    start_date = models.DateField()
    activities = models.CharField(max_length=200)

class Visitor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    start_date = models.DateField()
    end_date = models.CharField(max_length=200)
    characters = models.CharField(max_length=200)


class Grievence(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    grievence=models.CharField(max_length=200,null=True)
    sender = models.CharField(max_length=200)


class Achievement(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    image = models.ImageField(upload_to='achievements/')
    upload_date = models.DateTimeField(auto_now_add=True)
    text= models.CharField(max_length=200)
class Location(models.Model):
    lang = models.FloatField()
    long = models.FloatField()
    address = models.TextField()

class Post(models.Model):
    place= models.CharField(max_length=300, unique=False)
    murder= models.CharField(max_length=300, unique=False)
    rape= models.CharField(max_length=300, unique=False)
    theft= models.CharField(max_length=300, unique=False)
    others= models.CharField(max_length=300, unique=False)
    total= models.CharField(max_length=300, unique=False)

    average= models.CharField(max_length=300, unique=False)
    future= models.CharField(max_length=300, unique=False)
    nextplace= models.CharField(max_length=300, unique=False)
    ndays= models.CharField(max_length=300, unique=False)

