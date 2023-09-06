from django.test import TestCase, Client
from apps.example.models import Name
from apps.example.tests.factories import NameFactory
from apps.example.schema import OutputNameSchema, InputNameSchema


class TestGetNames(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_existing_names(self):
        name = NameFactory.create()
        expected_result = OutputNameSchema.from_orm(name).dict()

        response = self.client.get('/api/example/names')
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)
        self.assertIn(expected_result, data)


class TestNewName(TestCase):
    def setUp(self):
        self.client = Client()

    def test_name_is_created(self):
        name = NameFactory.build()
        name_data = InputNameSchema.from_orm(name).dict()

        self.client.post(
            '/api/example/names/new',
            name_data,
            content_type='application/json'
        )

        self.assertTrue(Name.objects.filter(name=name.name).exists())

    def test_new_name_is_returned(self):
        name = NameFactory.build()
        name_data = InputNameSchema.from_orm(name).dict()
        expected_result = InputNameSchema.from_orm(name).dict()

        response = self.client.post(
            '/api/example/names/new',
            name_data,
            content_type='application/json'
        )

        print(response)
        data = response.json()
        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(data, dict)
        data.pop('id')
        self.assertEqual(expected_result, data)

    def test_returns_409_if_name_exists(self):
        name = NameFactory.create()
        name_data = InputNameSchema.from_orm(name).dict()

        response = self.client.post(
            '/api/example/names/new',
            name_data,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 409)


class TestDeleteName(TestCase):
    def setUp(self):
        self.client = Client()

    def test_name_is_deleted(self):
        name = NameFactory.create()
        self.assertTrue(Name.objects.filter(id=name.id).exists())

        self.client.delete(
            f'/api/example/names/delete?name_id={name.id}',
            content_type='application/json'
        )

        self.assertFalse(Name.objects.filter(id=name.id).exists())

    def test_returns_404_if_id_not_found(self):
        NameFactory.create()
        non_existing_id = Name.objects.latest('id').id + 1

        response = self.client.delete(
            f'/api/example/names/delete?name_id={non_existing_id}',
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 404)
