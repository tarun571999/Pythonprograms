while(True):
    line = input("enter the input")
    if(line[0]=='#'):
        continue
    if(line=='done'):
        break
    print(line)
    print('done')





for i in range(0,10):
    if i==5 :
        continue
    else:
        print(i)

l = ["abcd","hello",655465,77.00]
print(l[0])
print(l[1])
print(l[1][1])
b="hello"
print(b[0:3])

friend = list(input("enter the list").split(" "))



friend = list(input("enter the list").split('e'))
for fr in friend:
    print(fr)



l=[[1,2,3],[["hello"],[4,5,6]]]
print(l[1][1][0])
print(len(l))
l1=[1,2,3,4,5]
print(len(l1))
print(max(l1))
num=0
for i in l1:
    num=num+i

print(num)


