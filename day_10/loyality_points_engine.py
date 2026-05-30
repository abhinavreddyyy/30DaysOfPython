purchases = [3.45, 7, 2, 4.5, 9, 2.3]

def earn_points(prices):
    total = sum(prices)
    return int(total * 3)

def tier_label(points):
    if points >= 500:
        return "Gold"
    elif points >= 100:
        return "Silver"
    else:
        return "Bronze"

price = sum(purchases)
points = earn_points(purchases)

print("Loyality Summary")
print(price)
print(points)
print(tier_label(points))
