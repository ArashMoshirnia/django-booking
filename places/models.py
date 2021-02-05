from django.db import models

from places import settings as booking_settings
from places.base_models import AbstractPlaceModel, AbstractRoomModel, AbstractBookingModel
from places.utils import get_place_images_upload_location


class PlaceType(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, related_name='cities', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Address(models.Model):
    city = models.ForeignKey(City, related_name='addresses', on_delete=models.CASCADE)
    street = models.TextField()
    number = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return '{} - {}'.format(self.street, self.number)


class Place(AbstractPlaceModel):
    pass


class PlaceImage(models.Model):
    place = models.ForeignKey(booking_settings.BOOKING_PLACE_MODEL, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=get_place_images_upload_location)


class RoomType(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Currency(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return '{} ({})'.format(self.name, self.code)


class Price(models.Model):
    value = models.FloatField(default=0.0)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(str(self.value), self.currency.code)


class Room(AbstractRoomModel):
    pass


class Booking(AbstractBookingModel):
    pass
