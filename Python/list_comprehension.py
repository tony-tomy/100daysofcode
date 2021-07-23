#!python3

fruits = ['apple', 'mango', 'kiwi', 'watermelon', 'pear']

fruits_len =[]

for x in fruits:
    fruits_len.append(len(x))

print(fruits)

print(fruits_len)

fruits_mp = []

for x in fruits:
    if x.startswith('m') or x.startswith('p'):
        fruits_mp.append(x)

print(fruits_mp)

