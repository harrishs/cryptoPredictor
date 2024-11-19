from django.urls import path
from . import views

urlpatterns = [
    path('fetch_data/', views.fetch_data, name='fetch_data'),
    path('predict/', views.predict, name='predict'),
    path('historical/', views.historical, name='historical'),
    path('sentiment/', views.sentiment, name='sentiment'),
    path('schedule/', views.schedule_task, name='schedule')
]