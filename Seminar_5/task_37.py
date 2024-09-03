def f(n):
    if n == 0:
        return ""
    k = int(input())
    return f(n-1) + f"{k}"
print(f(int(input())))