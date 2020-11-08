#print("Hello World")

list_data = list(1,1,1,2,3,2)

m = 6

n = 2

while(n > 0){
    v <- unlist(list_data)
    s = sort(table(v))
    #print(s)
    small_val = as.integer(names(s[1]))
    #print(small_val)
    small_pos = match(small_val, v)
    #print(small_pos)
    list_data = list_data[- small_pos]
    #v.erase(small_pos)
    n = n-1
    #print(n)
    #print(list_data)
}
v <- unlist(list_data)
print(length(v))
print(v)






"

#print(list_data)

#list_data = list_data[- 5]  # remove element from list

#print(list_data)

print(length(list_data)) # length of a list

n = 2

while(n > 0) {  # loop example.
    print(n)
    n = n-1
}

v <- unlist(list_data)

s = sort(table(v))

print(s)
least = as.integer(names(s[1]))
print(least)
print(class(least))

small_pos = match(3, v)  # return first occurance

print(small_pos)
"

"
v <- unlist(list_data)

print(v)

print(sort(table(v)))

s = sort(table(v))

print(s[1][1])

"