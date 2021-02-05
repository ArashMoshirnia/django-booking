from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from places import get_place_model, get_room_model
from places.models import PlaceType, Address, City, Country, Price, Currency


Place = get_place_model()
Room = get_room_model()


class PlaceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceType
        fields = ('id', 'title')


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')


class CitySerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = City
        fields = ('id', 'name', 'country')


class AddressSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = Address
        fields = ('id', 'city', 'street', 'number', 'phone_number')


class PlaceSerializer(serializers.ModelSerializer):
    type = PlaceTypeSerializer()
    address = AddressSerializer()

    class Meta:
        model = Place
        fields = ('id', 'name', 'star_rating', 'description', 'address', 'type')


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('id', 'name', 'code')


class PriceSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer()

    class Meta:
        model = Price
        fields = ('id', 'value', 'currency')


class RoomSerializer(serializers.ModelSerializer):
    price = PriceSerializer()

    class Meta:
        model = Room
        fields = ('id', 'capacity', 'existing_count', 'description', 'price')

    def calculate_price(self, instance):
        # Ideally inherited from PriceConverterInterface and should have a method named convert
        PriceConverter = self.context.get('price_converter_class')
        request = self.context.get('request')
        if not PriceConverter or not request:
            return None

        destination_currency_id = request.query_params.get('currency_id')
        if not destination_currency_id:
            return None

        try:
            currency = Currency.objects.get(id=destination_currency_id)
        except Currency.DoesNotExist:
            raise ValidationError('Invalid destination currency')

        price_converter = PriceConverter(instance.price, currency)
        price = price_converter.convert()
        serialized_price = PriceSerializer(price).data
        return serialized_price

    def to_representation(self, instance):
        ret = super(RoomSerializer, self).to_representation(instance)
        serialized_price = self.calculate_price(instance)
        if serialized_price is not None:
            ret['price'] = serialized_price

        return ret
