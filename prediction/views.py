from django.shortcuts import render
from django.http import JsonResponse
from .utils import fetch_crypto_price, fetch_historical_data, fetch_santiment_data
from django.http import JsonResponse
from .models import SantimentData
from django.utils import timezone
from datetime import datetime

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
    crypto_id = request.GET.get('crypto', 'bitcoin')
    from_date = request.GET.get('from', '2024-01-01')
    to_date = request.GET.get('to', '2024-01-07')
    metric = request.GET.get('metric', 'social_volume_total')

    sentiment_data = fetch_santiment_data(crypto_id, from_date, to_date, metric)
    return JsonResponse(sentiment_data)

#Get Stored Analysis Data
def stored_sentiment(request):
    crypto_id = request.GET.get('crypto', 'bitcoin')
    metric = request.GET.get('metric', 'social_volume_total')
    from_date = request.GET.get('from', '2024-01-01')
    to_date = request.GET.get('to', '2024-01-07')

    #Convert times to timezone-aware datetime
    from_datetime = timezone.make_aware(datetime.strptime(from_date, "%Y-%m-%d"))
    to_datetime = timezone.make_aware(datetime.strptime(to_date, "%Y-%m-%d"))

    data = SantimentData.objects.filter(
        cryptocurrency__crypto_id=crypto_id,
        metric = metric,
        datetime__range=[from_datetime, to_datetime]
    ).values("datetime", "value")

    return JsonResponse(list(data), safe=False)

#Schedule tasks
def schedule_task(request):
    return JsonResponse({"message": "Will schedule tasks"})