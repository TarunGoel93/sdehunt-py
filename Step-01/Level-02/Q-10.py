def Half_Diamond_Star_Pattern(n):
    for i in range(1, n+1, 1):
        for j in range(0, i, 1):
            print("*", end="")
        print("")
    
    for i in range(1, n, 1):
        for j in range(n, i, -1):
            print("*", end="")
        print("")
Half_Diamond_Star_Pattern(5)
