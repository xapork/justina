import re

def check_password_complexity(password):
    complexity_score = 0
    if len(password) >= 8:
        complexity_score += 1
    if re.search(r'[a-z]', password):
        complexity_score += 1
    if re.search(r'[A-Z]', password):
        complexity_score += 1
    if re.search(r'\d', password):
        complexity_score += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        complexity_score += 1

    print(complexity_score)
    return complexity_score

check_password_complexity('Furj*97wlsshira498.')