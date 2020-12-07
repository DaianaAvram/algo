"""
Se da de la tastatura un numar N, dupa care se citesc N numere intr-o lista. Sa se afle care numar apare de
cele mai multe ori in lista.

INPUT:
5
6 9 10 6 3

OUTPUT:
6

Complexity:
    Time: O(n) = (1 + 1 + 1 + 1 + n + 1 + n^2 + 1) = (6 + 2n^2) = n^2
    Space:
"""

n = int(input())
line = input()

str_numbers = line.split(' ')
numbers = []
for i in range(0, n):
    numbers.append(int(str_numbers[i]))

counter = 0

for i in str_numbers:
    number_of_occurences = str_numbers.count(i)
    if number_of_occurences > counter:
        counter = number_of_occurences
        numbers = i

print (numbers)

