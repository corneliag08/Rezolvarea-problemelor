with open('numar.txt','r') as f:
    a=f.readline()
for i in range(1,11):
    t=str(i)+"*"+a+"="+str(i*int(a))
    with open("inmultire.txt","a") as f:
        f.write(x)
        f.write("\n")