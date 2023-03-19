import json
from decimal import Decimal

def build_decimal(string):
    return Decimal(string)

text = '{"total": 9.61, "items": ["Americano", "Omelet"]}'

print(json.loads(text))
print(json.loads(text, parse_float=build_decimal))

class Factory(object):
    def build_sequence(self):
        return []
    
    def build_number(self, string):
        return Decimal(string)

class Loader(object):
    def load(string, factory):
        sequence = factory.build_sequence()
        for substr in string.split(','):
            print(substr)
            item = factory.build_number(substr)
            sequence.append(item)
        return sequence

f = Factory()
result = Loader.load('1.23, 4.56, 7.890', f)
print(result)


from abc import ABCMeta, abstractmethod

class AbstractFactory(metaclass=ABCMeta):
    @abstractmethod
    def build_sequence(self):
        pass

    @abstractmethod
    def build_number(self, string):
        pass
