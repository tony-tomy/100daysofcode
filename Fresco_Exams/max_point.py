def maxPoints(elements):
    if len(elements) == 0:
        return 0

    if len(elements) == 1:
        return elements[0]

    upper_limit = max(elements)+1
    new_arr = [0]*upper_limit
    for i in elements:
        new_arr[i] += i

    print(new_arr)
    dp_arr = [0] * upper_limit
    
    dp_arr[1] = max(new_arr[0], new_arr[1])
    print(dp_arr)
    dp_arr[0] = new_arr[0]
    print(dp_arr)

    for i in range(2, upper_limit):
        dp_arr[i] = max(new_arr[i] + dp_arr[i - 2], dp_arr[i - 1])

    print(dp_arr)
    return dp_arr[-1]


elements = [1,1,1,2,2,3]
result = maxPoints(elements)
print(result)