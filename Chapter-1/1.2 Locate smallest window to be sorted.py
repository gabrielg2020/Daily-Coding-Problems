def main():
    # Checks from left to right if the i+1 > i
    for s in range(n-1):
        if input[s] > input[s+1]:
            break
    # Checks from right to left if the i < i+1
    e= n-1
    while e > 0:
        if input[e] < input[e-1]:
            break
        e-=1
    # Finds the min and max value of our subarray
    # Checks if the sorted subarray will sort our list
    max, min = input[s], input[s]
    for i in range(s+1, e+1):
        if input[i] > max:
            max = input[i]
        if input[i] < min:
            min = input[i]
    # If there is a value smaller s=value    
    for i in range(s):
        if input[i] > min:
            s = i
            break
    # If there is a value greater e=value       
    i = n-1
    while i >= e+1:
        if input[i] < max:
            e = i
            break
        i -= 1
    return s,e
    
input =  [3,7,5,6,9]
n = len(input)
print(main())