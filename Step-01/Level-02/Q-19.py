def Symmetric_Void_Pattern(n):

    # upper part
    for i in range(n, 0, -1):
        for j in range(0, i, 1):
            print("*", end="")
        for k in range(i, n, 1):
            print(" ", end="")
        for l in range(i, n, 1):
            print(" ", end="")
        for m in range(0, i, 1):
            print("*", end="")
        print()

    # lower part
    for i in range(0, n+1, 1):
        for j in range(1, i+1, 1):
            print("*", end="")
        for k in range(n, i, -1):
            print(" ", end="")
        for l in range(n, i, -1):
            print(" ", end="")
        for m in range(1, i+1, 1):
            print("*", end="")
        print()

Symmetric_Void_Pattern(5)
