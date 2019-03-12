import re

def atoi(text):

    return int(text) if text.isdigit() else text

def natural_keys(text):

    return [atoi(c) for c in re.split(r'(\d+)', text)]


handle = open("input.txt", "r")
n = handle.read().replace('\n', ',')

list = n.split(",")
sorting = []
sum = []
num = int(list[0])

print('Количество игральных костей = ', num)

for i in range(num):
    list[i + 1] = list[i + 1].replace(' ', "")
    sorting.append(str(int(list[i + 1][0]) + int(list[i + 1][2])) + "," + str(int(list[i + 1][1]) + int(list[i + 1][3])) + "," + str(int(list[i + 1][4]) + int(list[i + 1][5])))


for i in range(num):
    sorting[i] = sorting[i].split(",")
    sorting[i].sort(key=natural_keys)

sum = 0

for i in range(num):
    for j in range(num):
        if i != j and sorting[i] == sorting[j] and sorting[j] != '':
            sorting[j] = ''
            sum = sum + 1
    num = num - sum
    sum = 0

print('Результат игральных схем = ', num)

handle.close()