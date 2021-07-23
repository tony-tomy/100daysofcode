#!python3

# List : A list is a collection which is ordered and changeable. In Python lists are written with square brackets.

thislist = ['Apple','Banana','Cherry']

print(thislist)

print(thislist[1])

print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

print(thislist[:4])

print(thislist[2:])

print(thislist[-4:-1])

thislist[0] = 'grapes'

print(thislist)

for x in thislist:
    print(x)

if 'orange' in thislist:
    print('Yes, orange exist in the list')

print(len(thislist))

thislist.append('apple')

print(thislist)

# To add an item at the specified index, use the insert() method:

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

thislist.remove('banana')

print(thislist)

thislist.pop()

print(thislist)

del thislist[0]

print(thislist)

