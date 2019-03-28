num = int(input("enter the size of the queue\n"))
l=[]
input = []
while(True):
    input = input("enter the command and required parameter\n").split(" ")
    str = str(input[0])
    n1 = int(input[1])
    n2 = int(input[2])
    if (len(l)>num):
        break
    if a=="insert":
        l.insert(n1,n2)
    elif a=="print":
        print(l)
    elif(a=="remove"):
        l.remove(n1)
    elif(a=="append"):
        l.append(n1)
    elif(a=="sort"):
        l.sort()
    elif(a=="pop"):
        l.pop()
    elif(a=="reverse"):
        l.reverse()
    else:
        break
'''alternate code using eval functions'''
n = int(input())
l = []
for i in range(n):
    s = input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"
        eval("l."+cmd)
    else:
        print(l)

