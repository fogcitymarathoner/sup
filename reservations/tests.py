import datetime
from django.test import TestCase

from reservations import models


class ReservationTestCase(TestCase):

    def setUp(self):
        self.tables = []
        self.tables.append(models.Table.objects.create(tableName='One'))

    def tearDown(self):
        pass

    def test_is_available_in_range(self):
        print(models.Table.objects.all())
        print(models.Table.objects.all()[0])
        self.tables[0].reserve(datetime.datetime(2017, 1, 1, 17, 0, 0), datetime.datetime(2017, 1, 1, 18, 0, 0))
        self.assertFalse(
            self.tables[0].is_available_in_range(datetime.datetime(2017, 1, 1, 17, 0, 0),
                                                 datetime.datetime(2017, 1, 1, 18, 0, 0)))
        self.assertTrue(
            self.tables[0].is_available_in_range(datetime.datetime(2017, 1, 1, 18, 0, 1),
                                                 datetime.datetime(2017, 1, 1, 19, 0, 0)))
