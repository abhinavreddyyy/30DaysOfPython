class person:
    def __init__(self, name):
        self.name = name
    
p1 = person('Vaibhav')
print(p1.name)

class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=25, country='nepal', city='kathmandu'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
          self.skills = []

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
      def add_skill(self, skill):
          self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
print(p1.skills)
print(p2.skills)

class Student(Person):
    pass

s1 = Student('Alice', 'Smith', 22, 'USA', 'New York')
print(s1.person_info())
s1.add_skill('Python')
print(s1.skills)