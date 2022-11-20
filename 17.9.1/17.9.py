while True:
    try:
        # 1. Преобразование введённой последовательности в список
        spisok = [int(c) for c in input('Введите последовательность чисел через пробел: ').split()]
    except ValueError:
        print("Это неправильный ввод! Введите данные согласно условий ввода!")
    else:
        break
while True:
    try:
        num = int(input('Введите число: '))
    except ValueError:
        print("Это неправильный ввод! Введите данные согласно условий ввода!")
    else:
        break

# 2.Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)
def quick_merge(list1):
    s = []
    for i in list1:
        s.append(i)
    s.sort()
    return s


print('Сортированный список:', *quick_merge(spisok))


# 3.Устанавливается номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу.
if min(spisok) <= num <= max(spisok):
    spisok.append(num)
    spisok.sort()


def binary_search(array, element, left, right):
    if element > max(array):
        return print('Нет числа, которое больше введенного')

    elif element < min(array):
        return print('Нет числа, которое меньше введенного')

    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        return middle - 1
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


print('Номер позиции элемента:', binary_search(quick_merge(spisok), num, 0, len(spisok) - 1))
