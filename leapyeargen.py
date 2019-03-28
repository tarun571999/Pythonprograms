year = int(input('enter the year\n'))
l=[]
count=0
def leap_year(year):
	if year%4 == 0 and year%100 != 0 or year%400 == 0:
		return True
	else:
		return False

while(count!= 15):
	if(leap_year(year)):
		count = count+1
		l.append(year)
		year = year +1
	else:
		year = year+1

print(l)
n1 = int(input('enter the start year\n'))
n2 = int(input('enter the end year\n'))
year2 = n1
l2=[]
count1=0
while(year2>=n1 and year2<=n2):
    if(leap_year(year2)):
        count1 = count1+1
        l2.append(year2)
        year2 = year2 +1
    else:
        year2 = year2+1

print(l2)
