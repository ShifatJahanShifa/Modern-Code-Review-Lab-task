from password_strength_constants import WEAK, MEDIUM, STRONG, INVALID

def check_password_strength(password: str, min_length : int, max_length: int) -> str:

    if not isinstance(password, str) or password == "":
        return INVALID
    
    if not isinstance(min_length, int) or not isinstance(max_length, int):
        return INVALID
    if min_length < 0 or max_length < 0 or min_length > max_length:
        return INVALID
     
    length = len(password)

    if length < min_length:
        return WEAK
    elif min_length <= length < max_length:
        return MEDIUM
    else:
        return STRONG
