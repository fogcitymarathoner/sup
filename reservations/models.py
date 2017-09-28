from django.db import models


class Table(models.Model):

    tableName = models.CharField(max_length=30)

    def __str__(self):
        return "Table: %s %s" % (self.id, self.tableName)

    def reserve(self, start, end):
        self.startTime = start
        self.endTime = end
        reservation, _ = Reservation.objects.get_or_create(table=self, startTime=start, endTime=end)

        return reservation

    def is_available_in_range(self, start, end):

        reservations = Reservation.objects.filter(startTime__gte=start).filter(endTime__lte=end)
        if len(reservations) == 0:
            return True
        else:
            return False


class Reservation(models.Model):

    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    reservingPerson = models.CharField(max_length=30)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()

    def __str__(self):
        return "Reservation: %s %s %s %s - %s" % (
            self.id,
            self.table,
            self.reservingPerson,
            self.startTime,
            self.endTime
        )