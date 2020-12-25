import random

money = 100
arr2d = [[0] * 3 for i in range(5)]

for i in range(len(arr2d)):
    for j in range(3):
        arr2d[i][j] = random.randint(-2, 2)

for i in range(5):
    print(arr2d[i])

counter = 0
for i in range(5):
    if arr2d[i][0] + arr2d[i][1] + arr2d[i][2] > 0:
        counter += 1
if counter > 2:
    money += 5
elif counter <= 2:
    money -= 5

print(money)
