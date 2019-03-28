#input 1 output one
di = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
num = int(input('Enter the valid number from 1 to 9\n'))
if num not in di:
    print('number not present please do enter between 0 to 9')
else:
    print(di[num])

    
#input abc a=1 b=2 c=3 output 1+2+3 = 6
dis = {}
count =1
for i in range(65,92):
	    dis[chr(i)] = count
	    count = count+1

for key,value in dis.items():
	    print(key,value)
s = str(input('Enter a string\n'))
val=0
for i in s:
    val = val+dis[i]
print(s,'=',val)
