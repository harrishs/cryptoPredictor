from django.shortcuts import render
from django.http import JsonResponse
from .utils import fetch_crypto_price

#Get realtime crypto data
def fetch_data(request):
    crypto_data = fetch_crypto_price(["bitcoin", "ethereum"])
    return JsonResponse(crypto_data)

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