from django.conf import settings


DEFAULTS = {
    'BOOKING_PLACE_MODEL': 'places.Place',
    'BOOKING_ROOM_MODEL': 'places.Room',
    'BOOKING_BOOKING_MODEL': 'places.Booking'
}

BOOKING_PLACE_MODEL = 'places.Place'
BOOKING_ROOM_MODEL = 'places.Room'
BOOKING_BOOKING_MODEL = 'places.Booking'

if hasattr(settings, 'BOOKING_SETTINGS'):
    booking_settings = getattr(settings, 'BOOKING_SETTINGS')
    if not isinstance(booking_settings, dict):
        raise ValueError('BOOKING_SETTINGS should be a dictionary')
    BOOKING_PLACE_MODEL = booking_settings.get('BOOKING_PLACE_MODEL', DEFAULTS.get('BOOKING_PLACE_MODEL'))
    BOOKING_ROOM_MODEL = booking_settings.get('BOOKING_ROOM_MODEL', DEFAULTS.get('BOOKING_ROOM_MODEL'))
    BOOKING_BOOKING_MODEL = booking_settings.get('BOOKING_BOOKING_MODEL', DEFAULTS.get('BOOKING_BOOKING_MODEL'))
