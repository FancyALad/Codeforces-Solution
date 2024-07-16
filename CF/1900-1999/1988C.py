def solve():
    n = int(input())
    l = [n]
    mod = 1
    while mod < n:
        if mod & n > 0:
            l.append(n ^ mod)
        mod <<= 1
    print(len(l))
    for x in reversed(l[1:]):
        print(x, end=' ')
    print(n)

check = int(input())
for _ in range(check):
    solve()
