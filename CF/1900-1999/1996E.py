# submission link: https://codeforces.com/contest/1996/submission/272911832

import sys
input = lambda: sys.stdin.readline().strip()

def solve():
    s = input()
    n = len(s)
    pre = [0] * (n + 1)
    for i in range(n):
        if s[i] == '0':
            pre[i + 1] = pre[i] + 1
        else:
            pre[i + 1] = pre[i] - 1

    ans = 0
    f = [0] * (2 * n + 1)
    for i in range(n + 1):
        t = pre[i]
        ans = (ans + f[t] * (n - i + 1)) % 1_000_000_007
        f[t] += (i + 1)

    print(ans)
    return

check = int(input())
for _ in range(check):
    solve()