import re

splitWithTag = re.split('([<|>| ])', input())

newStr = ""

i=0
while(i < len(splitWithTag)):
  if(splitWithTag[i] == '<'):
    while(True):
      if(splitWithTag[i] == '>'):
        newStr += splitWithTag[i]
        i+=1
        break
      newStr += splitWithTag[i]
      i+=1
  else:
    newStr += "".join(reversed(splitWithTag[i]))
    i+=1

print(newStr)
