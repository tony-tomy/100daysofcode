#!python3

'''
Q1. Count ways to reach the n’th stair

There are n stairs, a person standing at the bottom wants to reach the top. The person can climb either 1 stair or 2 stairs at a time. 
Count the number of ways, the person can reach the top.

url : https://www.geeksforgeeks.org/count-ways-reach-nth-stair/

Examples:

Input: n = 1
Output: 1
There is only one way to climb 1 stair

Input: n = 2
Output: 2
There are two ways: (1, 1) and (2)

Input: n = 4
Output: 5
(1, 1, 1, 1), (1, 1, 2), (2, 1, 1), (1, 2, 1), (2, 2)


'''
'''
Approach 1
'''

def n_ways(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n_ways(n-1) + n_ways(n-2)

# Driver Program

s = 4

print("Number of ways :" + str(s) +" steps can climb is " +str(n_ways(s)))


'''
Complexity Analysis:

Time Complexity: O(2^n)
The time complexity of the above implementation is exponential (golden ratio raised to power n) due to redundant calculations.It can be optimized to work in O(Logn) time using the previously discussed Fibonacci function optimizations.
Auxiliary Space: O(1)
'''

'''
Approach 2 : Dynamic Programming
'''

def n_ways_bottom_up(n):
    if n == 0 or n == 1:
        return 1
    nums =[0 for x in range(n+1)]
    nums[0] = 1
    nums[1] = 1
    for i in range(2,n+1):
        nums[i] = nums[i-1] + nums[i-2]
    return nums[n]


# Driver Program

s = 5

print("Number of ways :" + str(s) +" steps can climb is " +str(n_ways_bottom_up(s)))

'''
Generalization of the Problem
How to count the number of ways if the person can climb up to m stairs for a given value m. For example, if m is 4, the person can 
climb 1 stair or 2 stairs or 3 stairs or 4 stairs at a time.

ways(n, m) = ways(n-1, m) + ways(n-2, m) + ... ways(n-m, m)
'''


# A program to count the number of ways 
# to reach n'th stair 

# Recursive function used by countWays 
def countWaysUtil(n, m): 
	if n <= 1: 
		return n 
	res = 0
	i = 1
	while i<= m and i<= n: 
		res = res + countWaysUtil(n-i, m) 
		i = i + 1
	return res 
	
# Returns number of ways to reach s'th stair	 
def countWays(s, m): 
	return countWaysUtil(s + 1, m) 
	

# Driver program 
s, m = 4, 2
print("Number of ways =", countWays(s, m)) 

# Contributed by Harshit Agrawal 


