import random

arr1 = []
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
random_word = ""

for i in range(20):
    for i in range(7):
        random_word += random.choice(letters)
    arr1.append(random_word)
    random_word = ""
print(arr1)


counter = 0
for el in arr1:
    if "a" in el:
        counter += 1
        arr1.remove(el)
print('arr1 without words that contain "a" ' , arr1)

random_words5 = []
for i in range(counter):
    for j in range(5):
        random_word += random.choice(letters)
    random_words5.append(random_word)
    random_word = ""

for el in random_words5:
    arr1.append(el)
print("metodi2 --- modified arr1: ", arr1)

index = random.randint(0,len(arr1))
for i in range(5):
    for j in range(4):
        random_word += str(random.randint(0, 9))
    arr1[index] = random_word
    index -= 1
    random_word = ""
print("with numbers", arr1)

