print("You are invited to my party!")

names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']

names.extend(names1)

for index in range(2):
    names.append(input('Enter a new name: '))

for name in names:
    msg1 = f'{name.title()}! You are invited to my party on saturday'
    print(msg1)
    