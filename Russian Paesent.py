a = int(input('First Number: '))
b = int(input('Second Number: '))
ans = []
ans2 = []
while b != 1:
    a = a*2
    ans.append(a)
    b = b//2
    tempa = a%2
    tempb = b%2
    print(a,b)
    if tempa == 0 and tempb == 0:
        ans2.append(a)

    else:
        pass
    print(ans)
    print(ans2)

ans = sum(ans)
ans2 = sum(ans2)
total = ans - ans2
print(total)
    
