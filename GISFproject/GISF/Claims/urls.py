from django.urls import path

from .views import CalimsRaiseView

app_name = 'Claim1'

urlpatterns = [
    path('RaiseClaim/', CalimsRaiseView, name='RaiseClaim')
]