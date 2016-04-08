n = input()
if n:
    try:
        while True:
            w = input()
            if len(w) > 10:
                print(w[0] + str(len(w[1:-1])) + w[-1])
            else:
                print(w)
    except Exception as e:
        pass