f = open("../day_19/reading_file_example.txt")
text = f.read()
print(type(text))
print(text)
f.close()

with open("../day_19/reading_file_example.txt", 'a') as f:
    f.write('\n So tell me about yourself')
print(f)


import os
if os.path.exists("../day_19/reading_file_example.txt"):
    os.remove("./files/reading_file_example.txt")
else:
    print("The file does not exist")


import json
person_json = '''{
    "name": "Alice",
    "age": 30,
    "city": "New York"
}'''
person_dict = json.loads(person_json)
print(type(person_dict))
print(person_dict)

import json
people = {
    'name' : 'vaibhav',
    'age' : 23 
}
people_json = json.dumps(people, indent=2)
print(people_json)

import csv
with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # we use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')

