def validate_password(password):
    if len(password) <= 8:   #

        return False
    
    has_upper = has_lower = has_digit = False
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
    
    return has_upper and has_lower and has_digit
 print(validate_password("Pass123"))       # Expected: False
 print(validate_password("Password123"))   # Expected: True