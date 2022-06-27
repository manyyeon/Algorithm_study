text = input() # 전체 문자열 입력받기

stack = [] # 스택
arr = [] # '-' 기준으로 나눈 숫자들을 모두 더한 걸 넣어놓는 배열

numLen = 0 # 숫자 길이
for i in range(len(text)): # 전체 문자열을 검사
  if(text[i] >= '0' and text[i] <= '9'): # 숫자면
    numLen += 1 # 숫자 길이를 센다
    
    if(i == (len(text)-1)): # 문자열의 맨 끝 인덱스이면
      # 숫자를 구해서 스택에 넣어주고 스택 총합을 배열에 넣는다
      j = i - numLen + 1 # 숫자가 시작하는 인덱스
      numLen = 0 # 숫자 길이 초기화
      num ="" # 숫자를 문자열로 연결한 다음에 int 씌워서 숫자로 바꿀거임
      while(j <= i): # 숫자인 곳만
        num += text[j] # 숫자를 문자열로 연결
        j += 1 # 다음 인덱스
      stack.append(int(num)) # 스택에 숫자를 넣는다
      arr.append(sum(stack)) # 스택에 있는 숫자들의 합을 배열에 넣는다
      stack = [] # 스택 초기화
      
      if(len(arr) == 1): # 마지막에 배열에 숫자 하나만 있으면 '+' 기호만 등장한거임
        result = arr[0] # 결과는 그 숫자
      else:
        result = 2*arr[0] - sum(arr) # 맨 처음 숫자에서 나머지 숫자들의 합을 빼야하는데 계산의 편의를 위해 이렇게 함
        
  elif(text[i] == '+' or text[i] == '-'): # 연산자면
    j = i - numLen # 숫자가 시작하는 인덱스(맨 끝이랑 계산하는 방식이 다름)
    numLen = 0 # 숫자 길이 초기화
    num ="" # 숫자를 문자열로 연결한 다음에 int 씌워서 숫자로 바꿀거임
    while(j < i): # 숫자인 곳만
      num += text[j] # 숫자를 문자열로 연결
      j += 1 # 다음 인덱스
    stack.append(int(num)) # 스택에 숫자를 넣는다
    if(text[i] == '-'): # '-' 기호면
      arr.append(sum(stack)) # 스택에 있는 숫자들의 합을 배열에 넣는다
      stack = [] # 스택 초기화

print(result) # 결과 출력
