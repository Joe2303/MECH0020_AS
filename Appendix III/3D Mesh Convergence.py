# -*- coding: mbcs -*-
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
import regionToolset

# Other Import
import numpy as np

# Change Work Directory
os.chdir(r"N:\Project\ABAQUS\Results\SingleCrease\Mesh 2")

#PLoad = np.arange(5e-6,5.05e-4,5e-6)
MS = np.around((np.linspace(0.01, 0.5, num=100)),10)

for M in MS:

	# Create Part 
	mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=2)
	mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(
		decimalPlaces=4)
	mdb.models['Model-1'].sketches['__profile__'].ConstructionLine(point1=(0.0, 
		0.002375), point2=(0.0, -0.00137499999627471))
	mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
		False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[2])
	mdb.models['Model-1'].sketches['__profile__'].ConstructionLine(point1=(0.0, 
		0.00113297230564058), point2=(0.003375, -0.00075))
	mdb.models['Model-1'].sketches['__profile__'].AngularDimension(line1=
		mdb.models['Model-1'].sketches['__profile__'].geometry[3], line2=
		mdb.models['Model-1'].sketches['__profile__'].geometry[2], textPoint=(
		0.0013867449015379, -0.000400120159611106), value=44.5)
	mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-0.002875, 0.001625)
		, point2=(0.001125, -0.002625))
	mdb.models['Model-1'].sketches['__profile__'].ParallelConstraint(entity1=
		mdb.models['Model-1'].sketches['__profile__'].geometry[4], entity2=
		mdb.models['Model-1'].sketches['__profile__'].geometry[3])
	mdb.models['Model-1'].sketches['__profile__'].ObliqueDimension(textPoint=(
		-0.002246611751616, -0.0010740072466433), value=2, vertex1=
		mdb.models['Model-1'].sketches['__profile__'].vertices[0], vertex2=
		mdb.models['Model-1'].sketches['__profile__'].vertices[1])
	mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Part-1', type=
		DEFORMABLE_BODY)
	mdb.models['Model-1'].parts['Part-1'].BaseShellExtrude(depth=2, sketch=
		mdb.models['Model-1'].sketches['__profile__'])
	del mdb.models['Model-1'].sketches['__profile__']

	# Create Material
	mdb.models['Model-1'].Material(name='kapton')
	mdb.models['Model-1'].materials['kapton'].Elastic(table=((250000.0, 0.34), 
		))
		
	# Create and Assign Section
	mdb.models['Model-1'].HomogeneousShellSection(idealization=NO_IDEALIZATION, 
		integrationRule=SIMPSON, material='kapton', name='PlateThickness', 
		nodalThicknessField='', numIntPts=5, poissonDefinition=DEFAULT, 
		preIntegrate=OFF, temperature=GRADIENT, thickness=0.005, thicknessField='', 
		thicknessModulus=None, thicknessType=UNIFORM, useDensity=OFF)
	mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
		offsetField='', offsetType=MIDDLE_SURFACE, region=Region(
		faces=mdb.models['Model-1'].parts['Part-1'].faces.getSequenceFromMask(
		mask=('[#1 ]', ), )), sectionName='PlateThickness', thicknessAssignment=
		FROM_SECTION)
		
	# Meshing
	mdb.models['Model-1'].parts['Part-1'].seedPart(deviationFactor=0.1, 
		minSizeFactor=0.1, size=M)
	mdb.models['Model-1'].parts['Part-1'].generateMesh()

	# Create Instance
	mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
	mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-1-1', 
		part=mdb.models['Model-1'].parts['Part-1'])	
		
	# Create Step
	mdb.models['Model-1'].StaticStep(name='Load Application', previous='Initial')

	# Create Support
	p1 = mdb.models['Model-1'].parts['Part-1']
	session.viewports['Viewport: 1'].setValues(displayedObject=p1)
	p = mdb.models['Model-1'].parts['Part-1']
	e = p.edges
	edges = e.getSequenceFromMask(mask=('[#2 ]', ), )
	p.Set(edges=edges, name='Left Edge')
	a = mdb.models['Model-1'].rootAssembly
	a.regenerate()
	session.viewports['Viewport: 1'].setValues(displayedObject=a)
	a = mdb.models['Model-1'].rootAssembly
	region = a.instances['Part-1-1'].sets['Left Edge']
	mdb.models['Model-1'].DisplacementBC(name='Pinned Support', 
		createStepName='Initial', region=region, u1=SET, u2=SET, u3=SET, ur1=SET, 
		ur2=SET, ur3=UNSET, amplitude=UNSET, distributionType=UNIFORM, 
		fieldName='', localCsys=None)
		
	# Create Reference Point for Load
	e1 = a.instances['Part-1-1'].edges
	a.DatumPointByOffset(point=a.instances['Part-1-1'].InterestingPoint(edge=e1[3], 
		rule=MIDDLE), vector=(0.5, 0.0, 0.0))
	a = mdb.models['Model-1'].rootAssembly
	d1 = a.datums
	a.ReferencePoint(point=d1[4])

	# Create Edge Load
	session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
		predefinedFields=ON, interactions=OFF, constraints=OFF, 
		engineeringFeatures=OFF)
	session.viewports['Viewport: 1'].assemblyDisplay.setValues(
		step='Load Application')
	e1 = a.instances['Part-1-1'].edges
	r1 = a.referencePoints
	a = mdb.models['Model-1'].rootAssembly
	s1 = a.instances['Part-1-1'].edges
	side1Edges1 = s1.getSequenceFromMask(mask=('[#8 ]', ), )
	region = regionToolset.Region(side1Edges=side1Edges1)
	mdb.models['Model-1'].ShellEdgeLoad(name='Edge Load', 
		createStepName='Load Application', region=region, magnitude=5e-5, 
		directionVector=(a.instances['Part-1-1'].InterestingPoint(edge=e1[3], 
		rule=MIDDLE), r1[5]), distributionType=UNIFORM, field='', localCsys=None, 
		traction=GENERAL, follower=ON, resultant=ON)
		
	# Coupling Constraint
	v1 = a.instances['Part-1-1'].vertices
	verts1 = v1.getSequenceFromMask(mask=('[#2 ]', ), )
	region1=regionToolset.Region(vertices=verts1)
	a = mdb.models['Model-1'].rootAssembly
	s1 = a.instances['Part-1-1'].edges
	side1Edges1 = s1.getSequenceFromMask(mask=('[#2 ]', ), )
	region2=regionToolset.Region(side1Edges=side1Edges1)
	mdb.models['Model-1'].Coupling(name='Couple', controlPoint=region1, 
		surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC, 
		localCsys=None, u1=OFF, u2=OFF, u3=OFF, ur1=OFF, ur2=OFF, ur3=ON)

	# Create Spring
	v1 = a.instances['Part-1-1'].vertices
	verts1 = v1.getSequenceFromMask(mask=('[#2 ]', ), )
	region=regionToolset.Region(vertices=verts1)
	mdb.models['Model-1'].rootAssembly.engineeringFeatures.SpringDashpotToGround(
		name='Spring', region=region, orientation=None, dof=6, springBehavior=ON, 
		springStiffness=0.0012, dashpotBehavior=OFF, dashpotCoefficient=0.0)


	# Create Job
	mdb.Job(name='MembraneAnalysis', model='Model-1', description='', 
		type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
		memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
		explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
		modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
		scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
		numGPUs=0)
	mdb.jobs['MembraneAnalysis'].setValues(numCpus=4, numDomains=4)
	
	# Submit job	
	mdb.jobs['MembraneAnalysis'].submit(consistencyChecking=OFF)
	mdb.jobs['MembraneAnalysis'].waitForCompletion() 	

	# Extracting Results
	o3 = session.openOdb(
		name='N:\Project\ABAQUS\Results\SingleCrease\Mesh 2\MembraneAnalysis.odb')
	#: Model: C:/Users/sajjaphnrj_j/Documents/Membrane/MembraneAnalysis.odb
	#: Number of Assemblies:         1
	#: Number of Assembly instances: 0
	#: Number of Part instances:     1
	#: Number of Meshes:             2
	#: Number of Element Sets:       3
	#: Number of Node Sets:          4
	#: Number of Steps:              1
	session.viewports['Viewport: 1'].setValues(displayedObject=o3)
	a = mdb.models['Model-1'].rootAssembly
	session.viewports['Viewport: 1'].setValues(displayedObject=a)
	session.viewports['Viewport: 1'].setValues(
		displayedObject=session.odbs['N:\Project\ABAQUS\Results\SingleCrease\Mesh 2\MembraneAnalysis.odb'])
	session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
		predefinedFields=OFF, connectors=OFF)
		
	# Save Deflection	
	odb = session.odbs['N:\Project\ABAQUS\Results\SingleCrease\Mesh 2\MembraneAnalysis.odb']
	session.writeFieldReport(fileName='abaqusMembraneMesh'+str(M)+'.txt', append=OFF, 
		sortItem='Node Label', odb=odb, step=0, frame=1, outputPosition=NODAL, 
		variable=(('U', NODAL, ((COMPONENT, 'U2'), )), ))
		
	# Save Image
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
	session.viewports['Viewport: 1'].view.fitView()
	session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
	session.printToFile(fileName='DeformedMembraneMesh'+str(M)+'.tif', format=TIFF, canvasObjects=(
		session.viewports['Viewport: 1'], ))	
		
	odb.close()
	Mdb()	