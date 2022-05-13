name=input('inter your name')
file=open('D://q.txt','r')
z=0
x=0
for x in range(20):
    line=file.readline()
    print(line)
    y=input('answer')
    y=y+"\n"
    line=file.readline()
    if y==line:
        z+=1
print(name,z)
w=open('D://w.txt','w')
l=[name,str(z)]
w.writelines(l)
w.close()
