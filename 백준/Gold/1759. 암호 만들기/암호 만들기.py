

s = ['a', 'e', 'i', 'o', 'u']
s = set(s)

l, c = map(int,input().split())
a = list(input().split())
a.sort()
selected = []

def choose(cnt):
  if cnt == c:

    if len(selected) == l:
      consonant = 0
      vowel = 0
      for i in range(len(selected)):
        if vowel >= 1 and consonant >= 2:
          break
        if selected[i] in s:
          vowel += 1
        else:
          consonant += 1
      if vowel >= 1 and consonant >= 2:
        print("".join(selected))
    return

  selected.append(a[cnt])
  choose(cnt + 1)
  selected.pop()

  choose(cnt + 1)


choose(0)
