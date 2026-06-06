class Pizza:
    def __init__(self, size, crust_type):
        self.size = size
        self.crust_type = crust_type
        self.toppings = []
    
    def add_topping(self, topping):     
        self.toppings.append(topping)
        print(f'{topping} added!')

    def remove_topping(self, topping):
        if topping == True:
            self.toppings.remove(topping)
            print(f'{topping} removed :)')
        else:
            print(f"{topping} not found")
    
    def pizza_details(self):
        print(f"So the pizza you choose is of size {self.size}, crust type is {self.crust_type}")

        if self.toppings:
            print("Toppings:", ",".join(self.toppings))
        else:
            print("no toppings yikes!")
    

new_pizza = Pizza('thin', 'thick')
new_pizza.add_topping("Cheese")
new_pizza.pizza_details()

 