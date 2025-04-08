from django.test import TestCase
from .models import Status, Type, Category, Subcategory
from .forms import DDSRecordForm
from django.urls import reverse
from django.test import Client

class HandbookViewTest(TestCase):
    def test_handbook_view_get(self):
        client = Client()
        response = client.get(reverse('handbook'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'handbook.html')


class DDSRecordFormTest(TestCase):
    def setUp(self):
        self.status = Status.objects.create(name="Активный")
        self.type = Type.objects.create(name="Доход")
        self.category = Category.objects.create(name="Зарплата", type=self.type)
        self.subcategory = Subcategory.objects.create(name="Основная", category=self.category)

    def test_valid_form(self):
        form_data = {
            'status': self.status.id,
            'type': self.type.id,
            'category': self.category.id,
            'subcategory': self.subcategory.id,
            'amount': 1000.00,
            'comment': 'Тестовая запись',
            'created_at': '2024-04-08',
        }
        form = DDSRecordForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = DDSRecordForm(data={})
        self.assertFalse(form.is_valid())


class HandbookModelsTest(TestCase):
    def test_create_status(self):
        status = Status.objects.create(name="Активный")
        self.assertEqual(str(status), "Активный")

    def test_create_type(self):
        type_obj = Type.objects.create(name="Доход")
        self.assertEqual(str(type_obj), "Доход")

    def test_create_category_and_subcategory(self):
        type_obj = Type.objects.create(name="Расход")
        category = Category.objects.create(name="Продукты", type=type_obj)
        subcategory = Subcategory.objects.create(name="Овощи", category=category)
        self.assertEqual(subcategory.category.name, "Продукты")
