import numpy as np

a = np.array([[1, 2, 3], [6, 4, 3], [78, 4, 2]])

print(a.ndim)
print(a.shape)
print(a.size)

print(a[2][0])

a=np.array([0,1])

b=np.array([1,0])

print(np.dot(a,b))