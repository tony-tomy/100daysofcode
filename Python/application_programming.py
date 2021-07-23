#!python3

# Working with files

# read, readline and readlines for reading data and write or writelines for writng to file

fp = open('D:/Python Workspace/Visual Studio Code/Files/temp.txt', 'w')
fp.write('My first external file')

#content = fp.read()
fp.close()

fp = open('D:/Python Workspace/Visual Studio Code/Files/temp.txt', 'r')
content = fp.read(3)  # number of characters can be specified 
content1 = fp.read()  # pointer will be moved from begining
print(content)
print(content1)
fp.close()

# Regular expression

import re

pattern = 'for'
text = 'Information'
if re.search(pattern, text):
    print('Yes') 

print(re.split(r'[aeiou]', 'abcdefghij'))

text_list = ['Sample ','--text to-','search special character','* in between *','']
for row in text_list:
    if re.search('^\*.*\*$|^-.*-$',row):  # multiple conditions of regular expressions
        print(row)

# syntax is used to name a grouped portion of a match? (?P<name>group) captures the match of group into the backreference “name”

# re.compile() method : combine a regular expression pattern into pattern objects, which can be used for pattern matching

"""
fp = io.StringIO(zenPython)   # Another method to write the data to file
    fp.write(zenPython)

    zenlines = [ line.strip() for line in zenlines ]  
    """

import re
addr = ['100 NORTH MAIN ROAD',
            '100 BROAD ROAD APT.',
            'SAROJINI DEVI ROAD',
            'BROAD AVENUE ROAD']

for i, v in enumerate(addr):
    addr[i] = re.sub('ROAD', 'RD', v) #v.replace("ROAD", "RD")

print(addr)

""" Regular expression question answers

#!/bin/python3

import sys
import os
import io
import re


# Complete the function below.
def subst(pattern, replace_str, string):
    #susbstitute pattern and return it
    new=[re.sub(pattern,replace_str,x) for x in string] # substitue paterns in every element one by one.
    return new


def main():
    addr = ['100 NORTH MAIN ROAD',
            '100 BROAD ROAD APT.',
            'SAROJINI DEVI ROAD',
            'BROAD AVENUE ROAD']
            
    #Create pattern Implementation here 
    pattern = r'\bROAD\b'                #  \b : to deneote starting of word.
    replace = 'RD.'
    
    #Use subst function to replace 'ROAD' to 'RD.',Store as new_address
    new_address = subst(pattern,replace,addr)

    return(new_address)

'''For testing the code, no input is required'''

if __name__ == "__main__":
    f = open(os.environ['OUTPUT_PATH'], 'w')

    res = main();
    f.write(str(res) + "\n")


    f.close()
"""