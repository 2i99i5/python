# coding: utf-8

# PEP-8

"""
2.Представлен список чисел. Необходимо вывести элементы исходного списка,
 значения которых больше предыдущего элемента.
 Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
 Для формирования списка использовать генератор.
"""
list1 = [-20, 10, 25, 9, 35, 33, 35, 40, 40, 45]
print(f"Исходный список: {list1}")
r_list = [el for i, el in enumerate(list1) if list1[i] > list1[i-1]]
print(f"Конечный список: {r_list}")
