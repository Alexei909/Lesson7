from bs4 import BeautifulSoup
from django.test import TestCase, Client
from django.urls import reverse

from core import factories, models


class PhoneTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_list(self):
        phone = factories.PhoneFactory()
        resp = self.client.get(reverse("core:phone_list"))
        self.assertEqual(resp.status_code, 200)
        bs = BeautifulSoup(resp.content, "html.parser")
        self.assertListEqual(bs.tbody.tr.text.split(), ['1', phone.name, "Обновить", "Удалить"])

    def test_create(self):
        phone = factories.PhoneFactory.build()
        resp = self.client.post(reverse("core:phone_create"), {"name": phone.name}, follow=True)
        self.assertEqual(resp.status_code, 200)
        phone_db = models.Phone.objects.first()
        self.assertEqual(phone_db.name, phone.name)

    def test_update(self):
        phone = factories.PhoneFactory()
        phone_name = "Иван123"
        resp = self.client.post(reverse("core:phone_update", args=(phone.pk,)), {"name": phone_name}, follow=True)
        self.assertEqual(resp.status_code, 200)
        phone_db = models.Phone.objects.first()
        self.assertEqual(phone_db.name, phone_name)

    def test_delete(self):
        phone = factories.PhoneFactory()
        resp = self.client.post(reverse("core:'phone_del'", args=(phone.pk,)), follow=True)
        self.assertEqual(resp.status_code, 200)
        phone_db = models.Phone.objects.first()
        self.assertEqual(phone_db, None)