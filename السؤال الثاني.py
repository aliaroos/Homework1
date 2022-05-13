x=int(input('A number'))
s=[]
while 1:
    y=x
    s.append(x%2)
    x=int(x/2)
    if x==0:
        break
d=list(s)
for v in range(len(s)):
    s[v]=d[len(s)-1-v]
print(s)
