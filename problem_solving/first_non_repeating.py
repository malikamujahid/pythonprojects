from collections import Counter
def Repeat(s):
    n = len(s)
    for i in range(n):
        found = False
        for j in range(n):
            if i != j and s[i] == s[j]:
                found = True
                break
        if not found:
            return s[i]
    


s = "aabbccdde"
print(Repeat(s))