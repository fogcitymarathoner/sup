from django.db import models


class Table(models.Model):

    tableName = models.CharField(max_length=30)

    def __str__(self):
        return "Table: %s %s" % (self.id, self.tableName)


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
