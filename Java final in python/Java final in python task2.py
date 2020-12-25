import random

a = 19628347
arr_of_digits = []
for digit in str(a):
    arr_of_digits.append(digit)
print(arr_of_digits)

arr1 = arr_of_digits
arr2 = []
arr3 = []

print("arr1: ", sorted(list(set(arr1))))
num2 = ""
for i in range(100):
    for i in range(2):
        num2 += (random.choice(arr_of_digits))
    arr2.append(num2)
    num2 = ""
print("arr2: ", sorted(list(set(arr2))))

num3 = ""
for i in range(1000):
    for i in range(3):
        num3 += (random.choice(arr_of_digits))
    arr3.append(num3)
    num3 = ""
print("arr3: ", sorted(list(set(arr3))))

final_arr = sorted(list(arr1+arr2+arr3))

with open("file.txt", "w")as f:
    for el in final_arr:
        f.write(el+",")
    f.close()

