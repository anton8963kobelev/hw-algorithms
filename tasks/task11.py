'''Условие задачи "Клумбы":
Алла захотела, чтобы у неё под окном были узкие клумбы с тюльпанам. На схеме земельного участка клумбы обозначаются
просто горизонтальными отрезками, лежащими на одной прямой. Для ландшафтных работ было нанято n садовников.
Каждый из них обрабатывал какой-то отрезок на схеме. Процесс был организован не очень хорошо, иногда один и тот же отрезок или его
часть могли быть обработаны сразу несколькими садовниками. Таким образом, отрезки, обрабатываемые двумя разными садовниками, сливаются в один.
Непрерывный обработанный отрезок затем станет клумбой. Нужно определить границы будущих клумб.

Рассмотрим пример:
Отрезки
[2,3], [3,4] и [3,4] сольются в один отрезок [2,4]. Отрезок [5,6] ни с кем не объединяется, добавляем его в ответ.
'''

'''Формат ввода:
В строке через пробел записаны координаты клумб в формате: start end, где start — координата начала, end — координата конца.
Оба числа целые, неотрицательные. start строго меньше, чем end.
'''

'''Формат вывода:
Нужно вывести координаты каждой из получившихся клумб в отдельных строках.
Данные должны выводится в отсортированном порядке — сначала клумбы с меньшими координатами, затем — с бОльшими.
'''

# Пример ввода -> вывода:
inputs = [
    [
        '7 8', '7 8', '2 3', '6 10'  # -> '2 3' '6 10'
    ],
    [
        '2 3', '5 6', '3 4', '3 4'  # -> '2 4' '5 6'
    ],
    [
        '1 3', '3 5', '4 6', '5 6', '2 4', '7 10'  # -> '1 6' '7 10'
    ]
]

# тут ваше решение: