import sys
input = lambda: sys.stdin.readline().strip()

def solve():
    n, q = map(int, input().split())
    a = input()
    b = input()

    dc = [[0] * 26 for _ in range(n + 1)]

    for i in range(n):
        dc[i + 1] = dc[i].copy()
        if a[i] != b[i]:
            ai = ord(a[i]) - ord('a')
            bi = ord(b[i]) - ord('a')
            dc[i + 1][ai] += 1
            dc[i + 1][bi] -= 1

    for _ in range(q):
        l, r = map(int, input().split())
        print(sum(abs(x - y) for x, y in zip(dc[r], dc[l - 1])) // 2)
    return

check = int(input())
for _ in range(check):
    solve()