import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mtp




# 2D Mesh

Mesh = np.around((np.linspace(1e-6,0.01,num=50)),10)
#Mesh = [0.001837551]
MeshValue = []

for E in Mesh:
    filename = open('')     # Add directory
    lst = []

    for line in filename:
        lst.append([str(x) for x in line.split()])
        
    del lst[:-6]
    del lst[-5:]

    #col1 = [int(x[0]) for x in lst]
    col2 = [float(x[1]) for x in lst]

    Data = col2
    #print(Data)
    MeshValue.append(Data)



	
# 2D Convergence Plot

plt.figure(dpi=900)

MP = ((np.delete(MeshValue,[0]))*(10**2))/3.04
M = np.delete(Mesh,[0])

Poly = np.poly1d(np.polyfit(M,MP,3))
plt.plot(M,MP,color='grey',linestyle='--')
plt.plot(M,Poly(M), color="dodgerblue")
plt.gca().invert_xaxis()


# Plot Characteristics
plt.grid(b=bool)
plt.title('2D Mesh Convergence (P = 0.0001 N) ')
plt.xlabel('Average Mesh Size / $m^2$')
plt.ylabel('Maximum Deformation / 1E-2 m')
plt.legend(['Actual Results','Polynomial Regression'])
plt.savefig('2D Mesh Convergence')	




# 3D Mesh

MeshSC2 = np.around((np.linspace(0.01, 0.5, num=100)),10)
MeshValueSC2 = []

for E in MeshSC2:
    filename = open('')     # Add directory
    lst = []
   
    for line in filename:
        lst.append([str(x) for x in line.split()])
        
                
    del lst[:-6]
    del lst[-5:]

    #col1 = [int(x[0]) for x in lst]
    col2 = [float(x[1]) for x in lst]

    Data = col2
    #print(Data)
    MeshValueSC2.append(Data)




# 3D Mesh Convergence Plot

plt.figure(dpi=900)

MPSC = np.delete(MeshValueSC,[-1])
MSC = np.delete(MeshSC, [-1])

PolySC = np.poly1d(np.polyfit(MSC,MPSC,2))

plt.plot(MSC*(10**-2), MPSC, color='yellowgreen', linestyle = '--')
plt.plot(MSC*(10**-2),PolySC(MSC), color='darkgreen')
plt.gca().invert_xaxis()

plt.grid(b=bool)
plt.title('3D Mesh Convergence (P = 0.0001 N) ')
plt.xlabel('Average Mesh Size / 1E-2 $m^2$')
plt.ylabel('Maximum Deformation / 1E-2 m')
plt.legend(['Actual Results', 'Polynomial Regression'])
plt.savefig('3D Mesh Convergence')




# 3D Tri Mesh

Mesh = np.around((np.linspace(0.01, 0.5, num=100)),10)
#Mesh = [0.001837551]
MeshValueSCTri = []

for E in Mesh:
    filename = open('')     # Add directory
    lst = []

    for line in filename:
        lst.append([str(x) for x in line.split()])
        
    del lst[:-6]
    del lst[-5:]

    #col1 = [int(x[0]) for x in lst]
    col2 = [float(x[1]) for x in lst]

    Data = col2
    #print(Data)
    MeshValueSCTri.append(Data)
	
	
	
# Mesh shape comparison
	
plt.figure(dpi=900)

Error = abs(((np.subtract(MeshValueSC, MeshValueSCTri))/MeshValueSC)*100)

ErrorP = np.delete(Error,[-1])
MSC = np.delete(MeshSC, [-1])

PolySC = np.poly1d(np.polyfit(MSC,ErrorP,2))

plt.plot(MSC*(10**-2), Error, color='yellowgreen', linestyle = '--')
plt.plot(MSC*(10**-2),PolySC(MSC), color='darkgreen')
plt.gca().invert_xaxis()

plt.grid(b=bool)
plt.title('Hexahedral vs. Tetahedral Mesh (P = 0.0001 N)')
plt.xlabel('Average Mesh Size / 1E-2 $m^2$')
plt.ylabel('Error / %')
plt.legend(['Actual Results', 'Polynomial Regression'])
plt.savefig('Mesh Shape Comparison')
