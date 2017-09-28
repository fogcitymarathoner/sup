import datetime
from django.test import TestCase

from reservations import models
from reservations import lib


class ReservationTestCase(TestCase):
    def setUp(self):
        self.tables = []
        self.tables.append(models.Table.objects.create(tableName='One'))
        self.tables.append(models.Table.objects.create(tableName='Two'))
        self.tables.append(models.Table.objects.create(tableName='Three'))
        self.tables.append(models.Table.objects.create(tableName='Four'))

    def tearDown(self):
        pass

    def test_is_available_in_range(self):
        self.tables[0].reserve('tuser', datetime.datetime(2017, 1, 1, 17, 0, 0),
                               datetime.datetime(2017, 1, 1, 18, 0, 0))
        self.assertFalse(
            self.tables[0].is_available_in_range(datetime.datetime(2017, 1, 1, 17, 0, 0),
                                                 datetime.datetime(2017, 1, 1, 18, 0, 0)))
        self.assertTrue(
            self.tables[0].is_available_in_range(datetime.datetime(2017, 1, 1, 18, 0, 1),
                                                 datetime.datetime(2017, 1, 1, 19, 0, 0)))

    def test_none_reservation_return_if_fully_booked(self):

        self.tables[0].reserve('tuser', datetime.datetime(2017, 1, 1, 17, 0, 0),
                               datetime.datetime(2017, 1, 1, 18, 0, 0))
        self.tables[1].reserve('tuser', datetime.datetime(2017, 1, 1, 17, 0, 0),
                               datetime.datetime(2017, 1, 1, 18, 0, 0))
        self.tables[2].reserve('tuser', datetime.datetime(2017, 1, 1, 17, 0, 0),
                               datetime.datetime(2017, 1, 1, 18, 0, 0))
        self.tables[3].reserve('tuser', datetime.datetime(2017, 1, 1, 17, 0, 0),
                               datetime.datetime(2017, 1, 1, 18, 0, 0))

        self.assertEquals(None, lib.assign_reservation_to_party('tuser', datetime.datetime(2017, 1, 1, 17, 0, 0),
                                                                datetime.datetime(2017, 1, 1, 18, 0, 0)))

    def test_reservation_assignment(self):


        self.tables[1].reserve('tuser', datetime.datetime(2017, 1, 1, 17, 0, 0),
                               datetime.datetime(2017, 1, 1, 18, 0, 0))
        self.tables[2].reserve('tuser', datetime.datetime(2017, 1, 1, 17, 0, 0),
                               datetime.datetime(2017, 1, 1, 18, 0, 0))
        self.tables[3].reserve('tuser', datetime.datetime(2017, 1, 1, 17, 0, 0),
                               datetime.datetime(2017, 1, 1, 18, 0, 0))

        reservation = lib.assign_reservation_to_party('tuser', datetime.datetime(2017, 1, 1, 17, 0, 0),
                                                                datetime.datetime(2017, 1, 1, 18, 0, 0))
        self.assertTrue(reservation is not None)
        self.assertEqual(self.tables[0], reservation.table)
