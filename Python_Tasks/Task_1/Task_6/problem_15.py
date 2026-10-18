# python15
n = int(input())
set_a = set(map(int, input().split()))

m = int(input())
set_b = set(map(int, input().split()))

result = set_a.difference(set_b)

print(len(result))
