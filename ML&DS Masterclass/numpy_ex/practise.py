import numpy as np

my_list = [1, 2, 3, 4, 5]
my_arr = np.array(my_list)
print(my_arr)

my_matrix = [[1, 2], [3, 4], [5, 6]]
print(my_matrix)
my_npmatrix = np.array(my_matrix)
print(my_npmatrix)

np.arange(0, 10)  # creating np array [0,10) / works like rang(...)
print(np.zeros(5))  # /np.ones()...
print()
print(np.zeros((2, 5)))

np.linspace(0, 10, 50)  # 50numbers * linearly spaced in [0-10]

print()
print(np.eye(5))

print(np.random.rand(1))
print()
print(np.random.rand(5, 6))  # 5rows x 5col with random nums
print()

print(np.random.randn())
print()

print(np.random.randint(0, 100, (4, 5)))
print()

arr = np.arange(0, 25)
print(arr)
print(arr.max())
print(arr.argmax())
print(arr.shape)
arr = arr.reshape(5, 5)
print(arr)
arr[0:5] = 5  # in np only
# so...
arr_copy = arr.copy()
arr_copy[:] = 100
print(arr)

arr = np.arange(0, 25)
bool_arr = arr > 4
print(bool_arr)
print(arr[arr > 4])

print(arr + 5)
print(arr - 5)
print(arr * 5)
print(arr + arr)
print(arr - arr)
# we get only warning for deviding by 0
np.sqrt(arr)
np.sin(arr)
print(arr.sum())
print(arr.mean())
print(arr.var())
print(arr.std())

array_2d = np.arange(0, 25).reshape(5, 5)
print(array_2d.sum(axis=0))  # operations across the column (y) axis
