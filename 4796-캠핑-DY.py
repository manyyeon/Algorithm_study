import sys
count = 0
# 0 0 0이 나올 때까지 반복
while(True):
  count+=1
  dap = 0
  L,P,V = map(int,sys.stdin.readline().split()) # L, P, V 입력 받기
  # 0 0 0이 나오면 탈출
  if(L == 0 and P == 0 and V == 0):
    break
  # 전체 휴가 V일 중에 연속하는 P일 중 L일은 캠핑 가능
  # 따라서 V를 P로 크게 나누고 그 중에 L만큼 캠핑 가능한 거니까 곱해줌
  dap += (V // P) * L
  # 그럼 나머지가 생기는데
  if((V % P) > L): # 나머지가 L보다 크면 L을 더해주고 ex) 연속하는 8일 중 3일 가능한데 나머지가 4일임
    dap += L
  else: # 나머지가 L보다 작거나 같으면 나머지를 더해줌 ex) 연속하는 8일 중 3일 가능한데 나머지가 2일
    dap += V % P
  # 출력
  print("Case", count, end = "")
  print(": ", end = "")
  print(dap)
