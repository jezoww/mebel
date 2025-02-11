from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db.models import *


class PhoneNumber(Model):
    phone = CharField(max_length=155)
    company = ForeignKey('mebel.Company', on_delete=CASCADE, related_name='phone_numbers')

    def __str__(self):
        return self.phone

    def clean(self):
        if len(self.phone) != 9 or not self.phone.isdigit():
            raise ValidationError("Phone number must be exactly 7 digits and contain only numbers.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)



class CompanyImage(Model):
    image = TextField()
    company = ForeignKey('mebel.Company', on_delete=CASCADE, related_name='images')


class Company(Model):
    instagram = CharField(max_length=255)
    telegram = CharField(max_length=255)
    youtube = CharField(max_length=255)
    telegram_bot = CharField(max_length=255)
    admin = CharField(max_length=128)
    company_address = CharField(max_length=255)
    lon = DecimalField(max_digits=11, decimal_places=8)
    lat = DecimalField(max_digits=11, decimal_places=8)
    website = CharField(max_length=255)


class Image(Model):
    image = TextField()
    product = ForeignKey('mebel.Product', on_delete=CASCADE, related_name='images')

    def __str__(self):
        return self.product.name

class Category(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(Model):
    name = CharField(max_length=255)
    price = IntegerField()
    description = TextField()
    weight = DecimalField(max_digits=7, decimal_places=1)
    height = IntegerField()
    width = IntegerField()
    category = ForeignKey('mebel.Category', on_delete=CASCADE, related_name='products')
    material = CharField(max_length=256)


    def __str__(self):
        return self.name



