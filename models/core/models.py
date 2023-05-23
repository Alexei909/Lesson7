from django.db import models
from django.urls import reverse


class Company(models.Model):
    name_company = models.CharField(max_length=255)

    def __str__(self):
        return self.name_company
    
    class Meta:
        verbose_name = 'Компанию'
        verbose_name_plural = 'Компании'
        ordering = ('id', )


class Shop(models.Model):
    name_shop = models.CharField(max_length=255)

    def __str__(self):
        return self.name_shop


class Phone(models.Model):
    phone_name = models.CharField(blank=True, max_length=255, verbose_name='Модель телефона')
    name_oc = models.CharField(blank=True, max_length=255, verbose_name='Название ОС')
    volume_memory = models.IntegerField(blank=True, null=True, verbose_name='Объём памяти')
    on_sale = models.BooleanField(default=True, verbose_name='В продаже')
    date_of_issue = models.DateField(blank=True, null=True, verbose_name='Дата выпуска')
    dc = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    du = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='phone', null=True, blank=True, verbose_name='Компания')
    shop = models.ManyToManyField(Shop, blank=True, verbose_name='В магазинах')

    def __str__(self):
        return self.phone_name
    
    def get_absolute_url(self):
        return f'/phone/{self.pk}/'
    
    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'
        ordering = ('dc', 'phone_name', )
    

class Owner(models.Model):
    name_owner = models.CharField(max_length=255)
    phone = models.OneToOneField(Phone, on_delete=models.CASCADE, related_name='owner')

    def __str__(self):
        return self.name_owner