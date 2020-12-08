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
    Space: O(n) = n
"""

n = int(input())  #1
line = input()  #1

str_numbers = line.split(' ')  #1
numbers = []  #n
for i in range(0, n):  #n
    numbers.append(int(str_numbers[i]))  #1

counter = 0  #1

for i in str_numbers:  #n
    number_of_occurences = str_numbers.count(i)  #1
    if number_of_occurences > counter:  #1
        counter = number_of_occurences  #1
        numbers = i  #1

print (numbers)  #0?

