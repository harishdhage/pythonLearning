import numpy as np

print(np.__version__)
ax = np.array([1,2,3,4])
ax = ax*2
print(ax)
print(type(ax))
print("Array dimention of ax - ",ax.ndim)
ap = np.array('Apple')
print("Array dimention of ap - ",ap.ndim)