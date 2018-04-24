a=0
b=0
c=int(input('?'))
d=[]
while c>b:
    b+=1
    a+=1
    if c%a==0:
        d.append(a)
print(d)
if len(d)==2:
    print(str(c)+'는 소수입니다.')