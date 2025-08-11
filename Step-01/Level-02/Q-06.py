def Inverted_Numbered_Right_Pyramid(n):
    for i in range(n, 0, -1):
        for j in range(1, i+1, 1):
            print(j, end="")
        print("")

Inverted_Numbered_Right_Pyramid(5)
