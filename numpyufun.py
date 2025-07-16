# without numpy ufunc
# x= [1, 2, 3, 4]
# y = [4, 5, 6, 7]
# z = []

# for i, j in zip(x, y):
#   z.append(i + j)
# print(z)



# with numpy ufunc

# import numpy as np

# x = [1, 2, 3, 4]
# y = [4, 5, 6, 7]
# z = np.add(x, y)

# print(z)
import numpy as np

# def hibaAdd(x, y):
#   return x+y

# hibaAdd = np.frompyfunc(hibaAdd, 2, 1)

# print(hibaAdd([1, 2, 3, 4], [5, 6, 7, 8]))

x=[1,2,3,4,5]
y=np.prod(x)
print(y)


