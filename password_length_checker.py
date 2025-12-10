def check_password_strength(password, a, b):
    length = len(password)

    if length < a:
        return "Weak"
    elif a <= length <= b:
        return "Medium"
    else:
        return "Strong"
