from places.base_controllers import PriceConverterInterface


class DummyPriceConverter(PriceConverterInterface):
    def convert(self):
        self.price.currency = self.destination_currency
        return self.price
