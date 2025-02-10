import pytest
from rest_framework.test import APIClient
from django.urls import reverse

from mebel.models import Product, Category


@pytest.mark.django_db
class TestProduct:
    @pytest.fixture
    def client(self):
        return APIClient()

    @pytest.fixture
    def db(self):
        category = Category.objects.create(name='test1')
        Category.objects.create(name='test2')
        Product.objects.create(name='test1', price=100000, description='wertyu', weight=15.2, height=200, width=200,
                               category=category)
        Product.objects.create(name='test2', price=100000, description='wertyu', weight=15.2, height=200, width=200,
                               category=category)
        Product.objects.create(name='test4', price=100000, description='wertyu', weight=15.2, height=200, width=200,
                               category=category)

    def test_product(self, client, db):
        url = reverse('product-list')
        response = client.get(url)

        assert response.status_code == 200
        # -----------------------------------

        url = "http://127.0.0.1:8001/api/v1/furniture/2/"

        response = client.get(url)

        assert response.status_code == 200
        assert response.data.get('name') == 'test2'
        assert response.data.get('id') == 2
        # -----------------------------------

        url = reverse('product-create')
        data = {
  "name": "string",
  "price": 4654,
  "description": "string",
  "weight": "546",
  "height": 543,
  "width": 3,
  "category": 1
}

        response = client.post(url, data)

        assert response.status_code <= 210
        # -----------------------------------

        url = 'http://127.0.0.1:8001/api/v1/furniture/delete/1/'

        response = client.post(url)

        assert response.status_code <= 210
        # -----------------------------------

        url = 'http://127.0.0.1:8001/api/v1/furniture/update/2/'
        data = {
            "name": "updated_name"
        }

        response = client.patch(url, data)

        assert response.status_code <= 210


    def test_category(self, client, db):
        url = reverse('category-list')

        response = client.get(url)

        assert response.status_code == 200
        assert len(response.data) == 2
