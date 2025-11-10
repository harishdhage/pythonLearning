
def passwordStrength(pwd):
    if len(pwd) < 8 :
        return False
    if not any(char.isdigit for char in pwd):
        return False
    if not any(char.islower for char in pwd):
        return False
    if not any(char.isupper for char in pwd):
        return False
    if not any(char in '!$#@&*' for char in pwd):
        return False
    return True

print(passwordStrength("Hello"))
print(passwordStrength("Hello1$2"))