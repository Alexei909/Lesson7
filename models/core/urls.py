from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.index),
    path('phone_list/',  views.PhoneList.as_view(), name='phone_list'),
    path('phone/<int:pk>', views.phone_detail, name='phone_detail')
]