import math
import random

import numpy as np

length = 100
spin_values = [-1, 1]
spins = [[random.choice(spin_values) for _ in range(length)] for _ in range(length)]
spins = np.array(spins)

lid = random.randint(1, length)
rid = random.randint(1, length)

cnt = 0
old_spin = spins[lid, rid]
neighbor_ids = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i, j in neighbor_ids:
    if spins[(lid + i + length) % length, (rid + j + length) % length] == old_spin:
        cnt += 1

if cnt <= 2:
    spins[lid, rid] *= -1
elif random.random() < math.exp(-(cnt - 2)):
    spins[lid, rid] *= -1
