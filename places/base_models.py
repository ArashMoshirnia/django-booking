from django.conf import settings
from django.db import models

from places import settings as booking_settings


class AbstractPlaceModel(models.Model):
    name = models.CharField(max_length=100)
    star_rating = models.PositiveSmallIntegerField(null=True)
    description = models.TextField(blank=True)
    type = models.ForeignKey('places.PlaceType', related_name='%(app_label)s_%(class)s', on_delete=models.PROTECT)
    address = models.OneToOneField('places.Address', on_delete=models.PROTECT)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class AbstractRoomModel(models.Model):
    place = models.ForeignKey(booking_settings.BOOKING_PLACE_MODEL, related_name='%(app_label)s_%(class)s',
                              on_delete=models.CASCADE)
    capacity = models.PositiveSmallIntegerField()
    existing_count = models.PositiveSmallIntegerField()
    description = models.TextField(blank=True)
    type = models.ForeignKey('places.RoomType', related_name='%(app_label)s_%(class)s', on_delete=models.PROTECT)
    price = models.ForeignKey('places.Price', null=True, on_delete=models.SET_NULL)

    class Meta:
        abstract = True

    def __str__(self):
        return '{} - {}'.format(self.place, self.type)


class AbstractBookingModel(models.Model):
    room = models.ForeignKey(booking_settings.BOOKING_ROOM_MODEL, related_name='%(app_label)s_%(class)s',
                             on_delete=models.PROTECT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(app_label)s_%(class)s',
                             on_delete=models.PROTECT)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    adult_count = models.PositiveSmallIntegerField(default=0)
    children_count = models.PositiveSmallIntegerField(default=0)
    total_cost = models.ForeignKey('places.Price', on_delete=models.PROTECT)

    def __str__(self):
        return '{} - {} - {}'.format(self.user, self.room, self.check_in_date)

    class Meta:
        abstract = True
