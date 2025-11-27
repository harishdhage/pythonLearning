import numpy as np

print(np.random.uniform(-1,1))
a1 = np.random.default_rng()
randf = a1.uniform(-1,1,3)
print(randf)
randf = a1.uniform(-1,1,(3,2))
print(randf)
