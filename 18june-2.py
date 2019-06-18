import numpy as np

x=np.array([[2,5,8],[3,6,2]])
print(x)

print(x[0][0])

y=x+7
print(type(y))
print(y)

z=np.array([[2,7],[3,8],[2,9],[9,4]])
print(z.shape)
print(z[0:2])
print(z[0:])
print(z[0:,0])
