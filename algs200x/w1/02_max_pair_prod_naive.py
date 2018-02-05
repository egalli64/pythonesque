n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0

for i in range(n):
    for j in range(i+1, n):
        result = max(result, a[i] * a[j])

print(result)