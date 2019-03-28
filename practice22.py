# to extract to words defined in the string using string slicing concepts
# to count the n of times the char i appeared in the string
str = 'hi this python class'
str.encode()

print(str[3:7])
print(str[8:15])
count = 0
for i in str:
    if(i == 'i'):
        count = count +1
print('''the "count" of i's in the given string is''', count )
print("hello",end="\n")
print("pyhton")
str = "hel"
str1= "lo"
print(str+str1)
list = [0,1,2]
liu = [3,4,5]
print(list+liu)

l=[]
num= int(input("enter the number"))
for i in range(0, num):
    l[i][0] = str(input("name:"))
    l[i][1] = float(input("score:"))




l= [1,2,3,4,5]
l.insert(2,33)
print(l)

l.remove(3)
print(l)

l.append(44)
print(l)

l.sort()
print(l)

l.pop()
print(l)

l.reverse()
print(l)

def print_full_name(a, b):
    print("Hello ",a+" "+b,'! You just delved into python.',sep='')

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

# code for disabling the softspace feature
print('G', 'F', 'G', sep='')

# for formatting a date
print('09', '12', '2016', sep='-')

# another example
print('pratik', 'geeksforgeeks', sep='@')

print('G', 'F', sep='', end='')
print('G')
# n provides new line after printing the year
print('09', '12', sep='-', end='-2016n')

print('prtk', 'agarwal', sep='', end='@')
print('geeksforgeeks')

a = "hello my name is tharun"
a = a.split(" ")
print(a)
a = "-".join(a)
print(a)

string = input().strip()
sub_string = input().strip()
print(string, sub_string)
print(string.find(sub_string))
string.lower()

s = str(input())
if (s.isalpha()):
    print("True")
else:
    print("False")
if (s.isalnum()):
    print("True")
else:
    print("False")
if (s.isdigit()):
    print("True")
else:
    print("False")
if (s.islower()):
    print("True")
else:
    print("False")
if (s.isupper()):
    print("True")
else:
    print("False")

