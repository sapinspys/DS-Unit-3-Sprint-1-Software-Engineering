from random import randint, uniform
from statistics import mean
from acme import Product

adj = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
noun = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']

def generate_products(count=30):
    """Takes in a number and generates a list of that number of products randomly generated from existing adjective and noun lists."""
    product_list = []

    for _ in range(count):
        name =  f'{adj[randint(0,len(adj))]} {noun[randint(0,len(noun))]}'
        price = randint(5,100)
        weight = randint(5, 100)
        flammability = uniform(0, 2.5)
        product_list.append(Product(name, price, weight, flammability))
    
    return product_list

def inventory_report(li)
    """Takes a list of producs and returns a summary."""
    avg_price = mean([product.price for product in li])
    avg_weight = mean([product.weight for product in li])
    avg_flammability = mean([product.flammability for product in li])

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f'Unique product names: {len(set(li))}')
    print(f'Average price: {avg_price}')
    print(f'Average weight: {avg_weight}')
    print(f'Average flammability: {avg_flammability}')
