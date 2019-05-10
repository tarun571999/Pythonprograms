f = open('song list.txt')
Lines =[]
for line in f:
    Lines.append(line)
print("1.MJ","2.the chainsmokers","3.ed sheeran","4.kygo","5.charlie puth","6.The script","7.one direction","8.sean paul","9.Taylor swift","10.katty perry","11.john legend","12.shawn mendes","13.calvin harris","14.justin beiber","15.imagine dragons","16.Eminem","17.elie goulding","18.enrique iglesias","19.Dj snake",sep='\n')
print("Press 'end' to exit\n")

while True:
    name = input("Enter any one person from above list\n")
    if(name == 'end'):
        break
    else:
        for i in Lines:
            if (i.endswith(name + '\n')):
                print(i)

