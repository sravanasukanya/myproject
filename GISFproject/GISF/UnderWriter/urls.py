from django.urls import path
from .views import InsuredcreateView, PolicyCreateView, PolicyUpdateView, PolicyBillsview

app_name = 'UnderWriter'

urlpatterns = [
    path('CreateInsured/', InsuredcreateView, name='CreateInsured'),
    path('PolicyCreate/', PolicyCreateView, name='PolicyCreate'),
    path('PolicyUpdate/', PolicyUpdateView, name='PolicyUpdate'),
    path('PolicyBillPay/', PolicyBillsview, name='PolicyBillPay'),
]