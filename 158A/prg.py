g = ["A", "O", "Y", "E", "U", "I"]
s = [c.lower() for c in input() if c.upper() not in g]
print('.'+'.'.join(s))