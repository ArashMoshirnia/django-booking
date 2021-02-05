from abc import ABC, abstractmethod


class PriceConverterInterface(ABC):
    def __init__(self, price, destination_currency):
        self.price = price
        self.destination_currency = destination_currency

    @abstractmethod
    def convert(self):
        """
        Method that should use price and destination currency and then return a new Price instance
        :return:
        """
        pass
