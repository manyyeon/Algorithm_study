import sys

N = int(input()) # 스위치 개수
switch = list(map(int, sys.stdin.readline().split()))
switch.insert(0, 2) # 인덱스 계산을 편하게 하기 위해 0번 인덱스에 의미 없는 값 추가

S = int(input()) # 학생 수
for i in range(S):
  gender, switchNum = map(int, sys.stdin.readline().split())
  if(gender == 1): # 남자
    for j in range(switchNum, N+1, switchNum):
      switch[j] = 0 if (switch[j]==1) else 1
  elif(gender == 2): # 여자
    space = 1
    switch[switchNum] = 0 if (switch[switchNum]==1) else 1
    while((switchNum - space) >= 1 and (switchNum + space) <= N):
      if(switch[switchNum-space] == switch[switchNum+space]):
        switch[switchNum-space] = switch[switchNum+space] = 0 if (switch[switchNum-space]==1) else 1
      else:
        break
      space += 1

result = ""
for i in range(1, N+1, 20):
  end = min(i+20,N+1)
  tmp = " ".join(map(str, switch[i:end]))
  result += tmp
  if(end == N+1):
    break
  result += "\n"

print(result)
