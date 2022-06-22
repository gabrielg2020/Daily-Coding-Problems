def main():
    # Create a list of zeros
    result = [0]*n
    # Check if i + 1 < i
    # Add to the counter
    for i in range(n):
        for j in range(i + 1, n):
            if input[j] < input[i]:
                result[i] += 1
    return result


input = [3, 4, 9, 6, 1]
n = len(input)
print(main())
