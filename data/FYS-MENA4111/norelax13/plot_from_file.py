import numpy as np
import matplotlib.pyplot as plt
#norelax

def absdiff(x):
	return np.abs(np.diff(x))

file1 = "LOCPOT_norelax13_zero"
file2 = "LOCPOT_norelax13_tretre"
file3 = "LOCPOT_norelax13_half"
file4 = "LOCPOT_norelax13_sixsix"
file5 = "LOCPOT_norelax13_tresix" #Strange potensial peak
file6 = "LOCPOT_norelax13_sixtre"

standard = np.loadtxt(file1, dtype = 'float', skiprows = 4)
lenght = len(standard[:,0])

meanslab = np.zeros((1,lenght))
files = [file1,file2,file3,file4,file5,file6]
names = ['(0,0)','(0.3,0.3)','(0.5,0.5)','(0.6,0.6)','(0.3,0.6)','(0.6,0.3)']
marker = ['.','o','*','v','s']
for i in range(len(files)):
	slab = np.loadtxt(files[i], dtype = 'float', skiprows = 4)
	vakum = max(slab[:,1])
	meanslab += slab[:,1]
	plt.figure(1)
	plt.plot(slab[:,0],slab[:,1]-vakum,label='(b,c) = ' + names[i])
#plt.style.use('ggplot')
plt.title('Potensials for unrelaxed slab',size = 25)
plt.legend(loc='smart',fontsize = 20)
plt.xlabel('Lenght [A]',size = 20)
plt.ylabel('Potensial [V]',size = 20)
plt.grid('on')
newslab = [slab[:,0],(meanslab/len(files) - vakum)]

"""
strange_slab = np.loadtxt(file5, dtype = 'float', skiprows = 4)
plt.figure(2)
plt.plot(strange_slab[:,0],strange_slab[:,1],label='(b,c) = (0.3,0.6)' )
plt.title('Potensials for unrelaxed slab',size = 25)
plt.legend(loc='smart',fontsize = 20)
plt.xlabel('Lenght [A]',size = 20)
plt.ylabel('Potensial [V]',size = 20)
plt.grid('on')
"""



#print newslab[1][0][3]
#plt.plot(newslab[0],newslab[1][0]/len(files)-vakum)

MIP = 0
count = 0
for k in range(lenght):
	if k >= 15 and k<=25:
		MIP += newslab[1][0][k]
		count +=1

MIP = ("%.2f" % abs(MIP/count))
print 'MIP = ', MIP
plt.text(10,-55,'MIP = ' + str(MIP) + 'V',size=15)

plt.xticks( fontsize = 20)
plt.yticks( fontsize = 20)
#plt.savefig('plot_GaN_slab13_unrelax.eps',bbox_inches='tight')
plt.show()
