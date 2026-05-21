fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
st3 = fruits.union(vegetables)
print(st3)

x = 'awesome'
def myfunc():
    global x
    x = 'fantastic'
myfunc()
print("Python is " + x)

mylist = ['apple', 'banana', 'cherry']
mylist[0] = 'kiwi'
print(mylist[1])

mylist = ['apple', 'banana', 'cherry']
i = 0
for i in range(len(mylist)):
  print(mylist[i])
  i = i + 1