def check(s):
  l=[]
  for i in s:
    if i=="[" or i=="(":
      l.append(i)
    elif i=="]": 
      if l.pop() !="[":  
        return False
    elif i==")":   
      if l.pop()!="(":
        return False  
  return len(l)==0
print(check("[(]"))
