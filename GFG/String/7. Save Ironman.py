def saveIronman(s):
    # Complete the function
    s = s.lower()
    s = "".join([x for x in s if x.isalpha() or x.isdigit()])
    if s == s[::-1]:
        return True
    return False
