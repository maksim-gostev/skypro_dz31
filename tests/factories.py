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
    username = factory.Sequence(lambda n: 'user{0}'.format(n))
    password = "test"


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = "test"


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad
    name = "test"
    author = factory.SubFactory(UserFactory)
    price = 100
    is_published = False
    category = factory.SubFactory(CategoryFactory)

