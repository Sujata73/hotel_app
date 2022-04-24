from django.db import models

# Create your models here.
class test_data(models.Model):
    name = models.TextField()


class Payments(models.Model):
    paymentid = models.IntegerField(primary_key=True)
    bookingid = models.ForeignKey('Roombookings', models.DO_NOTHING, db_column='bookingid')
    paymenttype = models.CharField(max_length=255)
    paymentamount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payments'

    def __str__(self):
        return str(self.bookingid)




class Roombookings(models.Model):
    bookingid = models.IntegerField(primary_key=True)
    customername = models.CharField(max_length=500, blank=True, null=True)
    customeraddress = models.CharField(max_length=550, blank=True, null=True)
    bookingfrom = models.DateField(blank=True, null=True)
    bookingto = models.DateField(blank=True, null=True)
    assignroomid = models.ForeignKey('Rooms', models.DO_NOTHING, db_column='assignroomid', blank=True, null=True)
    noofguests = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roombookings'

    def __str__(self):
        return str(self.customername)


class Rooms(models.Model):
    roomid = models.IntegerField(primary_key=True)
    roomnumber = models.IntegerField()
    roomprice = models.IntegerField()
    roomtype = models.CharField(max_length=255)
    roomcapacity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rooms'

    def __str__(self):
        return str(self.roomnumber)

