import string
from typing import Optional, Dict


CHAR_UPPER = "upper"
CHAR_LOWER = "lower"
CHAR_DIGIT = "digit"
CHAR_SPECIAL = "special"

ALL_CATEGORIES = [CHAR_UPPER, CHAR_LOWER, CHAR_DIGIT, CHAR_SPECIAL]



def classify_char(char: str) -> Optional[str]:
    """
    Classify a single character into one of four categories:
    - 'upper' for uppercase letters
    - 'lower' for lowercase letters
    - 'digit' for digits
    - 'special' for punctuation symbols

    Returns:
        Optional[str]: One of the category names or None.
    """
    if char.isupper():
        return CHAR_UPPER
    elif char.islower():
        return CHAR_LOWER
    elif char.isdigit():
        return CHAR_DIGIT
    elif char in string.punctuation:
        return CHAR_SPECIAL
    else:
        return None  # unknown/unclassified chars


# ============================
#   DIVERSITY SCORE CALCULATOR
# ============================
def calculate_diversity_score(password: str) -> int:
    """
    Count the number of categories present in a password and return
    a diversity score from 0 to 4.

    Args:
        password (str): The input password.

    Returns:
        int: diversity score (0–4)
             → If user enters characters not in any known category,
               the score remains 0.
    """
    if not password:
        return 0

    categories_found: Dict[str, bool] = {
        CHAR_UPPER: False,
        CHAR_LOWER: False,
        CHAR_DIGIT: False,
        CHAR_SPECIAL: False,
    }

    for char in password:
        category = classify_char(char)
        if category:
            categories_found[category] = True

    score = sum(categories_found.values())

   
    return score
