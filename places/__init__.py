from django.apps import apps as django_apps
from django.core.exceptions import ImproperlyConfigured

from places import settings as booking_settings


def get_place_model():
    try:
        return django_apps.get_model(booking_settings.BOOKING_PLACE_MODEL, require_ready=False)
    except ValueError:
        raise ImproperlyConfigured("BOOKING_PLACE_MODEL must be of the form 'app_label.model_name'")
    except LookupError:
        raise ImproperlyConfigured(
            "BOOKING_PLACE_MODEL refers to model '%s' that has not been installed" %
            booking_settings.BOOKING_PLACE_MODEL
        )


def get_room_model():
    try:
        return django_apps.get_model(booking_settings.BOOKING_ROOM_MODEL, require_ready=False)
    except ValueError:
        raise ImproperlyConfigured("BOOKING_ROOM_MODEL must be of the form 'app_label.model_name'")
    except LookupError:
        raise ImproperlyConfigured(
            "BOOKING_ROOM_MODEL refers to model '%s' that has not been installed" %
            booking_settings.BOOKING_ROOM_MODEL
        )
