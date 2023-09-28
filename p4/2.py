"""Напишіть функцію prepare_data, 
яка видаляє з переданого списку найбільше та найменше значення, 
сортує його в порядку зростання  i повертає змінений список як результат."""


def prepare_data(data=None):
    b = sorted(data)
    delete_firs = b.pop(0)
    delete_last = b.pop(-1)

    return b


print(prepare_data(data=[1, 5, 77, 66, 88, 111, 6]))
