n = int(input())
s = str(n)
l = len(s)
ans = 0

for d in range(2, l + 1, 2):
    half = d // 2
    start = 10 ** (half - 1)
    end = 10 ** half - 1

    if d < l:
        ans += end - start + 1
    else:
        left = int(s[:half])
        cand = int(str(left) * 2)
        if cand <= n:
            ans += left - start + 1
        else:
            ans += left - start

print(ans)
