a=["ali","bsaam","hana","karam","lama","mais"]
y=input('inter student name')
x=0
s=0
for x in range (len(a)):
    if(y==a[x]):
        print(a[x],"is graduated")
        s=1
if (s==0):
    print(y,"is not graduated")
