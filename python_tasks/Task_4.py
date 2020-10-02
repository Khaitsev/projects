"""Петя решил узнать, когда программисту выгоднее всего искать работу на hh.ru. Конечно, когда больше всего открыто вакансий.

Он выгрузил в текстовый файл время открытия и закрытия всех подходящих вакансий за 2019 год.

Теперь нужно определить период времени, когда открытых вакансий было больше всего.

Считаем, что:

- начальное и конечное время всегда присутствуют;
- начальное время всегда меньше или равно конечному;
- начальное и конечное время включены в интервал.

Входные данные
Входная информация поступает из стандартного ввода, в первой строке приходит 1 число - количество вакансий. Каждая из следующих строк содержит информацию о вакансии в виде двух чисел – начальное и конечное время, они разделены пробелом. Время задается в секундах (https://ru.wikipedia.org/wiki/Unix-время). Некорректные данные на вход не поступают, дополнительные проверки не требуются.


Выходные данные
В качестве ответа в стандартный вывод через пробел нужно вывести два числа: количество найденных интервалов и сумму длительности интервалов в секундах (начальная и конечная секунды должны быть включены в интервал)."""

def intervals_2(intervals):
    new = []
    used = []
    step_count = 0
    intervals.sort()

    # выбираем 2 интервала для сравнения
    for i, interval_check in enumerate(intervals):
        step_count += 1
        new_start, new_end = interval_check[0], interval_check[1]

        if interval_check in used:
            continue

        end_next = len(intervals) + 1
        next = intervals[i + 1:end_next]

        for j, next_check in enumerate(next):

            if new_end >= next_check[0]:
                new_start = next_check[0]
                used.append(next_check)
                if next_check[1] <= new_end:
                    new_end = next_check[1]
                    used.append(next_check)
        new_interval = [new_start, new_end]
        if new_interval and new_interval not in new:
            new.append([new_start, new_end])

    return new


input_intervals = int(input())
intervals = []
while input_intervals > 0:
    input_intervals -= 1
    interval_start, interval_end = input().split()
    interval_start = int(interval_start)
    interval_end = int(interval_end)
    intervals.append([interval_start, interval_end])

list_result = intervals_2(intervals)
intevals_count = len(list_result)

sum_time = 0
for item in list_result:
    sum_time = sum_time + (item[1] - item[0] + 1)

print(intevals_count, sum_time)

