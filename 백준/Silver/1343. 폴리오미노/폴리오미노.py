a = input()

ans = ""
a = a.replace("XXXX", "AAAA")
a = a.replace("XX","BB")

if "X" in a:
    ans = -1
else :
    ans = a;
print(ans)