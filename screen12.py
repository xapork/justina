def check(s: str) -> bool:
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            return True
    return False
result = check("abcde")  
print(result)
