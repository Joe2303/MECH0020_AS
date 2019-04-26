# -*- coding: mbcs -*-
# Import Abaqus functions
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *

# Other Import
import numpy as np

# Change Work Directory
os.chdir(r"N:\Project\ABAQUS\Results\Beam\Beam Mesh")

P = 0.0003
MS = np.around((np.linspace(1e-6,0.01,num=50)),10)

for M in MS:

	# Create Part
	mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=0.02)
	mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(
		decimalPlaces=4)
	mdb.models['Model-1'].sketches['__profile__'].ConstructionLine(point1=(0.0, 
		0.001625), point2=(0.0, -0.00200000004749745))
	mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
		False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[2])
	mdb.models['Model-1'].sketches['__profile__'].ConstructionLine(point1=(0.0, 
		0.001), point2=(0.001625, 0.0))
	mdb.models['Model-1'].sketches['__profile__'].AngularDimension(line1=
		mdb.models['Model-1'].sketches['__profile__'].geometry[3], line2=
		mdb.models['Model-1'].sketches['__profile__'].geometry[2], textPoint=(
		0.00153005588799715, -0.00137725635431707), value=44.5)
	mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-0.001875, 0.002), 
		point2=(0.00325, -0.00325))
	mdb.models['Model-1'].sketches['__profile__'].ParallelConstraint(entity1=
		mdb.models['Model-1'].sketches['__profile__'].geometry[3], entity2=
		mdb.models['Model-1'].sketches['__profile__'].geometry[4])
	mdb.models['Model-1'].sketches['__profile__'].ObliqueDimension(textPoint=(
		-0.00161435687914491, -0.00103188934735954), value=0.02, vertex1=
		mdb.models['Model-1'].sketches['__profile__'].vertices[0], vertex2=
		mdb.models['Model-1'].sketches['__profile__'].vertices[1])
	mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='Part-1', type=
		DEFORMABLE_BODY)
	mdb.models['Model-1'].parts['Part-1'].BaseWire(sketch=
		mdb.models['Model-1'].sketches['__profile__'])
	del mdb.models['Model-1'].sketches['__profile__']

	# Create Material
	mdb.models['Model-1'].Material(name='kapton')
	mdb.models['Model-1'].materials['kapton'].Elastic(table=((2500000000.0, 0.34), 
		))
		
	# Create Section	
	mdb.models['Model-1'].RectangularProfile(a=0.02, b=50e-06, name='Profile-1')
	mdb.models['Model-1'].BeamSection(consistentMassMatrix=False, integration=
		DURING_ANALYSIS, material='kapton', name='Beam', poissonRatio=0.0, profile=
		'Profile-1', temperatureVar=LINEAR)
	mdb.models['Model-1'].sections['Beam'].setValues(poissonRatio=0.0)
	mdb.models['Model-1'].parts['Part-1'].Set(edges=
		mdb.models['Model-1'].parts['Part-1'].edges.getSequenceFromMask(('[#1 ]', 
		), ), name='Beam')
		
	# Section Assignment	
	mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
		offsetField='', offsetType=MIDDLE_SURFACE, region=
		mdb.models['Model-1'].parts['Part-1'].sets['Beam'], sectionName='Beam', 
		thicknessAssignment=FROM_SECTION)
	mdb.models['Model-1'].parts['Part-1'].assignBeamSectionOrientation(method=
		N1_COSINES, n1=(0.0, 0.0, -1.0), region=Region(
		edges=mdb.models['Model-1'].parts['Part-1'].edges.getSequenceFromMask(
		mask=('[#1 ]', ), )))
		
	# Create Spring	
	mdb.models['Model-1'].parts['Part-1'].engineeringFeatures.SpringDashpotToGround(
		dashpotBehavior=OFF, dashpotCoefficient=0.0, dof=6, name='Spring', 
		orientation=None, region=Region(
		vertices=mdb.models['Model-1'].parts['Part-1'].vertices.getSequenceFromMask(
		mask=('[#1 ]', ), )), springBehavior=ON, springStiffness=1.2e-5)
		
	# Creat Sets	
	mdb.models['Model-1'].parts['Part-1'].Set(name='Left Support', vertices=
		mdb.models['Model-1'].parts['Part-1'].vertices.getSequenceFromMask((
		'[#1 ]', ), ))
	mdb.models['Model-1'].parts['Part-1'].Set(name='End Load', vertices=
		mdb.models['Model-1'].parts['Part-1'].vertices.getSequenceFromMask((
		'[#2 ]', ), ))
	mdb.models['Model-1'].parts['Part-1'].Set(name='Right Support', vertices=
		mdb.models['Model-1'].parts['Part-1'].vertices.getSequenceFromMask((
		'[#2 ]', ), ))
		
	# Create Steps	
	mdb.models['Model-1'].StaticStep(name='LoadApplication', previous='Initial')

	# Meshing
	mdb.models['Model-1'].parts['Part-1'].seedPart(deviationFactor=0.1, 
		minSizeFactor=0.1, size=M)
	mdb.models['Model-1'].parts['Part-1'].generateMesh()

	# Assembly
	mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
	mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-1-1', 
		part=mdb.models['Model-1'].parts['Part-1'])
		
	# BC	
	mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
		distributionType=UNIFORM, fieldName='', localCsys=None, name=
		'Pinned Support', region=
		mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].sets['Left Support']
		, u1=SET, u2=SET, ur3=UNSET)
		
	# End Load	
	mdb.models['Model-1'].ConcentratedForce(cf1=P, createStepName=
		'LoadApplication', distributionType=UNIFORM, field='', localCsys=None, 
		name='End Load', region=
		mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].sets['End Load'])
		
	# Create Job	
	mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
		explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
		memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, 
		multiprocessingMode=DEFAULT, name='PlainAnalysis', nodalOutputPrecision=
		SINGLE, numCpus=1, numGPUs=0, queue=None, resultsFormat=ODB, scratch='', 
		type=ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)
		
	# Submit job	
	mdb.jobs['PlainAnalysis'].submit(consistencyChecking=OFF)
	mdb.jobs['PlainAnalysis'].waitForCompletion() 

	# Output
	# execfile('Post_Processing.py')

	from abaqus import *
	from abaqusConstants import *
	session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=184.609375, 
		height=218.438873291016)
	session.viewports['Viewport: 1'].makeCurrent()
	session.viewports['Viewport: 1'].maximize()
	from caeModules import *
	from driverUtils import executeOnCaeStartup  

	a = mdb.models['Model-1'].rootAssembly
	session.viewports['Viewport: 1'].setValues(displayedObject=a)
	o3 = session.openOdb(
		name='N:\Project\ABAQUS\Results\Beam\Beam Mesh\PlainAnalysis.odb')
	#: Model: E:/Project/ABAQUS/Automated Python/PlainAnalysis.odb
	#: Number of Assemblies:         1
	#: Number of Assembly instances: 0
	#: Number of Part instances:     1
	#: Number of Meshes:             1
	#: Number of Element Sets:       4
	#: Number of Node Sets:          5
	#: Number of Steps:              1
	session.viewports['Viewport: 1'].setValues(displayedObject=o3)
	a = mdb.models['Model-1'].rootAssembly
	session.viewports['Viewport: 1'].setValues(displayedObject=a)
	session.viewports['Viewport: 1'].setValues(
		displayedObject=session.odbs['N:\Project\ABAQUS\Results\Beam\Beam Mesh\PlainAnalysis.odb'])
	session.viewports['Viewport: 1'].assemblyDisplay.setValues(
		optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)

	# Save Deformed Image 
	session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
		CONTOURS_ON_DEF, ))
	session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
		variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
		'Magnitude'), )
	session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
		deformationScaling=UNIFORM)
	session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
		uniformScaleFactor=1)	
	session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(
		compass=OFF)
	session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(title=OFF)	
	session.printToFile(fileName='Deformed Beam Mesh'+str(M)+'.tif', format=TIFF, canvasObjects=(
		session.viewports['Viewport: 1'], ))
	
	# Save Y-Deflection
	odb = session.odbs['N:\Project\ABAQUS\Results\Beam\Beam Mesh\PlainAnalysis.odb']
	session.writeFieldReport(fileName='abaqusMesh'+str(M)+'.txt', append=OFF, 
    sortItem='Node Label', odb=odb, step=0, frame=1, outputPosition=NODAL, 
    variable=(('U', NODAL, ((COMPONENT, 'U2'), )), ))
		
	odb.close()
	Mdb()


