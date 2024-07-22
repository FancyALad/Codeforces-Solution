# submission link: https://codeforces.com/contest/1372/submission/271860753
from math import sqrt
import sys
input = lambda: sys.stdin.readline().strip()
check = int(input())
'''
def LCD(a: int, b: int) -> int:
    c = b % a
    if c == 0:
        return a
    if c > a:
        a, c = c, a
    return LCD(c, a)

def LCM(a: int, b: int) -> int:
    return a * b // LCD(a, b)
'''

for _ in range(check):
    n = int(input())
    a = 1; b = n - 1
    k = 0
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            k = n // i 
            break
    if k:
        a = k
        b = n - k
            
    print(a, b)
