import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




# ANALYTICAL SOLUTION

Ploadf = np.linspace(1e-6,0.001,num=100)
RMS_array1 = []
RMS_array2 = []
#P = [0.00076]                                       Remove Hashtag for the structure plots
for P in Ploadf:
    # Definitions
    a = (44.5*np.pi)/180
    L = 20e-3
    E = 2.5e9
    I = (20e-3*((50e-6)**3))/12
    EI = E*I
    k = 0.0006*20e-3
    xlimit = np.linspace(0,L*np.sin(a),num=100)
    xlimit_r = np.flip(xlimit)
    # Initial Beam Function
    y_initial = -(xlimit/np.tan(a))+(L*np.cos(a))
    
    # X-Deflection, Structure 2
    Dx_2 = (((P*(L**2)*((np.sin(a))**2)*xlimit)-((P*(xlimit**6))/6))/(EI*np.tan(a)))+((P*L*xlimit*np.cos(a))/(k*np.tan(a)))

    # Y-Deflection, Structure 2
    Dy_2 = -((P*(xlimit**3))/(6*EI*np.tan(a)))+((P*(xlimit**2)*L*np.cos(a))/(2*EI))+((P*L*xlimit*np.cos(a))/k)   
    
    # Y-Deflection, Structure 1
    Dy = ((P*(xlimit**3))/(6*EI*np.tan(a)))-((P*(xlimit**2)*L*np.cos(a))/(2*EI))-((P*L*xlimit*np.cos(a))/k)
    
    # Deformed Beam, Structure 2
    Df2 = y_initial+Dy_2
    
    #Deformed Beam, Structure 1
    Dy_r = y_initial+np.flip(Dy)
    
    # Vertical Displacement from referenced flat point 
    Df2_real = Df2-np.amin(Df2)
    Df1_real = Dy_r-np.amin(Dy_r)

    # RMS, Structure 2ms 
    RMS2 = np.sqrt(np.mean(Df2_real**2))
    RMS1 = np.sqrt(np.mean(Df1_real**2))
    RMS_array1.append(RMS1)
    RMS_array2.append(RMS2)
	



# ANALYTICAL SOLUTION DEFORMED STRUCTURES PLOT
# Remove Hashtag for P = [0.00075]

plt.figure(dpi=600)

plt.plot(xlimit,y_initial, color = 'darkgreen', linestyle = '--')
plt.plot(xlimit,Dy_r, color = 'dodgerblue' )
plt.plot(xlimit,Df2, color = 'yellowgreen')

plt.title('Deflected Beam (P = 0.00076 N)')
plt.ylabel('y-dimension')
plt.xlabel('x-dimension')
plt.legend(['Initial Position','Structure 1', 'Structure 2'])
plt.savefig('Deflected Beam 00076')

	

#2D BEAM MODEL 

nametag = np.around(np.arange(1e-5,0.00101,1e-5),10)
RMS_Actual = []

for E in nametag:

    filename = open('')     #Add directory for the data 
    lst = []

    for line in filename:
        lst.append([str(x) for x in line.split()])
    i = 0
    while i < 19:
        del lst[0]
        i = i + 1

    del lst[-11:]

    col1 = [int(x[0]) for x in lst]
    col2 = [float(x[1]) for x in lst]

    Data = col2
    Number = len(Data)

    L = 0.02
    A = np.deg2rad(44.5)
    Height = L*np.cos(A)
    RangeMax = Height+(Height/Number)
    Incr = -(Height/(Number-1))

    OrgLst = np.arange(RangeMax,0,Incr)
    OrgLst[-1] = 0

    NewH = OrgLst+Data
    FinH = NewH-(Data[-1]+OrgLst[-1])

    RMS = np.sqrt(np.mean(FinH**2))
    #print(RMS)
    RMS_Actual.append(RMS)
	



#SINGLE CREASE MEMBRANE MODEL 

nametag_1C = np.around(np.arange(5e-6,5.05e-4,5e-6),10)
RMS_Actual_1C = []
Force_1C = nametag_1C*2

for E_1C in nametag_1C:
    #print(E_1C)
    filename = open('')     #Add directory for the data 
    lst_1C = []

    for line in filename:
        lst_1C.append([str(x) for x in line.split()])
    i = 0
    while i < 19:
        del lst_1C[0]
        i = i + 1

    del lst_1C[-11:]

    col1 = [int(x[0]) for x in lst_1C]
    col2 = [float(x[1]) for x in lst_1C]

    Data_1C = col2
    Number_1C = 201
    RepeatNum = len(Data_1C)
    Repeat = (RepeatNum/Number_1C)

    L_1C = 2
    Height_1C = L_1C*np.cos(A)
    Incr_1C = -(Height_1C/(Number_1C-1))

    OrgLst_1C = np.linspace(0,Height_1C,num=Number_1C)
    OrgLstAdapted = np.tile(OrgLst_1C,Number_1C)

    NewH_1C = OrgLstAdapted+Data_1C
    FinH_1C = (NewH_1C-(np.amin(NewH_1C)))*(10**-2)

    RMS_1C = np.sqrt(np.mean(FinH_1C**2))
    #print(RMS_1C)
    RMS_Actual_1C.append(RMS_1C)




# Validation of 2D Simplification 

plt.figure(dpi=600)

# Plot
plt.plot(nametag, RMS_Actual, color = 'darkgreen')
plt.plot(Force_1C, RMS_Actual_1C, color = 'yellowgreen')

# Minimum Line
plt.plot([nametag[(np.where(RMS_Actual == np.amin(RMS_Actual)))], nametag[(np.where(RMS_Actual == np.amin(RMS_Actual)))]], [0,0.008], color = 'darkgreen', linewidth = 1, linestyle = "--")
plt.plot([Force_1C[(np.where(RMS_Actual_1C == np.amin(RMS_Actual_1C)))], Force_1C[(np.where(RMS_Actual_1C == np.amin(RMS_Actual_1C)))]], [0,0.008], color = 'yellowgreen', linewidth = 1, linestyle = "--")

plt.grid(b=bool)
plt.title('RMS against End-Load')
plt.ylabel('RMS / m')
plt.xlabel('End Load / N')
plt.legend(['2D Beam Model', '3D Half Single-Crease Model'])
plt.savefig('2D Simplification - Graph 1')




# Validation of 2D Simplification 2
# Error Comparing 2D and 3D only

plt.figure(dpi=600)

ErrorLAB = abs(((np.subtract(RMS_Actual,RMS_Actual_1C))/RMS_Actual_1C)*100)

RMS_arrayforSC2 = RMS_array
del RMS_arrayforSC2[1::2]

#ErrorLASC2 = abs(((np.subtract(RMS_array,RMS_Actual_SC2))/RMS_Actual_SC2)*100)

s = np.arange(1,100,2)
Ploadf_forSC2 = Ploadf[[s]]

plt.plot(nametag,ErrorLAB, color = 'dodgerblue')
plt.plot(np.repeat(0.00072,100), np.linspace(0,100,num=100), color = 'darkgreen', linewidth = 1, linestyle = "--")
plt.plot(np.repeat(0.00074,100), np.linspace(0,100,num=100), color = 'yellowgreen', linewidth = 1, linestyle = "--")

plt.grid(b=bool)
plt.title('Percentage Error of 2D against 3D Model')
plt.xlabel('End Load / N')
plt.ylabel('Error / %')
plt.legend(['% Error', 'P at 2D Minimum RMS','P at 3D Minimum RMS'])
plt.savefig('2D Simplification - Graph 2')




# Comparison with Analytical Solution 1
plt.figure(dpi=600)

# Plot with 1C Membrane
plt.plot(Ploadf, RMS_array2, color = 'k')
plt.plot(nametag, RMS_Actual, color = 'darkgreen')
plt.plot(Force_1C, RMS_Actual_1C, color = 'yellowgreen')


plt.plot([Ploadf[(np.where(RMS_array2 == np.amin(RMS_array2)))], Ploadf[(np.where(RMS_array2 == np.amin(RMS_array2)))]], [0,0.008], color = 'k', linewidth = 1, linestyle = "--")
plt.plot([nametag[(np.where(RMS_Actual == np.amin(RMS_Actual)))], nametag[(np.where(RMS_Actual == np.amin(RMS_Actual)))]], [0,0.008], color = 'darkgreen', linewidth = 1, linestyle = "--")
plt.plot([Force_1C[(np.where(RMS_Actual_1C == np.amin(RMS_Actual_1C)))], Force_1C[(np.where(RMS_Actual_1C == np.amin(RMS_Actual_1C)))]], [0,0.008], color = 'yellowgreen', linewidth = 1, linestyle = "--")

plt.fill_between(Ploadf,0.000833,color='royalblue',alpha=0.15)


plt.grid(b=bool)
plt.title('RMS against End-Load')
plt.ylabel('RMS / m')
plt.xlabel('End Load / N')
plt.legend(['ANALYTICAL','Beam', 'Half Single-Crease'])
plt.savefig('RMS against End-Load 2D and 3D with full crease')




# Comparison with Analytical Solution 2

plt.figure(dpi=600)

ErrorLAB = abs(((np.subtract(RMS_array2,RMS_Actual))/RMS_Actual)*100)
ErrorLASC = abs(((np.subtract(RMS_array2,RMS_Actual_1C))/RMS_Actual_1C)*100)


# Make arrays equal
RMS_arrayforSC2 = RMS_array2
del RMS_arrayforSC2[1::2]

s = np.arange(1,100,2)
Ploadf_forSC2 = np.around(Ploadf[[s]],5)


plt.plot(nametag,ErrorLAB, color = 'dodgerblue')
plt.plot(nametag,ErrorLASC, color = 'grey')

plt.plot([nametag[71], nametag[71]], [0,300], color = 'dodgerblue', linewidth = 1.3, linestyle = "--")
plt.plot([Force_1C[73], Force_1C[73]], [0,300], color = 'grey', linewidth = 1.3, linestyle = "--")


plt.grid(b=bool)
plt.title('Percentage Error of the Analytical Solution')
plt.xlabel('End Load / N')
plt.ylabel('Error / %')
plt.legend(['Beam', 'Half Single-Crease'])
plt.savefig('Analytical Solution Error with 2D and 3D')





	
	