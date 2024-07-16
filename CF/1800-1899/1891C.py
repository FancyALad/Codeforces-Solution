def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    s = s_2 = (sum(nums) + 1) // 2
    nums.sort()
    
    i = 0
    # 一个数的一半不会大于等于这个数自身，但是一个数 +1 再除 2 就有可能了。
    # 特例是 1，（1 + 1）// 2 = 1。所以当 n = 1，nums = [1] 时如果不加 i < n 会越界。
    while i < n and s_2 - nums[i] >= 0:
        s_2 -= nums[i]
        i += 1
    ans = n - i + s
    print(ans)

check = int(input())
for _ in range(check):
    solve()
