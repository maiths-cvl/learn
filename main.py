import random

freq = [[0][0]]

for i in range(1000):
    ra = random.randint(1, 2)
    if (ra == 1):
        freq[0] += 1
    if (ra == 2):
        freq[1] += 1

print(freq)