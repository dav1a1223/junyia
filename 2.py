q1 = 15

def list_num(n):
    ans = 0
    for i in range(1, n+1):
        if i % 15 == 0:
            ans += 1
        elif i % 3 == 0 or i % 5 == 0:
            continue
        else:
            ans += 1
    return ans

print(list_num(q1))