import re

a = input()
sum = 0
if a.find('-') != -1:
    idx = a.find('-')
    if idx != 0:
        for str_val in a[:idx].split('+'):
            sum += int(str_val)
    tmp = 0
    for str_val in re.split('[+-]', a[idx+1:]):
        tmp += int(str_val)

    sum -= tmp


else:
    for str_val in a.split('+'):
        sum += int(str_val)
print(sum)