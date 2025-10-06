def decrep(n):

    ans = []
    pos = 1
    while n > 0:
        rem = (n%10) * pos
        print(n, rem)
        ans.append(rem)
        n //= 10
        pos *= 10
    
    return reversed(ans)

print(decrep(537))