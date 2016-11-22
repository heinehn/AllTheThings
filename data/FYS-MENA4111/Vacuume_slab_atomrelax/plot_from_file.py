import numpy as np
import matplotlib.pyplot as plt

def absdiff(x):
	return np.abs(np.diff(x))

file1 = "LOCPOT_layer5_vac8"
file2 = "LOCPOT_layer5_vac10"
file3 = "LOCPOT_layer5_vac12"
file4 = "LOCPOT_layer5_vac14"
file5 = "LOCPOT_layer5_vac16"
file6 = "LOCPOT_layer5_vac18"
file7 = "LOCPOT_layer5_vac20"

#data = np.loadtxt(file1, dtype = 'float', skiprows = 1, usecols = (1,2))

vac8 = np.loadtxt(file1, dtype = 'float', skiprows = 4)
vac10 = np.loadtxt(file2, dtype = 'float', skiprows = 4)
vac12 = np.loadtxt(file3, dtype = 'float', skiprows = 4)
vac14 = np.loadtxt(file4, dtype = 'float', skiprows = 4)
vac16 = np.loadtxt(file5, dtype = 'float', skiprows = 4)
vac18 = np.loadtxt(file6, dtype = 'float', skiprows = 4)
vac20 = np.loadtxt(file7, dtype = 'float', skiprows = 4)

files = [vac8,vac10,vac12,vac14,vac16,vac18,vac20]

plt.close('all')

print len(files)
for i in range(len(files)):
	plt.figure(i)
	plt.plot(files[i][:,0],files[i][:,1])
	plt.title(8+2*i)


"""
my_toten = slab_vac[:,3]
my_press = slab_vac[:,2]
my_drift = slab_vac[:,1]
my_mxForce = slab_vac[:,0]
my_range = range(len(my_toten))


en_diff = absdiff(my_toten)
press_diff = absdiff(my_press)
drift_diff = absdiff(my_drift)
mxF_diff = absdiff(my_mxForce)

diff_bulk_slab = bulk_cut/3 - slab_cut/6
print diff_bulk_slab[:,3]


plt.figure(1)
plt.plot(en_diff, label = '$\Delta$E')
#plt.plot(press_diff, label = '$\Delta$P')
#plt.plot(mxF_diff, label = '$\Delta$mxF')
plt.grid('on')
plt.xticks( fontsize = 20)
plt.yticks( fontsize = 20)
plt.xlabel(r'Vacuum distance [A]', size = 20,labelpad= 5 )
plt.ylabel(r'$\Delta$',size = 20, labelpad = 5)
plt.title( r'Convergence for different vacuum distance in $GaN$',size = 25 )
plt.legend(loc='smart',fontsize = 15)
#plt.savefig('plot_GaN_vacuum_relax.png',bbox_inches='tight')


plt.figure(1)
plt.plot(vac8[:,0],vac8[:,1])
#plt.plot(press_diff, label = '$\Delta$P')
#plt.plot(mxF_diff, label = '$\Delta$mxF')
plt.grid('on')
plt.xticks( fontsize = 20)
plt.yticks( fontsize = 20)
plt.xlabel(r'Distance [A]', size = 20,labelpad= 5 )
plt.ylabel(r'Potensial [V]',size = 20, labelpad = 5)
plt.title( r'Potensial vs distance in $GaN$ slab',size = 25 )
plt.legend(loc='smart',fontsize = 15)
#plt.savefig('plot_GaN_potensial_vacuum10.eps',bbox_inches='tight')


plt.figure(2)
plt.plot(slab_locpot12[:,0],slab_locpot12[:,1])
#plt.plot(press_diff, label = '$\Delta$P')
#plt.plot(mxF_diff, label = '$\Delta$mxF')
plt.grid('on')
plt.xticks( fontsize = 20)
plt.yticks( fontsize = 20)
plt.xlabel(r'Distance [A]', size = 20,labelpad= 5 )
plt.ylabel(r'Potensial [V]',size = 20, labelpad = 5)
plt.title( r'Potensial vs distance in $GaN$ slab',size = 25 )
plt.legend(loc='smart',fontsize = 15)
#plt.savefig('plot_GaN_potensial_vacuum12.eps',bbox_inches='tight')

plt.figure(3)
plt.plot(slab_locpot14[:,0],slab_locpot14[:,1])
#plt.plot(press_diff, label = '$\Delta$P')
#plt.plot(mxF_diff, label = '$\Delta$mxF')
plt.grid('on')
plt.xticks( fontsize = 20)
plt.yticks( fontsize = 20)
plt.xlabel(r'Distance [A]', size = 20,labelpad= 5 )
plt.ylabel(r'Potensial [V]',size = 20, labelpad = 5)
plt.title( r'Potensial vs distance in $GaN$ slab',size = 25 )
plt.legend(loc='smart',fontsize = 15)
#plt.savefig('plot_GaN_potensial_vacuum14.eps',bbox_inches='tight')

plt.figure(4)
plt.plot(slab_locpot16[:,0],slab_locpot16[:,1])
#plt.plot(press_diff, label = '$\Delta$P')
#plt.plot(mxF_diff, label = '$\Delta$mxF')
plt.grid('on')
plt.xticks( fontsize = 20)
plt.yticks( fontsize = 20)
plt.xlabel(r'Distance [A]', size = 20,labelpad= 5 )
plt.ylabel(r'Potensial [V]',size = 20, labelpad = 5)
plt.title( r'Potensial vs distance in $GaN$ slab',size = 25 )
plt.legend(loc='smart',fontsize = 15)
plt.savefig('plot_GaN_potensial_vacuum16.eps',bbox_inches='tight')



#energy = data[:,1]
#en_diff = absdiff(energy)
cutoff_range = range(200,850,50)

plt.figure(1)
plt.plot(cutoff_range, diff_bulk_slab[:,3])
#plt.plot(drift_diff, label = '$\Delta$drift')
#plt.plot(mxF_diff, label = '$\Delta$mxF')
plt.grid('on')
plt.xticks( fontsize = 20)
plt.yticks( fontsize = 20)
plt.xlabel(r'Cutoff energy [eV]', size = 20,labelpad= 5 )
plt.ylabel(r'$\Delta$',size = 20, labelpad = 5)
plt.title( r'$\Delta$ E bulk v.s. slab cutoff in $GaN$',size = 25 )
plt.legend(loc='smart',fontsize = 15)

#plt.savefig('GaN_cutoff_bulkVSslab.png',bbox_inches='tight')


plt.savefig('GaN_cutoff_bulkVSslab.png',bbox_inches='tight')




plt.figure(2)
plt.plot(my_range,press_diff, label = '$\Delta$P')
plt.grid('on')
plt.xticks( fontsize = 20)
plt.yticks( fontsize = 20)
plt.xlabel(r'Cutoff energy [eV]', size = 20,labelpad= 5 )
plt.ylabel(r'$\Delta$P [kbar]',size = 20, labelpad = 5)
plt.title( r'$\Delta$P with different cutoff in $Ga_2N_2$',size = 25 )
#plt.legend(loc='smart',fontsize = 15)



plt.figure(2)
plt.plot(x,np.polyval(hcp_x,x), label = 'x-direction')
plt.plot(x,np.polyval(hcp_y,x), label = 'y-direction')
plt.plot(x,np.polyval(hcp_z,x), label = 'z-direction')
plt.grid('on')
plt.xticks( fontsize = 20)
plt.yticks( fontsize = 20)
plt.xlabel(r'distance [A]', size = 20,labelpad= 5 )
plt.ylabel(r'Energy [eV]',size = 20, labelpad = 5)
plt.title( r'Fitted energy curve for hcp',size = 25 )
plt.legend(loc='smart',fontsize = 15)
#plt.savefig('plot_hcp.png',bbox_inches='tight')
"""
plt.show()
