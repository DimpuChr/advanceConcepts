import numpy as np

rng = np.random.default_rng()

x = np.random.randint(0, 100)

print(x)
y = rng.integers(0, 100, 3)
print(y)

z = rng.random(size=3)
print(z)

arr = [1, 2, 3, 4, 5]
rng.shuffle(arr)
print(arr)
