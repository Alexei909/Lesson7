from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.index),
    path('phone_list/',  views.PhoneList.as_view(), name='phone_list'),
    path('phone/<int:pk>/', views.phone_detail, name='phone'),
    path('phone_create/', views.PhoneCreate.as_view(), name='phone_create'),
    path('phone_update/<int:pk>', views.PhoneUpdate.as_view(), name='phone_update'),
    path('phone_del/<int:pk>', views.PhoneDelete.as_view(), name='phone_del')
]


