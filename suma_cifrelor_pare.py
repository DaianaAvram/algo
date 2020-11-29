"""
Se citeste de la tastatura un N si N numere dupa. Sa se afiseze suma numerelor pare.

INPUT:
5
10 14 15 3 7

OUTPUT:
24

Complexity:
    Time: O(n)
    Space: O(n)
"""

n = int(input())
line = input()
even_sum = 0

# numbers = [int(number) for number in line.split(' ')]  # List Comprehension
str_numbers = line.split(' ')
numbers = []
for i in range(0, n):
    numbers.append(int(str_numbers[i]))

for number in numbers:
    if number % 2 == 0:
        even_sum += number

print(even_sum)
