# submission link: https://codeforces.com/contest/1996/submission/272751892

import sys
input = lambda: sys.stdin.readline().strip()

def solve():
    n, k = map(int, input().split())
    outs = []
    for i in range(n):
        s = input()
        if not (i % k):
            outstr = ''
            for j in range(0, n, k):
                outstr += s[j]
            outs.append(outstr)
    for s in outs:
        print(s)
    return

check = int(input())
for _ in range(check):
    solve()