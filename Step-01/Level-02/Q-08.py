def Inverted_Star_Pyramid(n):
    for i in range(1, n+1, 1):
        for j in range(0, i-1, 1):
            print(" ", end="")
        for k in range(0, (2*n - (2*i - 1)), 1):
            print("*", end="")
        print("")
Inverted_Star_Pyramid(5)
