def main():
    # Function that returns a dictionary that contains the frequecy of each letter in a string
    def countLetters(word):
        letters = {}
        for letter in word:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
        return letters
    result = []
    countDic = countLetters(w)
    # Takes substrings of length w from string s
    # Check if the substring is an anagram of the original string
    for i in range(m - n + 1):
        temp = s[i:i + n]
        tempDic = countLetters(temp)
        for j in range(0, n, n):
            if temp[j] in countDic and tempDic[temp[j]] == countDic[temp[j]]:
                if temp[j + 1] in countDic and tempDic[temp[j + 1]] == countDic[temp[j + 1]]:
                    result.append(i)
    return result


w = "ab"
s = "abxaba"
n = len(w)
m = len(s)
print(main())
