from rest_framework import serializers
from ads.models import Ad, Category
from users.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator


def validate_is_published(value):
    if value:
        raise ValidationError('При создании не может быть True')


class AdSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')
    category = serializers.SlugRelatedField(read_only=True,
                                            slug_field='name')

    location = serializers.SlugRelatedField(read_only=True,
                                            many=True,
                                            slug_field='name')

    class Meta:
        model = Ad
        fields = '__all__'


class AdCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    category = serializers.SlugRelatedField(required=False,
                                            queryset=Category.objects.all(),
                                            slug_field='name')
    author = serializers.SlugRelatedField(queryset=User.objects.all(),
                                          slug_field='username')
    is_published = serializers.BooleanField(validators=[validate_is_published])
    price = serializers.IntegerField(validators=[MinValueValidator(0)])

    class Meta:
        model = Ad
        exclude = ['image']


class AdUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    category = serializers.SlugRelatedField(required=False,
                                            queryset=Category.objects.all(),
                                            slug_field='name')
    author = serializers.SlugRelatedField(queryset=User.objects.all(),
                                          slug_field='username')

    class Meta:
        model = Ad
        exclude = ['image']
