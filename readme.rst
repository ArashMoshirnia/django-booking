=====
Django Booking
=====

Booking is package allowing users to create a website like booking.com without having to start from the scratch.
Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "places" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'places',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('places/', include('places.urls')),

3. Run ``python manage.py migrate`` to create the places models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

