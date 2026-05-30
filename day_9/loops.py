count = 0
while count < 5:
    print(count)
    count += 1
    if count == 3:
        count += 1
        continue

language = "Python"
for l in language:
    print(l)

for i in range(len(language)):
    print(language[i])

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

#for a, value in person.items():
    #print(a, value)

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')

lst = list(range(11,0,-2))
print(lst)

for number in range(5):
    pass
    