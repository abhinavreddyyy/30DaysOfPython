add_two_nums = lambda a,b: a +b
print(add_two_nums(2,3))

print((lambda x,y: x * y)(4,5))

# lambda function inside another function 

def power(x):
    return lambda n: x ** n
cube = power(2)(3)
print(cube)

def func(n):
    return lambda a: a - n
print(func(2)(3)) 