from password_length_checker import check_password_length
from char_diversity_check import calculate_diversity_score
from password_strength_constants import WEAK, MEDIUM, STRONG, INVALID
from input import password, min_length, max_length
from char_diversity_score import DIVERSITY_SCORE_THREE

def check_password_strength() -> str:
    base_strength = check_password_length(password, min_length, max_length)
    diversity = calculate_diversity_score(password)
    
    if base_strength == INVALID:
        return INVALID
    if base_strength == WEAK:
        return WEAK
    if base_strength == MEDIUM:
        if diversity >= DIVERSITY_SCORE_THREE:
            return STRONG
        else:
            return MEDIUM
    if base_strength == STRONG:
        if diversity >= DIVERSITY_SCORE_THREE:
            return STRONG
        else:
            return MEDIUM    
        
print(check_password_strength())