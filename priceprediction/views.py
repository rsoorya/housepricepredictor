from django.shortcuts import render
from django.http import HttpResponse
import json
from . import test
from .models import Predictions

global __data_columns
global __locations

with open('model/columns.json','r') as f:
    __data_columns = json.load(f)['data_columns']
    __locations = __data_columns[3:]

def home(request):
    if request.method == "POST":
            location=request.POST['location']
            bhk=request.POST['bhk']
            bath=request.POST['bath']
            sqft=request.POST['sqft']
            price=test.get_estimated_price(location,sqft,bhk,bath)
            ins = Predictions(locations=location,sqft=sqft,bhk=bhk,bath=bath,predicted_price=price)
            ins.save()
            return render(request,'prediction.html',context={'location':location,'bhk':bhk,'sqft':sqft,'bath':bath,'price':price})
            
    else:
            return render(request,'predict.html',context={'locations':__locations})

def predictions(request):
    predictions = Predictions.objects.all().order_by('-id')
    return render(request,'predictions.html',context={'predictions':predictions})

