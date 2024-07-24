# submission link: https://codeforces.com/contest/1901/submission/272256844
import sys
import math
input = lambda: sys.stdin.readline().strip()

check = int(input())
for _ in range(check):
    n = int(input())
    nums = list(map(int, input().split()))
    mn = min(nums); mx = max(nums)
    res = 0 if mx == mn else int(math.log(mx - mn, 2)) + 1
    print(res)
    if res and res <= n:
        # 为使 mx 和 mn 二进制公共前缀尽量长，将 mx 加到二进制全为 1，即加上 m_
        m_ = (1 << mx.bit_length()) - 1 - mx
        print(m_, (str(0) + ' ') * (res - 1))
    else: print()