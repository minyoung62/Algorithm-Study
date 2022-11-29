a, b = input().split()


minAns = int(b.replace("6", "5")) + int(a.replace("6", "5"))

maxAns = int(b.replace("5", "6")) + int(a.replace("5", "6"))
print(minAns, maxAns)