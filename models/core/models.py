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
    phone_name = models.CharField(max_length=255)
    name_oc = models.CharField(max_length=255)
    volume_memory = models.IntegerField(blank=True, null=True)
    on_sale = models.BooleanField(default=True)
    date_of_issue = models.DateField(blank=True, null=True)
    dc = models.DateTimeField(auto_now_add=True)
    du = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='phone', null=True, blank=True)
    shop = models.ManyToManyField(Shop, blank=True)

    def __str__(self):
        return self.phone_name

class Owner(models.Model):
    name_owner = models.CharField(max_length=255)
    phone = models.OneToOneField(Phone, on_delete=models.CASCADE, related_name='owner')

    def __str__(self):
        return self.name_owner