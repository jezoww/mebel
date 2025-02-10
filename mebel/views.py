from datetime import timedelta

from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.timezone import now
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from mebel.models import Product, Category, Company
from mebel.serializers import ProductListModelSerializer, CategoryModelSerializer, CompanyModelSerializer, \
    ProductModelSerializer


@extend_schema(tags=['product'], parameters=[
    OpenApiParameter(
        name="category",
        description=(
                "..."
        ),
        type={
            "type": "integer",
        },
        explode=False,
        style="form",
        required=False
    ),
    OpenApiParameter(
        name="search",
        description=(
                "..."
        ),
        type={
            "type": "string",
        },
        explode=False,
        style="form",
        required=False
    )
])
class ProductListAPIView(ListAPIView):
    serializer_class = ProductListModelSerializer

    def get_queryset(self):
        category_id = self.request.GET.get('category', None)
        search = self.request.GET.get('search', None)

        products = Product.objects.all()
        if category_id:
            products = products.filter(category_id=category_id)

        if search:
            products = products.filter(
                Q(name__icontains=search) | Q(description__icontains=search) | Q(category__name__icontains=search))


        # Product.objects.create(name='test1', price=100000, description='wertyu', weight=15.2, height=200, width=200, category_id=1, material='test material')
        # Product.objects.create(name='test2', price=100000, description='wertyu', weight=15.2, height=200, width=200, category_id=1, material='test material')
        # Product.objects.create(name='test4', price=100000, description='wertyu', weight=15.2, height=200, width=200, category_id=1, material='test material')

        return products

@extend_schema(tags=['product'])
class ProductRetrieveAPIView(RetrieveAPIView):
    serializer_class = ProductModelSerializer
    queryset = Product.objects.all()
    lookup_field = 'pk'


@extend_schema(tags=['category'])
class CategoryListAPIView(ListAPIView):
    serializer_class = CategoryModelSerializer
    queryset = Category.objects.all()


@extend_schema(tags=['company'], responses=CompanyModelSerializer)
class CompanyAPIView(APIView):
    def get(self, request):
        company = Company.objects.first()
        if company:
            data = CompanyModelSerializer(instance=company).data
            return JsonResponse(data, status=HTTP_200_OK)
        data = {"message": "Company data not found!", "status": 400}
        return JsonResponse(data, status=HTTP_400_BAD_REQUEST)


@extend_schema(tags=['product'], request=ProductModelSerializer)
class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductModelSerializer
    queryset = Product.objects.all()

@extend_schema(tags=['product'], request=ProductModelSerializer)
class ProductUpdateAPIView(UpdateAPIView):
    lookup_field = 'pk'
    serializer_class = ProductModelSerializer
    queryset = Product.objects.all()

@extend_schema(tags=['product'])
class ProductDestroyAPIView(DestroyAPIView):
    lookup_field = 'pk'
    queryset = Product.objects.all()


@extend_schema(tags=['category'], request=CategoryModelSerializer)
class CategoryCreateAPIView(CreateAPIView):
    serializer_class = CategoryModelSerializer
    queryset = Category.objects.all()

@extend_schema(tags=['category'], request=CategoryModelSerializer)
class CategoryUpdateAPIView(UpdateAPIView):
    lookup_field = 'pk'
    serializer_class = CategoryModelSerializer
    queryset = Category.objects.all()

@extend_schema(tags=['category'])
class CategoryDestroyAPIView(DestroyAPIView):
    lookup_field = 'pk'
    queryset = Category.objects.all()

@extend_schema(tags=['company'], request=CompanyModelSerializer)
class CompanyCreateAPIView(CreateAPIView):
    serializer_class = CompanyModelSerializer
    queryset = Company.objects.all()

@extend_schema(tags=['company'], request=CompanyModelSerializer)
class CompanyUpdateAPIView(UpdateAPIView):
    lookup_field = 'pk'
    serializer_class = CompanyModelSerializer
    queryset = Company.objects.all()

@extend_schema(tags=['company'])
class CompanyDestroyAPIView(DestroyAPIView):
    lookup_field = 'pk'
    queryset = Company.objects.all()

