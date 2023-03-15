n = int(input())

print(sum(1 for _ in range(n) if sum(int(x) for x in input().split(" ")) > 1))
