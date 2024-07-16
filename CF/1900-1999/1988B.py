def solve():
    n = int(input())
    s = input()
    cnt0 = cnt1 = 0
    last = 1
    for c in s:
        k = int(c)
        if k:
            cnt1 += 1
            last = 1
        elif last:
            cnt0 += 1
            last = 0
    print('YES' if cnt1 > cnt0 else 'NO')

check = int(input())
for _ in range(check):
    solve()
    
