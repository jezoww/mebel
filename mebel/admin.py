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

    def save_model(self, request, obj, form, change):
        phone = obj.phone

        if len(phone) != 7 or not phone.isdigit():
            raise ValidationError("Phone number must be 7 digits.")

        super().save_model(request, obj, form, change)
