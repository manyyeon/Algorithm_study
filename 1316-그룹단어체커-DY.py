import sys

N = int(input())

count = 0

for i in range(N):
  text = sys.stdin.readline().strip()
  alphabet = []
  now = ''
  isGroupWord = True
  for j in range(len(text)):
    if(text[j] not in alphabet):
      alphabet.append(text[j])
      now = text[j]
    else:
      if(now == text[j]):
        continue
      else:
        isGroupWord = False
        break
  if(isGroupWord == True):
    count += 1

print(count)
