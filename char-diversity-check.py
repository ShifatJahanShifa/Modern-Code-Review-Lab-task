

import string


def classify_char(char):
    """
    Classify a single character into one of four categories:
    - 'upper' for uppercase letters
    - 'lower' for lowercase letters
    - 'digit' for digits
    - 'special' for all other printable symbols

    Returns one of these category names or None.
    """
    if char.isupper():
        return "upper"
    elif char.islower():
        return "lower"
    elif char.isdigit():
        return "digit"
    elif char in string.punctuation:
        return "special"
    else:
        # ignore whitespace, unicode symbols, or other unknown chars
        return None


def calculate_diversity_score(password):
    """
    Count the number of categories present in a password and return
    a diversity score from 1 to 4.

    Args:
        password (str): the input password

    Returns:
        int: diversity score (0–4)
    """
    if not password:
        return 0  # no characters → no diversity

    categories_found = {
        "upper": False,
        "lower": False,
        "digit": False,
        "special": False,
    }

    for char in password:
        category = classify_char(char)
        if category:
            categories_found[category] = True

    score = sum(categories_found.values())

    # ensure minimum score of 1 if password exists but contains only unknown chars
    return max(score, 1)



