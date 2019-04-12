UC_letters = [x for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
LC_letters = [x for x in "abcdefghijklmnopqrstuvwxyz"]
numbers = [str(x) for x in range(10)]
symbols = [x for x in ".?!&#,;:-_*"]

def is_good_password(password):
    check = [1 if x in UC_letters\
    else 2 if x in LC_letters\
    else 3 if x in numbers\
    else 0 for x in password]
    return (1 in check and 2 in check and 3 in check)

# print(is_good_password("hDS3sd"))

def password_score(password):
    check = [1 if x in UC_letters\
    else 2 if x in LC_letters\
    else 3 if x in numbers\
    else 4 if x in symbols\
    else 0 for x in password]
    return sum(set(check))

# print(password_score("he2loLSA?"))
