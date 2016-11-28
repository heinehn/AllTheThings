import numpy as np
import matplotlib.pyplot as plt
import os
#ionrelax

file1 = "LOCPOT_ionrelax13_zero"
file2 = "LOCPOT_ionrelax_25_25"
file3 = "LOCPOT_ionrelax_25_5"
file4 = "LOCPOT_ionrelax_25_75"
file5 = "LOCPOT_ionrelax_5_25"
file6 = "LOCPOT_ionrelax13_half"
file7 = "LOCPOT_ionrelax_5_75"
file8 = "LOCPOT_ionrelax_75_25"
file9 = "LOCPOT_ionrelax_75_5"
file10 = "LOCPOT_ionrelax_75_75"



standard = np.loadtxt(file1, dtype = 'float', skiprows = 4)
lenght = len(standard[:,0])

meanslab = np.zeros((1,lenght))
vacumeslab = np.zeros((1,lenght))
marker = ['.','o','*','v','s']
files = [file1,file2,file3,file4,file5,file6,file7,file8,file9,file10]
names = ['(0,0)','(0.25,0.25)','(0.25,0.5)','(0.27,0.75)','(0.5,0.25)','(0.5,0.5)','(0.5,0.75)','(0.75,0.25)','(0.75,0.5)','(0.75,0.75)']
textfile = open("tableOfMIP_ionrelax","w")

vacuumepart = []
for i in range(len(files)):
	slab = np.loadtxt(files[i], dtype = 'float', skiprows = 4)

	for k in range(lenght):
		if slab[k,0] >= 49 and slab[k,0] <= 51:
			vacuumepart.append(slab[k,1])
	vacuume = max(vacuumepart)

	line_MIP = 0
	line_count = 0
	for k in range(lenght):
		if k >= 15 and k<=25:
			line_MIP += slab[k,1] - vacuume
			line_count +=1
			print line_MIP,line_count
	line_MIP =  str(abs(line_MIP/line_count))
	line = str(names[i] + ' = ' + line_MIP + '\n')
	textfile.write(line)

	plt.figure(1)
	plt.plot(slab[:,0],slab[:,1]-vacuume)

	meanslab += (slab[:,1] - vacuume)/len(files)
	newslab = [slab[:,0],meanslab]
textfile.close()
plt.legend(loc='smart',fontsize = 20)
plt.xlabel('Lenght [A]',size = 20)
plt.ylabel('Potensial [V]',size = 20)
plt.grid('on')

MIP = 0
count = 0
for k in range(lenght):

	if k >= 15 and k<=25:
		MIP += newslab[1][0][k]
		count +=1

MIP = ("%.2f" % abs(MIP/count))
print 'MIP full = ', MIP
plt.text(44,-55,'MIP = ' + str(MIP) + 'V',size=15)


plt.xticks( fontsize = 20)
plt.yticks( fontsize = 20)
plt.savefig('ION.eps',bbox_inches='tight')
plt.show()
