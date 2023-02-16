from django.db import models


class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(default=1)
    booking_date = models.DateTimeField()

    def __str__(self):
        return f'{self.name}: {self.no_of_guests} @ {self.booking_date}'


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField(blank=True)

    def __str__(self):
        return f'{self.title} : {str(self.price)}'

    def get_item(self):
        return f'{self.title} : {str(self.price)}'