def main():
    smax = input[0]
    cmax = input[0]
    # Loops throigh the input list
    # Will check the biggest between i and cmax + 1
    # Will check the biggest between smax and cmax
    # cmax is the max of the current array
    # smax is the max of the sub array
    for i in range(1, n):
        cmax = max(input[i], cmax + input[i])
        smax = max(smax, cmax)
    return smax

input = [34, -50, 42, 14, -5, 86]
n = len(input)
print(main())
