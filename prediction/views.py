from django.shortcuts import render
from django.http import JsonResponse

#Get realtime crypto data
def fetch_data(request):
    return JsonResponse({"message": "Will get real time data"})

#Create predictions
def predict(request):
    return JsonResponse({"message": "Will create predictions"})

#Get historical crypto data
def historical(request):
    return JsonResponse({"message": "Will get historical data"})

#Create analysis
def sentiment(request):
    return JsonResponse({"message": "Will create analysis"})

#Schedule tasks
def schedule_task(request):
    return JsonResponse({"message": "Will schedule tasks"})