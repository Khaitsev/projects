# 1.  Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
# func("papa")
# 6
# func("sova")
# 9


WORD = 'papa'

se = set()


def un(x):
    for z in range(len(x)):
        i = 1
        se.add(hash(x[z]))
        # se.add(hash(x[z])) - вывод подстрок в буквах
        b = ''
        while len(x) >= i + z + 1:
            c = x[z + i]
            b = b + c
            if (x[z] + b) != x:
                se.add(hash(x[z] + b))
                # se.add(x[z] + b) - вывод подстрок в буквах

            i += 1
    return se


print(un(WORD))
print(len(un(WORD)))

"""def un(x):
    for z in range(len(x)):
        i = 1
        se.add(x[z])
        b = ''
        while len(x) >= i + z + 1:
            c = x[z + i]
            b = b + c
            if (x[z] + b) != x:
                se.add(x[z] + b)
            i += 1
    return se"""
