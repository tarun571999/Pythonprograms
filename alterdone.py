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
