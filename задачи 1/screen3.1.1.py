def dislike_6(a):
    if isinstance(a, (int, float)):
        if a == 6:
            return "Только не 6!"
        else:
            return True
    else:
        return False
result = dislike_6(6)
print(result) 
