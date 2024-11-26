from celery import shared_task
from .utils import fetch_santiment_data

@shared_task
def update_santiment_data(crypto_id, from_date, to_date, metric="social_volume_total"):
    data = fetch_santiment_data(crypto_id, from_date, to_date, metric)
    print(f"Fetched data for {crypto_id}: {data}")
    return data