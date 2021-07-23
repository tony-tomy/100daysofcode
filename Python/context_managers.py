#!python3

# Context Managers

'''
A Context Manager allows a programmer to perform required activities, automatically, while entering or exiting a Context.

For example, opening a file, doing few file operations, and closing the file is manged using Context Manager

with open('sample.txt', 'w') as fp:

    content = fp.read()

The keyword with is used in Python to enable a context manager. It automatically takes care of closing the file.

'''

# Example 1 : Normal Program

'''
import sqlite3
try:
    dbConnection = sqlite3.connect('TEST.db')
    cursor = dbConnection.cursor()
    '
    Few db operations
    .
    '
except Exception:
    print('No Connection.')
finally:
    dbConnection.close()

'''

# Example 2 : 

import sqlite3
class DbConnect(object):
    def __init__(self, dbname):
        self.dbname = dbname
    def __enter__(self):
        self.dbConnection = sqlite3.connect(self.dbname)
        return self.dbConnection
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dbConnection.close()
with DbConnect('TEST.db') as db:
    cursor = db.cursor()
    '''
   Few db operations
   ...
    '''

# Lab Program 

'''

import zipfile
import sys
import os
import inspect

from zipfile import ZipFile

class FileManager(): 
    def __init__(self, filename, input_text): 
        self.filename = filename 
        self.mode = 'w' 
        self.input_text = input_text
          
    def __enter__(self): 
        self.file = open(self.filename, self.mode) 
        return self.file
      
    def __exit__(self, exc_type, exc_value, exc_traceback): 
        self.file.close()
# Define 'writeTo' function below, such that 
# it writes input_text string to filename.
def writeTo(filename, input_text):
    with FileManager(filename, 'w') as f: 
        f.write(input_text)
    
# Define the function 'archive' below, such that
# it archives 'filename' into the 'zipfile'
def archive(zfile, filename):
    with ZipFile(zfile,'w') as z: 
        z.write(filename)
    

if __name__ == "__main__":
    try:
        filename = str(input())
    except:
        filename = None

    try:
        input_text = str(input())
    except:
        input_text = None

        
    try:
        zip_file = str(input())
    except:
        zip_file = None
        
    res = writeTo(filename, input_text)
    
    if 'with' in inspect.getsource(writeTo):
        print("'with' used in 'writeTo' function definition.")
        
    if os.path.exists(filename):
        print('File :',filename, 'is present on system.')
 
    res = archive(zip_file, filename)
    
    if 'with' in inspect.getsource(archive):
        print("'with' used in 'archive' function definition.")
        
    if os.path.exists(zip_file):
        print('ZipFile :',zip_file, 'is present on system.')    
    

 

'''


'''

#!/bin/python3

import sys
import os
import subprocess
import inspect


from subprocess import Popen

# Complete the function below.

def run_process(cmd_args):
    with Popen(cmd_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc:
        stdout, stderr = proc.communicate()
        return(stdout)
        


if __name__ == "__main__":
    f = open(os.environ['OUTPUT_PATH'], 'w')

    cmd_args_cnt = 0
    cmd_args_cnt = int(input())
    cmd_args_i = 0
    cmd_args = []
    while cmd_args_i < cmd_args_cnt:
        try:
            cmd_args_item = str(input())
        except:
            cmd_args_item = None
        cmd_args.append(cmd_args_item)
        cmd_args_i += 1


    res = run_process(cmd_args);
    #f.write(res.decode("utf-8") + "\n")
    
   
    
    if 'with' in inspect.getsource(run_process):
        f.write("'with' used in 'run_process' function definition.\n")
    
    if 'Popen' in inspect.getsource(run_process):
        f.write("'Popen' used in 'run_process' function definition.\n")
        f.write('Process Output : %s\n' % (res.decode("utf-8")))

    f.close()

    
'''