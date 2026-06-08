numbers = [i for i in range(1,11)]
print(numbers)

squares = [i**2 for i in range(1,11)]
print(squares)

even_numbers = [i for i in range(1,11) if i % 2 == 0]
print(even_numbers)

numbers = [-8, -7, -3, -1, 0, 1, 4, 5, 8]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [num for row in list_of_lists for num in row]
print(flattened_list)

tuple_list = [(letter, number) for letter in 'spam' for number in range(4)]
print(tuple_list)

# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_whole_nums = [i for i in numbers if i <= 0]
print(negative_whole_nums)

new_list = [(i, i**0, i**1, i **2, i ** 3, i ** 4, i ** 5) for i in range(11)]
print(new_list)
