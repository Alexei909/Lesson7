from django.db import models


class Company(models.Model):
    name_company = models.CharField(max_length=255)

    def __str__(self):
        return self.name_company


class Shop(models.Model):
    name_shop = models.CharField(max_length=255)

    def __str__(self):
        return self.name_shop


class Phone(models.Model):
    phone_name = models.CharField(max_length=255, verbose_name='Модель телефона')
    name_oc = models.CharField(max_length=255, verbose_name='Название ОС')
    volume_memory = models.IntegerField(blank=True, null=True)
    on_sale = models.BooleanField(default=True, verbose_name='В продаже')
    date_of_issue = models.DateField(blank=True, null=True, verbose_name='Дата выпуска')
    dc = models.DateTimeField(auto_now_add=True)
    du = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='phone', null=True, blank=True, verbose_name='Компания')
    shop = models.ManyToManyField(Shop, blank=True, verbose_name='В магазинах')

    def __str__(self):
        return self.phone_name

class Owner(models.Model):
    name_owner = models.CharField(max_length=255)
    phone = models.OneToOneField(Phone, on_delete=models.CASCADE, related_name='owner')

    def __str__(self):
        return self.name_owner