def Alpha_Triangle_char_Pattern(n):
    for i in range(n):
        start_char = n - i 
        for j in range(start_char, n+1):
            print(chr(64 + j), end=" ")
        print()

Alpha_Triangle_char_Pattern(3)

