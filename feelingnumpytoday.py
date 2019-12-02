import numpy as np, matplotlib.pyplot as plt

x=np.linspace(0, 2*np.pi, 100)

y=np.sin(x)

# %matplotlib inline

plt.plot(x,y)

a = np.array([1, 2, 3, 4, 4, 5, 6])
#print(type(a))

#print(a.dtype)

#print(a.size)

#print(a.ndim)

#print(a.shape)

mean_a = a.mean()

print(f'This b  the mean bro {mean_a}')


u=np.array([5, 6])
v=np.array([2, 3])


z = u * v

d = np.dot(u, v)

l = v+1

print(f'Dot product: {d}')

print(f'Multiply vectors: {z}')

print(f'Broadcasting 1 to v: {l}')


x=np.array([1, np.pi/2, np.pi])

u=np.sin(x)


print(u)

print(np.linspace(-3, 3, num=10))