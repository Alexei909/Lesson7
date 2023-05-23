import factory
from faker import Factory

from core import models

factory_ru = Factory.create("ru-Ru")


class PhoneFactory(factory.django.DjangoModelFactory):
    name = factory_ru.phone_name()

    class Meta:
        model = models.Phone

        
