drink_count = 0
total_price = 0

while True:
    name = input("What's your name sir (or type 'done' to finish): ")
    if name == "done":
        break
    coffee_name = input("What do you wanna have sir: ")
    if coffee_name == "latte":
        total_price += 3.50
        drink_count += 1
    elif coffee_name == "americano":
        total_price += 3.00
        drink_count += 1
    elif coffee_name == "espresso":
        total_price += 2.50
        drink_count += 1
    else:
        print(f"{coffee_name} is not on the menu: ")
        continue
print(f"The total number of drinks are {drink_count} and the total price for your drinks would be: ${total_price:.2f} \
      How would you like to pay sir?")