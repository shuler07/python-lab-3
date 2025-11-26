n = int(input())

counts = [0] * 100
for _ in range(n):
    x, s = input().split()
    counts[int(x)] += 1
subsum = counts[0]
for i in range(1, 100):
    _subsum = subsum + counts[i]
    counts[i] = subsum = _subsum

print(" ".join(str(i) for i in counts))
