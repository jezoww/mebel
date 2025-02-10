from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from mebel.models import Product, Image, Company, Category, CompanyImage, PhoneNumber


class ImageModelSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = 'image',


class ProductListModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = 'id', 'name', 'price',

    def to_representation(self, instance):
        data = super().to_representation(instance)
        images = []
        for image in ImageModelSerializer(instance=Image.objects.filter(product_id=data.get('id')), many=True).data:
            images.append(image.get('image'))
        data['images'] = images
        return data


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        images = []
        for image in CompanyImageModelSerializer(instance=Image.objects.filter(product_id=data.get('id')), many=True).data:
            images.append(image.get('image'))

        data['images'] = images
        data['weight'] = float(data['weight'])

        return data


class CompanyImageModelSerializer(ModelSerializer):
    class Meta:
        model = CompanyImage
        fields = 'image',


class PhoneNumberModelSerializer(ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = 'phone',

    def validate_phone(self, value):
        if len(value) != 7 or not value.isdigit():
            raise ValidationError('Invalid phone number!')



class CompanyModelSerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        images = []
        phones = []

        for image in CompanyImageModelSerializer(instance=CompanyImage.objects.all(), many=True).data:
            images.append(image.get('image'))

        for phone in PhoneNumberModelSerializer(instance=PhoneNumber.objects.all(), many=True).data:
            phones.append(phone.get('phone'))

        data['images'] = images
        data['phones'] = phones
        return data


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = 'id', 'name',
