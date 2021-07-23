def numbers = [1, 2, 3]         

assert numbers instanceof List  
assert numbers.size() == 3

println numbers

def heterogeneous = [1, "a", true]  

println heterogeneous

def multi = [[0, 1], [2, 3]]     
assert multi[1][0] == 2 

println multi

String[] arrStr = ['Ananas', 'Banana', 'Kiwi']  

assert arrStr instanceof String[]    
assert !(arrStr instanceof List)

def numArr = [1, 2, 3] as int[]      

assert numArr instanceof int[]       
assert numArr.size() == 3