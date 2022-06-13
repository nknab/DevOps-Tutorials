def count_char(_password):
    return len(_password)

def chk_maj(_password):
    for letter in _password:
        if letter.isupper():
            return True
    return False

def chk_special(_password):
    special = ['!', '*', '&']
    for letter in _password:
        if letter in special:
            return True
    return False

def chk_valid(_password):
    password_len = 10
    if count_char(_password) >= 10 & chk_maj(_password) & chk_special(_password):
        return True
    return False


result = chk_valid("C8h-N7ULBZZPUa-c!WDuRuqsr")
if result:
    print("Password is Valid")
else:
    print("Password is Invalid")
