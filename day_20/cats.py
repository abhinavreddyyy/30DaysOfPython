import requests
import statistics

cat_api = 'https://api.thecatapi.com/v1/breeds'

cat_info = requests.get(cat_api).json()

weights = []
lifespans = []
country_freq = {}
breed_freq = {}

for cat in cat_info:
    # weight
    weight = cat['weight']['metric']
    low, high = map(float, weight.split(" - "))
    weights.append((low + high) / 2)

    # lifespan
    lifespan = cat['life_span']
    low, high = map(float, lifespan.split(" - "))
    lifespans.append((low + high) / 2)

    # country frequency
    country = cat['origin']
    if country in country_freq:
        country_freq[country] += 1
    else:
        country_freq[country] = 1
    
    # breed frequency
    breed = cat['name']
    if breed in breed_freq:
        breed_freq[breed] += 1
    else:
        breed_freq[breed] = 1

# weights statistics
print("Weight Statistics:")
print(f'Min: {min(weights)}')
print(f'Max: {max(weights)}')
print(f"Mean: {statistics.mean(weights)}")
print(f"Median: {statistics.median(weights)}")
print(f"Standard Deviation: {statistics.stdev(weights)}")

# lifespan statistics
print("\nLifespan Statistics:")
print(f'Min: {min(lifespans)}')
print(f'Max: {max(lifespans)}')
print(f"Mean: {statistics.mean(lifespans)}")
print(f"Median: {statistics.median(lifespans)}")
print(f"Standard Deviation: {statistics.stdev(lifespans)}")

# country frequency
print("\nCountry Frequency:")
for country, freq in country_freq.items():
    print(f"{country}: {freq}")

# breed frequency
print("\nBreed Frequency:")
for breed, freq in breed_freq.items():
    print(f"{breed}: {freq}")