def square(x):
    return x * x

def absolute(x):
    if x >= 0:
        return x
    else:
        return -x

def higher_order_func(type):
    if type == 'square':
        return square
    elif type == 'absolute':
        return absolute

result = higher_order_func('square')(5)
print(result)

# closures
def outer_func():
    el = 'Hello'
    def inner_func(x):
        return el + ' ' + x
    return inner_func

result = outer_func()('World')
print(result)

#decorators, multiple decorators
def uppercase_decorator(function):
    def wrapper():
        result = function()
        make_uppercase = result.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def say_hi():
    return 'hello there'
print(say_hi())
 # -------------------decorator
def split_string_decorator(function):
    def wrapper():
        result = function()
        splitted_string = result.split()
        return splitted_string
    return wrapper

@split_string_decorator
@uppercase_decorator
def say_hi():
    return 'hello there'
print(say_hi())

# decorator with parameters
def decorator_with_parameters(function):
    def wrapper_accepts_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepts_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print(f"I am {first_name} {last_name}. I love to teach")

print_full_name("Asabeneh", "Yetayeh", "Finland")

numbers = [1,2,3,4,5]
def square(x):
    return x * x
squared_numbers = map(square, numbers)
print(list(squared_numbers))