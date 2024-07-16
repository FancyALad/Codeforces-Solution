def solve():
    n, k = map(int, input().split())
    print((n - 1) // (k - 1) + ((n - 1) % (k - 1) > 0))

check = int(input())
for _ in range(check):
    solve()
