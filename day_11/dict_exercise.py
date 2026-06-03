#create stores
freelancers = {'name':'freelancing Shop','brian': 70, 'black knight':20, 'biccus diccus':100, 'grim reaper':500, 'minstrel':-15}
antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}

shopping_cart = {}
for shop in [freelancers, antiques, pet_shop]:
    
    buy_item = input(f"Welcome to {shop['name']}! What do you want to buy: {shop}").lower()
    
    if buy_item in shop:
        shopping_cart[buy_item] = shop[buy_item]
        shop.pop(buy_item)
print(f"You have purchased: {shopping_cart}")


