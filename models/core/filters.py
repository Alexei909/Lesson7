import django_filters as filters
from core import models

class PhoneFilter(filters.FilterSet):
    name = filters.CharFilter(label='Модель телефона', field_name='phone_name', lookup_expr='icontains')

    class Meta:
        model = models.Phone
        fields = ('phone_name', )

