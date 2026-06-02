MAX_SEATS = 8

bus = {
    1 : {
            'name' : "Buddy",
            'breed' : "Golden Retriever",
            'pickup_time' : "08:00",
            'dropoff_time' : "17:00"
        },
    2 : {
            'name' : "Max",
            'breed' : "German Shepherd",
            'pickup_time' : "09:00",
            'dropoff_time' : "18:00"
        },
    3 : {
            'name' : "Bella",
            'breed' : "Labrador Retriever",
            'pickup_time' : "07:30",
            'dropoff_time' : "16:30"
        }
}

print("Starting roaster")

for seat, info in bus.items():
    print(f"Seat no. {seat} name: {info['name']} and picking up at: {info['pickup_time']}")

if len(bus) < MAX_SEATS:
    new_seat = len(bus) + 1
    new_pet = {
        'name' : 'lucky',
        'breed' : 'inde',
        'pickup_time' : '07:00',
        'dropoff_time' : '15:30'
    }
    bus[new_seat] = new_pet

    print("Updated roaster")
    print(f"{new_pet['name']} boards seat {new_seat}")
else:
    print("No free seats")

print("\n-- Roster after pickup --")
for seat, info in bus.items():
  print(f"Seat {seat}: {info['name']}")


remove_name = input("\nWho goes home early? ").strip().lower()

seat_to_remove = 0
for seat, info in bus.items():
  if info['name'].lower() == remove_name:
    seat_to_remove = seat
    break

if seat_to_remove:
  gone = bus.pop(seat_to_remove)
  print(f"\n👋  {gone['name']} (seat {seat_to_remove}) heads home early.")
else:
  print(f"\n⚠️  No passenger name '{remove_name}' on the bus.")


print("\n-- Final roster --")
for seat, info in bus.items():
  print(f"Seat {seat}: {info['name']} (drop-off {info['dropoff_time']})")