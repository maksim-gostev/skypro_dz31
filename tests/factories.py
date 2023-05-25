import factory

from ads.models import Category, Ad
from users.models import User, Location


class LocationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Location

    name = "test"
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    role = 'member'
    age = 20
    username = "test"
    password = "test"


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = "test"


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad
    user = UserFactory
    name = "test"
    author = "test"
    price = 100
    is_published = False
    category = factory.SubFactory(CategoryFactory)

