# 1. Объявите функцию get_matrix и напишите в ней параметры n, m и value.
def get_matrix(n, m, value):
    # 2. Создайте пустой список matrix внутри функции get_matrix.
    matrix = []

    # 3. Напишите первый(внешний) цикл for для кол - ва строк матрицы, n повторов.
    for i in range(n):
        # 4. В первом цикле добавляйте пустой список в список matrix.
        stroka_i = []
        matrix.append(stroka_i)
        # 5. Напишите второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов.
        for j in range(m):
            # 6. Во втором цикле пополняйте ранее добавленный пустой список значениями value.
            element_i_j = value
            stroka_i.append(element_i_j)
    # 7. После всех циклов верните значение переменной matrix.
    return matrix

# 8. Выведите на экран(консоль) результат работы функции get_matix.
result1 = get_matrix(2,2,5)
print(result1)
result2 = get_matrix(5,1,4)
print(result2)
result3 = get_matrix(3,4,8)
print(result3)