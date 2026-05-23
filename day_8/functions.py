# Basic Declaring and calling function
def greet():
    first_sentence = input("enter your first sentence:")
    second_sentence = input("Enter your second sentence:")
    full_sentence = first_sentence + " " + second_sentence
    print(full_sentence)
greet() 

# Function returning a Value
def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())

# Function with parameters
def greetings(name1):
    message = name1 + ", Welcome to 30 Days Of Python Challenge!"
    return message
print(greetings("Abhinav"))

def area_of_circle(r):
    pi = 3.14
    area = pi * r**2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total
print(sum_of_numbers(100))
print(sum_of_numbers(1000))

def weight_of_object(mass, gravity=9.81):
    weight = str(mass * gravity)
    return weight + " N"
print("Weight of an object in Newtons: ", weight_of_object(100, 6))


def greet(name, location):
   
    print("Hi there", name, "how is the weather in", location)

greet(name="Alice", location="New York")  

my_dict = {"name": "Alice", "location": "New York"}

greet(**my_dict)  

