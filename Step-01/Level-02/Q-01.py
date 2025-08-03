def print_square_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print("*", end="")
        print()

print_square_pattern(5)
