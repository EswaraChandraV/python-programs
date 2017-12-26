s=input().upper()
d={}
list1=[]
list2=[]
f_count=0
m_count=0
for i in range(len(s)):
  if(s[i]=="F"):
    list1.append(s[i])
    f_count+=1
  else:
    list2.append(s[i])
    m_count+=1
print("m_count:",m_count)
print("f_count:",f_count)
print("".join(list1),end="")
print("".join(list2))
  