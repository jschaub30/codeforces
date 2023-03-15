def abbreviate(s):
    l = len(s)
    if l < 11:
        print(s)
    else:
        print(f"{s[0]}{l - 2}{s[-1]}")

n = int(input())
for _ in range(n):
    s = input()
    if len(s) < 11:
        print(s)
    else:
        abbreviate(s)
