s=input().split()
str=""
lst=[]
for i in s:
  print(i)
  count,s1=0,''
  for j in i:
    if j.lower() in "aeiou":
      count+=1
      if j not in str:
          str=str+j
      if j.lower() not in s1:
        s1+=j.lower()+" "
print("vowel count:",count)
print("vowels: ")
print(str)
