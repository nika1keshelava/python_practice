import random

N = random.randint(10000, 20000)
M = random.randint(10000, 20000)

for i in range(1, 99):
    if N % i == 0 and i % 2 == 0:
        print("N divisor: ", i)
    if M % i == 0 and i % 2 == 0:
        print("M divisor: ", i)

