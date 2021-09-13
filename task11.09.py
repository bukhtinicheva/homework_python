import string
import random

list_=[]

def rs (n):
    a = ''
    for i in range(n):
        a += random.choice(string.ascii_letters)
    return a

def char_count(n):
    length_ = len(n)
    count_up = 0
    count_down = 0
    for i in range(length_):
        if n[i] in string.ascii_lowercase:
            count_up += 1
        else:
            count_down += 1
    if count_up == count_down:
        return -1
    elif count_up > count_down:
        return 1
    else:
        return 0

def massivv(n,k):
    o = []
    for i in range(k):
        u = rs(n)
        o.append(u)
    return o

def procent(mas, n):
    count_mass = len(massivv(n,k))
    k1 = 0
    for i in range(count_mass):
        if char_count(massivv(n, k)[i]) == 1:
            k1 += 1
    return (k1/count_mass*100)


print('Введите количество символов в строке')
n = int(input())
print('Введите количество строк')
k = int(input())

massiv_strings = (massivv(n,k))
print(massiv_strings)
print('Искомый результат = ', procent(massiv_strings, n), '%', sep='')



