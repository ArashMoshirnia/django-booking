from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from places import get_place_model, get_room_model, get_booking_model
from places.api.serializers import PlaceSerializer, RoomSerializer, BookingSerializer
from places.controllers import DummyPriceConverter


Place = get_place_model()
Room = get_room_model()
Booking = get_booking_model()


class PlaceListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

    def create(self, request, *args, **kwargs):
        return Response(data={'detail': 'Not implemented'}, status=405)


class PlaceDetailViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

    def update(self, request, *args, **kwargs):
        return Response(data={'detail': 'Not implemented'}, status=405)

    def destroy(self, request, *args, **kwargs):
        return Response(data={'detail': 'Not implemented'}, status=405)


class RoomListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get_queryset(self):
        place_id = self.kwargs.get('place_id')
        return self.queryset.filter(
            place_id=place_id
        )

    def create(self, request, *args, **kwargs):
        return Response(data={'detail': 'Not implemented'}, status=405)


class RoomDetailViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def retrieve(self, request, *args, **kwargs):
        room = self.get_object()
        context = {
            'request': request,
            'price_converter_class': DummyPriceConverter
        }
        serialized_room = RoomSerializer(room, context=context)
        return Response(serialized_room.data)

    def update(self, request, *args, **kwargs):
        return Response(data={'detail': 'Not implemented'}, status=405)

    def destroy(self, request, *args, **kwargs):
        return Response(data={'detail': 'Not implemented'}, status=405)


class BookingListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_queryset(self):
        return self.queryset.filter(
            user=self.request.user
        )

    def create(self, request, *args, **kwargs):
        return Response(data={'detail': 'Not implemented'}, status=405)


class BookingDetailViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def update(self, request, *args, **kwargs):
        return Response(data={'detail': 'Not implemented'}, status=405)

    def destroy(self, request, *args, **kwargs):
        return Response(data={'detail': 'Not implemented'}, status=405)


place_list_create = PlaceListViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
place_retrieve_update_destroy = PlaceDetailViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})
room_list_create = RoomListViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
room_retrieve_update_destroy = RoomDetailViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})
booking_create = BookingListViewSet.as_view({
    'post': 'create'
})
