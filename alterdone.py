#problem statement : task is to accept input from the user untill user enters Done, if user enters done print sum,count ,maximum,minimum,and average of all the number the user has entered

l=[]
while(1):
	input1 = input('enter')
	if input1 == 'Done':
		print('Total:',sum(l))
		print('Count:',len(l))
		print('maximum:',max(l))
		print('minimum:',min(l))
		print('the average is:',sum(l)/len(l))
		break
	else:
		num = int(input1)
		l.append(num)
		print('done')
