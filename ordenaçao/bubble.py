import random
numbers = []
for i in range(10_000):
    numbers.append(random.randint(1,100_000))
# Bubble Sort
v = 0
for pos_inicial in range(0, len(numbers)-1):
    for pos_atual in range(0, len(numbers)-1-pos_inicial):
        if numbers[pos_atual] > numbers[pos_atual+1]:
            numbers[pos_atual], numbers[pos_atual+1] = numbers[pos_atual+1], numbers[pos_atual]
print(numbers)