import numpy
# creating numpy array from python list
array = numpy.array([1, 2, 3, 4, 5], dtype=float)
print(type(array))
print(array.shape)

numpy_two_dimenion_array = numpy.array([[1, 2, 3], [4, 5, 6]], dtype=int)
print(numpy_two_dimenion_array.shape)

numpy_zeroes = numpy.zeros((3,4), dtype=int, order='C')
print(numpy_zeroes)