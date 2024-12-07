from .models import Cryptocurrency, SantimentData
from celery import shared_task
from .utils import fetch_santiment_data

@shared_task
def update_santiment_data(crypto_id, from_date, to_date, metric="social_volume_total"):
    data = fetch_santiment_data(crypto_id, from_date, to_date, metric)
    
    #Get or create crypto record
    crypto, _ = Cryptocurrency.objects.get_or_create(crypto_id=crypto_id, defaults={"name": crypto_id.capitalize()})

    #Save santiment data
    for entry in data:
        SantimentData.objects.update_or_create(
            cryptocurrency = crypto,
            metric = metric,
            datetime = entry["datetime"],
            defaults = {"value": entry["value"]}
        )

    return f"Updated {len(data)} records for {crypto_id}"