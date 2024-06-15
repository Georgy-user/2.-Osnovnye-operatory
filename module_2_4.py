# Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print('Исходный список: ', numbers)

# Пустые списки primes и not_primes.
primes = []
not_primes = []

# При помощи цикла for переберите список numbers.
for i in range(len(numbers)):
    if 2 <= numbers[i] <= 3: primes.append(numbers[i])
    else:
        # Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из 1-го цикла.
        for j in range(2, numbers[i]):
            ostatok = numbers[i] % j
            if ostatok == 0:
                not_primes.append(numbers[i])
                break
            elif j == numbers[i-1]:
                primes.append(numbers[i])

print('Список простых чисел: ', primes)
print('Список составных чисел: ', not_primes)