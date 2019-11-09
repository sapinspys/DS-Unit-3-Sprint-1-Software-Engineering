from random import randint

class Product:
    def __init__(self, name, price=10, weight=20, flammability=0.5, id):
        self.name = name    
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.id = randint(1000000,9999999)

    def stealability(self):
        ratio = self.price/self.weight
        if ratio < 0.5:
            return 'Not so stealable..'
        elif 0.5 < ratio < 1:
            return 'Kinda stealable'
        else:
            return 'Very stealable!'

    def explode(self):
        product = self.flammability*self.weight
        if product < 10:
            return '...fizzle'
        elif 10 < product < 50:
            return '...boom!'
        else:
            return '...BABOOM!!'
