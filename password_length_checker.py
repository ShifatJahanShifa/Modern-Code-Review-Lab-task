from password_strength_constants import WEAK, MEDIUM, STRONG

def check_password_strength(password, a, b):
    length = len(password)

    if length < a:
        return WEAK
    elif a <= length <= b:
        return MEDIUM
    else:
        return STRONG
