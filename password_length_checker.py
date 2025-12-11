from password_strength_constants import WEAK, MEDIUM, STRONG, INVALID

def check_password_strength(password, a, b):

    if not isinstance(password, str) or password == "":
        return INVALID
    
    if not isinstance(a, int) or not isinstance(b, int):
        return INVALID
    if a < 0 or b < 0 or a >= b:
        return INVALID
     
    length = len(password)

    if length < a:
        return WEAK
    elif a <= length <= b:
        return MEDIUM
    else:
        return STRONG
