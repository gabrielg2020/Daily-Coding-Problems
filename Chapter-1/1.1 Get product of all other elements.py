def main():
    # Temp value always = 1
    t = 1
    # Allocating memory space of output
    output = [1 for i in range(n)]
    # Temp will have all the products on the left
    for i in range(n):
        output[i] = t
        t *= input[i]
    # Temp value reset
    t = 1
    # Temp will have all the products on the right
    for i in range(n-1, -1, -1):
        output[i] *= t
        t *= input[i]
    return output


input = [1, 2, 3, 4, 5]
n = len(input)
print(main())
