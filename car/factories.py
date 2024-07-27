import random
from faker import Faker
from factory.django import DjangoModelFactory
import factory

from .models import Car, Brand

faker = Faker()

class CarFactory(DjangoModelFactory):
    class Meta:
        model = Car
    title = factory.Faker("sentence", nb_words=1, variable_nb_words=True)
    description = factory.Faker('paragraph', nb_sentences=10, variable_nb_sentences=False)
    maker = factory.Faker("sentence", nb_words=1, variable_nb_words=True)
    price = factory.LazyFunction(lambda: random.randint(100, 100000))

        
class BrandFactory(DjangoModelFactory):
    class Meta:
        model = Brand

    title = factory.Faker("sentence", nb_words=1, variable_nb_words=True)
    description = factory.Faker('paragraph', nb_sentences=10, variable_nb_sentences=False)