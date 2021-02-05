from django.urls import path

from places.api.views import place_list_create, place_retrieve_update_destroy, room_list_create, \
    room_retrieve_update_destroy


urlpatterns = [
    path('places/', place_list_create, name='place_list'),
    path('places/<int:pk>/', place_retrieve_update_destroy, name='place_detail'),
    path('places/<int:place_id>/rooms/', room_list_create, name='room_list'),
    path('places/<int:place_id>/rooms/<int:pk>/', room_retrieve_update_destroy, name='room_detail')
]
