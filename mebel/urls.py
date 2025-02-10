from django.urls import path

from mebel.views import ProductListAPIView, ProductRetrieveAPIView, CategoryListAPIView, CompanyAPIView, \
    ProductDestroyAPIView, ProductCreateAPIView, ProductUpdateAPIView, CategoryDestroyAPIView, CategoryCreateAPIView, \
    CategoryUpdateAPIView, CompanyDestroyAPIView, CompanyCreateAPIView, CompanyUpdateAPIView

urlpatterns = [
    path('furniture/', ProductListAPIView.as_view(), name='product-list'),
    path('furniture/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product-detail'),
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('company/', CompanyAPIView.as_view(), name='company'),
    path('furniture/delete/<int:pk>/', ProductDestroyAPIView.as_view(), name='product-delete'),
    path('furniture/create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('furniture/update/<int:pk>', ProductUpdateAPIView.as_view(), name='product-update'),
    path('category/delete/<int:pk>/', CategoryDestroyAPIView.as_view(), name='category-delete'),
    path('category/create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('category/update/<int:pk>', CategoryUpdateAPIView.as_view(), name='category-update'),
    path('company/delete/<int:pk>/', CompanyDestroyAPIView.as_view(), name='category-delete'),
    path('company/create/', CompanyCreateAPIView.as_view(), name='company-create'),
    path('company/update/<int:pk>', CompanyUpdateAPIView.as_view(), name='company-update'),
]
