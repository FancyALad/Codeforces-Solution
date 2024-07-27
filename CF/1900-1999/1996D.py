# submission link: https://codeforces.com/contest/1996/submission/272901135

import sys
input = lambda: sys.stdin.readline().strip()

check = int(input())
outs = []
for _ in range(check):
    n, x = map(int, input().split())
    ans = 0
    for i in range(1, x - 1):
        for j in range(1, min(n // i, x - i) + 1):
            ans += min((n - i * j) // (i + j), x - i - j)
    outs.append(ans)
print('\n'.join(map(str, outs)))