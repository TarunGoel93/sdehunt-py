def Symmetric_Butterfly_Pattern(n):
    # Upper half
    for i in range(1, n+1, 1):
        # print star (-x, y)
        for j in range(1, i+1, 1):
            print("*", end="")

        # print space (-x, y)
        for k in range(0, n-i, 1):
            print(" ", end="")

        # print space (x, y)
        for l in range(0, n-i, 1):
            print(" ", end="")

        # print star (x, y)
        for m in range(1, i+1, 1):
            print("*", end="") 

        print("")

    # Lower half
    for i in range(n, 1, -1):
        # print star (-x, -y)
        for j in range(1, i, 1):
            print("*", end="")

        # print space (-x, -y) (x, -y)
        for k in range(0, 2*(n-i+1), 1):
            print(" ", end="")

        # print star
        for l in range(1, i, 1):
            print("*", end="")

        print("")

Symmetric_Butterfly_Pattern(5)
