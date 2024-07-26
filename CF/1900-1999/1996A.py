import sys
input = lambda: sys.stdin.readline().strip()

def solve():
    n = int(input())
    print(n // 4 + (n % 4) // 2)

    return

check = int(input())
for _ in range(check):
    solve()