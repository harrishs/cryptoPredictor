from django.shortcuts import render
from django.http import JsonResponse
from .utils import fetch_crypto_price, fetch_historical_data

#Get realtime crypto data
def fetch_data(request):
    crypto_data = fetch_crypto_price(["bitcoin", "ethereum"])
    return JsonResponse(crypto_data)

#Create predictions
def predict(request):
    return JsonResponse({"message": "Will create predictions"})

#Get historical crypto data
def historical(request):
    crypto_id = request.GET.get('crypto', 'bitcoin')
    from_date = request.GET.get('from', '2024-01-01')
    to_date = request.GET.get('to', '2024-01-07')

    historical_data = fetch_historical_data(crypto_id, from_date, to_date)
    return JsonResponse(historical_data)

#Create analysis
def sentiment(request):
    return JsonResponse({"message": "Will create analysis"})

#Schedule tasks
def schedule_task(request):
    return JsonResponse({"message": "Will schedule tasks"})