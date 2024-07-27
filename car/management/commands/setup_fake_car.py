from django.core.management import BaseCommand
from django.db import transaction, connection

from datetime import datetime, timedelta
from faker import Faker
import subprocess

from car.models import Car, Brand
from car.factories import BrandFactory, CarFactory

list_of_model = [Car, Brand]

faker1 = Faker()

NUM_BRAND = 10
NUM_CAR = 200


class Command(BaseCommand):
    help = 'Generate of car & brand data'

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write('Delete data ..')
        for m in list_of_model:
            m.objects.all().delete()
        self.stdout.write('Create data ...')

        print(f'Create brand {NUM_BRAND} data ...', end='')
        for _ in range(NUM_BRAND):
            brand = BrandFactory()
            brand.datetime_created = faker1.date_time_ad(start_datetime=datetime(2015, 1, 1),
                                                                                     end_datetime=datetime(2023, 1, 1))
            brand.datatime_modified = brand.datetime_created + timedelta(hours=1000)
        print('DONE')

        print(f'Create car {NUM_CAR} data ...', end='')
        for _ in range(NUM_CAR):
            brand = CarFactory()
            brand.datetime_created = faker1.date_time_ad(start_datetime=datetime(2015, 1, 1),
                                                                                     end_datetime=datetime(2023, 1, 1))
            brand.datatime_modified = brand.datetime_created + timedelta(hours=1000)
        print('DONE')





