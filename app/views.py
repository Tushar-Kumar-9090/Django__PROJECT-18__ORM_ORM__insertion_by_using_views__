from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from app.models import *

def insert_topic(request):
    tn = input("Enter The Topic_name: ")
    TO = Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse("<center><h3>Topic Data Is Inserted</h3></center>")

def insert_webpage(request):
    tn = input("Enter The Topic_name: ")
    TO = Topic.objects.get_or_create(topic_name = tn)[0]
    TO.save()
    n = input("Enter The Name: ")
    u = input("Enter The Url: ")
    WO = Webpage.objects.get_or_create(topic_name=TO, name=n, url=u)[0]
    WO.save()
    return HttpResponse("<center><h3>Webpage Data Inserted</h3></center>")

def insert_access_records(request):
    tn = input("Enter The Topic_name: ")
    TO = Topic.objects.get_or_create(topic_name = tn)[0]
    TO.save()
    n = input("Enter The Name: ")
    u = input("Enter The Url: ")
    WO = Webpage.objects.get_or_create(topic_name=TO, name=n, url=u)[0]
    WO.save()
    d = input("Enter The Date: ")
    a = input("Enter The Author: ")
    ARO = AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
    ARO.save()
    return HttpResponse("<center><h3>AccessRecord Data Inserted</h3></center>")

