s1=input("Enter the first string")
s2=input("Enter the second string")
i=0
c1=0
c2=0
for ch in s1:
    if ch!=' ':
        c1+=1
print("length of s1", c1)
for ch in s2:
    if ch!=' ':
        c2+=1
print("length of s2", c2)
j=c2-1
s3=""
while i<c1 and j>=0:
    s3+=s1[i]
    s3+=s2[j]
    i+=1
    j-=1
while i<c1:
    s3+=s1[i]
    i+=1
while j>=0:
    s3+=s2[j]
    j-=1
print(s3)
