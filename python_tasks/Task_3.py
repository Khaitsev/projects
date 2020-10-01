"""На вход подается 2 подстроки. Нужно определить, можно ли превратить первую во вторую, заменяя одни буквы на другие, с учетом следующих правил:

- участвуют только буквы русского алфавита а-я;
- все буквы в нижнем регистре;
- за один шаг нужно преобразовать все вхождения одной буквы в другую букву.

Входные данные
Входная информация поступает из стандартного ввода в виде одной строки. В этой строке содержатся две подстроки, разделенные пробелом. Ваше решение должно учитывать вариант, когда на вход поданы строки разной длины. Некорректные данные на вход не поступают, дополнительные проверки не требуются.


Выходные данные
В качестве ответа в стандартный вывод программа должна выводить 1 (если превратить можно) или 0 (если превратить нельзя)."""

def word_transform_2(tran, origin):
    tran = tran.lower()
    origin = origin.lower()

    if tran == origin:
        return 1

    if len(origin) != len(tran):
        return 0

    if len(origin) >= 33:
        alf = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
        for symbol in origin:
            if symbol in alf:
                alf.remove(symbol)
        if len(alf) == 0:
            return 0

    dict_to_check = {}
    for i, item in enumerate(tran):
        if item not in dict_to_check:
            dict_to_check[item] = origin[i]
        else:
            if dict_to_check[item] != origin[i]:
                return 0
    return 1


words = input().split(' ')
transform = words[0]
original = words[1]

print(word_transform_2(transform, original))
