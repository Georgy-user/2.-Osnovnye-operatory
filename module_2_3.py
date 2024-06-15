# Дан список чисел [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# 1. Запишите исходный список в переменную my_list.
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
print('Исходные данные:')
print(my_list)

# Номер элемента списка.
nomer = 0

# Длина списка.
dlina_ml = len(my_list)
# element = 0

# Нужно выписывать из списка только положительные числа до тех пор,
# пока не встретите отрицательное или не закончится список (выход за границу).
while nomer < dlina_ml:
    element = my_list[nomer]
    if element > 0:
        print(my_list[nomer])
        nomer = nomer + 1
        continue
    elif element == 0:
        nomer = nomer + 1
        continue
    else:
        break
# print('Цикл закончен')