import sys

N = int(input())
ropes = [int(sys.stdin.readline()) for x in range(N)]

ropes.sort(reverse=True)

i = 0
max = 0
for i in range(N):
  if(max < ropes[i] * (i+1)):
    max = ropes[i] * (i+1)
  else:
    continue
print(max)
