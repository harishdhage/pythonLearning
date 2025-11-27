import numpy as np

score = np.array([55,91,100,64,82,77,25])
print(score == 100)
print(score <= 60)
print(score <= 60)
score[score < 60] = 0
print(score)