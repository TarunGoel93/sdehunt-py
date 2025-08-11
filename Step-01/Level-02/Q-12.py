def Number_Crown_Pattern(n):
    for i in range(1, n+1, 1):
        # print numbers (left side)
        for j in range(1, i+1, 1):
            print(j, end="")

        # print stars (middle gap)
        for k in range(0, (2*(n-i)), 1):
            print(" ", end="")

        # print numbers (right side)
        for l in range(1, i+1, 1):
            print(l, end="")

        print("")

Number_Crown_Pattern(5)
