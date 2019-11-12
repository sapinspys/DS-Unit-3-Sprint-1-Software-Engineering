#!/usr/bin/env python
from random import randint


class Product:
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.id = randint(1000000, 9999999)

    def stealability(self):
        ratio = self.price/self.weight
        if ratio < 0.5:
            return 'Not so stealable..'
        elif ratio < 1:
            return 'Kinda stealable'
        else:
            return 'Very stealable!'

    def explode(self):
        product = self.flammability*self.weight
        if product < 10:
            return '...fizzle'
        elif product < 50:
            return '...boom!'
        else:
            return '...BABOOM!!'


class BoxingGlove(Product):
    def __init__(self, name, weight=10):
        super().__init__(name, weight)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return 'That tickles.'
        elif self.weight < 15:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'
