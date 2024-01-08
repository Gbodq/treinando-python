import random
numbers = []
for i in range(100):
    numbers.append(random.randint(1,100))
# Selection Sort
# mover a posição inicial
def selection_sort():
    for pos_inicial in range(0, len(numbers) - 1):
        #vou ter achado a posição do menor número
        menor_pos = pos_inicial
        for index in range(pos_inicial+1, len(numbers)):
            if numbers[menor_pos] > numbers[index]:
                menor_pos = index

        if menor_pos != pos_inicial:
            numbers[menor_pos], numbers[pos_inicial] = numbers[pos_inicial], numbers[menor_pos]

