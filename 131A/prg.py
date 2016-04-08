s = input()
c = [c.upper() for c in s if c.upper() == c]
if len(c) == len(s) or (len(c) == len(s) - 1 and s[0] == s[0].lower()):
    s = [c.upper() if c.lower() == c else c.lower() for c in s]
    print(''.join(s))
else:
    print(s)