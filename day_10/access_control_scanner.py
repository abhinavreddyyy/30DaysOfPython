revoked_badge_nos = {1001, 1002, 1003, 1004, 1005}
approved_nos = list()
denied_nos = []

while True:
    name = input("What's your name (or type 'done' to finish): ")
    
    if name.lower() == 'done':
        break
    
    badge_no = int(input("What's your badge no: "))
    
    if badge_no in revoked_badge_nos:
        denied_nos.append(name)
        print("ACCESS DENIED")
    else:
        approved_nos.append(name)
        print("ACCESS GRANTED")

approved_nos.sort()
denied_nos.sort()

print("Approved: ", approved_nos)
print("Denied:", denied_nos)

print("\nTotal Approved:", len(approved_nos))
print("Total Denied:", len(denied_nos))



