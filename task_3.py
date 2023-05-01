from random import randint


data = []
n = int(input("Введите длину массива: "))
for q in range(n):
    data.append(randint(-100, 100))

index_max = [0 for k in range(n - 1)]
index_max.insert(0, 1)
for i in range(1, len(index_max)):
    if data[i - 1] < data[i]:
        index_max[i] = index_max[i - 1] + 1
    else:
        index_max[i] = 1

maximum_index = max(index_max)
max_elem = index_max.index(maximum_index)
max_arr = data[max_elem - maximum_index + 1:max_elem + 1]
print("Исходный массив:", data)
print("Наибольшая непрерывная возрастающая последовательность:", max_arr)
print("Длина данной последовательности:", maximum_index)
