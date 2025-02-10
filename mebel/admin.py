from django.contrib import admin
from django.contrib.admin import StackedInline, ModelAdmin
from django.core.exceptions import ValidationError

from mebel.models import Product, Company, Category, Image, CompanyImage, PhoneNumber

admin.site.register(Category)


class ProductImageInline(StackedInline):
    model = Image
    extra = 3


@admin.register(Product)
class ProductModelAdmin(ModelAdmin):
    inlines = [ProductImageInline]


class CompanyImageInline(StackedInline):
    model = CompanyImage
    extra = 3



class PhoneInline(StackedInline):
    model = PhoneNumber
    extra = 2


@admin.register(Company)
class CompanyModelAdmin(ModelAdmin):
    inlines = [CompanyImageInline, PhoneInline]


