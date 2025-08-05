import math

class Solution:
    def print_divisors(self, N):
        m = []
        for i in range(1, int(math.sqrt(N)) + 1):
            if N % i == 0:
                m.append(i)
                if i != N // i:
                    m.append(N // i)
        return sorted(m)

if __name__ == "__main__":
    obj = Solution()
    print(obj.print_divisors(36))
