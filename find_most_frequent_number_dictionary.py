"""
Se da de la tastatura un numar N, dupa care se citesc N numere intr-o lista. Sa se afle care numar apare de
cele mai multe ori in lista, folosind o structura de date de tip dictionar.

INPUT:
5
6 9 10 6 3

OUTPUT:
6

Complexity:
    Time: O(n) = n^2
    Space: O(n) = n
"""

n = int(input())
line = input()

str_numbers = line.split(' ')
numbers = []
for i in range(0, n):
    numbers.append(int(str_numbers[i]))

dictionary = {}
key = ''
value = 0
for i in str_numbers:
    dictionary[i] = dictionary.get(i, 0) + 1
    if dictionary[i] >= value:
        value = dictionary[i]
        key = i

print(key)




