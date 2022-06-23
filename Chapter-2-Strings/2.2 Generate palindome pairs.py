def main():
    result = []
    # Checks if the word is a palindome
    def isPalidrome(word):
        return word == word[::-1]
    # Generates all possible palindome pairs
    for i in range(n):
        for j in range(n):
            if j == i:
                continue
            # Checks if the concatinated word is a palindome
            if isPalidrome(w_lst[i] + w_lst[j]):
                result.append([i, j])

    return result

w_lst = ["code","edoc","da","d"]
n = len(w_lst)

print(main())
