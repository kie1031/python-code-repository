a=int(input('?'))
b=int(input('?'))
c=[]
c.append(a)
while len(c)<b:
    c.append(c[-1]*a)
print(c)