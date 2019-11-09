from random import randint

def generate_products(count=30):
    adj = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
    noun = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']
    product_list = []

    while count > 0:
        product = f'{adj[randint(0,len(adj))]} {noun[randint(0,len(noun))]}
        product_list.append(product)
        count --
    
    return product_list