#create stores
freelancers = {'name':'freelancing Shop','brian': 70, 'black knight':20, 'biccus diccus':100, 'grim reaper':500, 'minstrel':-15}
antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}

department_store = {}

for shop in [freelancers, antiques, pet_shop]:
    department_store.update(shop)

department_store.pop('name', None)

print(f"Inventory before purchases: {department_store}")

shopping_cart = {}
purse = 1000
for shop in [freelancers, antiques, pet_shop]:
    
    buy_item = input(f"Welcome to {shop['name']}! What do you want to buy: {shop}").lower()
    
    if buy_item == 'exit' or buy_item not in shop:
        print("Exiting shop...")
        continue

    elif buy_item in shop:
        shopping_cart[buy_item] = shop[buy_item]
        shop.pop(buy_item)
        purse -= shopping_cart[buy_item]

print(f"You have purchased: {shopping_cart}")
print(f"Total cost: {sum(shopping_cart.values())} gold pieces")
print(f"You have {purse} gold pieces left")

department_store = {}

for shop in [freelancers, antiques, pet_shop]:
    department_store.update(shop)

department_store.pop('name', None)

print(f"Inventory after purchases: {department_store}")

                                                                            