age = 23
height = 6.0
complex_num = 1 +2j

b = float(input("Enter base: "))
h = float(input("Enter height: "))
area_of_triangle = 0.5 * b * h
print(area_of_triangle)

a = input("Enter side a: ")
b= input("Enter side b: ")
c = input("Enter side c: ")
perimeter_of_triangle = float(a) + float(b) + float(c)
print("Perimeter of triangle: ",perimeter_of_triangle)

slope = 2
b = -2

x_intercept = (-b/slope, 0)
y_intercept = (0, b)

print("Slope of the line: ", slope)
print("X-intercept: ", x_intercept)
print("Y-intercept: ", y_intercept)

point_A = (2,2)
point_B = (6,10)

slope = (point_B[1] - point_A[1]) / (point_B[0] - point_A[0])
print("Slope btw point A andd B is: ", slope)

euclidean_distance = ((point_B[0] - point_A[0])**2 + (point_B[1] - point_A[1])**2)**0.5
print("Euclidean distance between point A and B is: ", euclidean_distance)

x = float(input("Enter a value for x: "))
print("The value is ", x**2 + 6*x + 9, "when x = ", x)


import string

x = 'python'
y = 'dragon'

flo = float(len(x))
str = str(len(x))

print(flo, str)

print(len(x) > len(y)) 
print('on' in x and 'on' in y)
print('on' not in x and 'on' not in y)

x = "i hope this course is not full of jargon"
print("jargon" in x)

x = input("Enter hours: ")
y = input("Enter rate per hour: ")
print("Your weekly earning is:", float(x) * float(y))


for i in range(1,6):
    print(i, 1, i*1, i**2, i**3)