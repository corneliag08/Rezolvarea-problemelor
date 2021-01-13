with open('globulet.txt','r') as f:
    a=f.readline()
    r=int(a)+3
    albst=((int(a))+r)-2
    t= int(a)+r+albst
with open('bradut.txt','w') as f:
    f.write(str(t))    