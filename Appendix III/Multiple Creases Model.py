 #-*- coding: mbcs -*-
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
os.chdir(r"C:\Users\sajjaphnrj_j\Documents\MultiCrease")

PLoad = np.arange(20.2e-4,20.2e-1,20e-6)

#odb.close()
#Mdb()    #FOR TESTING ONLY

for P in PLoad:

	# BEYOND THIS MUST BE TABBED
	# Variables
	MS = 0.06        # Mesh Size # 0.06 is the minimum amount that the simulation will work

	# Create Parts
	# Create Right Part 
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
	mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Right Part', type=
		DEFORMABLE_BODY)
	mdb.models['Model-1'].parts['Right Part'].BaseShellExtrude(depth=2, sketch=
		mdb.models['Model-1'].sketches['__profile__'])
	del mdb.models['Model-1'].sketches['__profile__']

	# Create Right Part 2
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
	mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Right Part 2', type=
		DEFORMABLE_BODY)
	mdb.models['Model-1'].parts['Right Part 2'].BaseShellExtrude(depth=2, sketch=
		mdb.models['Model-1'].sketches['__profile__'])
	del mdb.models['Model-1'].sketches['__profile__']


	# Create Left Part
	mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=2.0)
	mdb.models['Model-1'].sketches['__profile__'].ConstructionLine(point1=(0.0, 
		-0.0125), point2=(0.0, -0.0375000000465661))
	mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
		False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[2])
	mdb.models['Model-1'].sketches['__profile__'].ConstructionLine(point1=(0.0, 
		0.0), point2=(-0.0875, -0.0625))
	mdb.models['Model-1'].sketches['__profile__'].AngularDimension(line1=
		mdb.models['Model-1'].sketches['__profile__'].geometry[3], line2=
		mdb.models['Model-1'].sketches['__profile__'].geometry[2], textPoint=(
		-0.0451008677482605, -0.175631746649742), value=44.5)
	mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-0.2, 0.15), point2=
		(-0.3125, 0.025))
	mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-0.3125, 0.025), 
		point2=(-0.290415614843369, 0.025))
	mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
		addUndoState=False, entity=
		mdb.models['Model-1'].sketches['__profile__'].geometry[5])
	mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
		mdb.models['Model-1'].sketches['__profile__'].geometry[5], ))
	mdb.models['Model-1'].sketches['__profile__'].ParallelConstraint(entity1=
		mdb.models['Model-1'].sketches['__profile__'].geometry[4], entity2=
		mdb.models['Model-1'].sketches['__profile__'].geometry[3])
	mdb.models['Model-1'].sketches['__profile__'].ObliqueDimension(textPoint=(
		-0.300531685352325, 0.0753911137580872), value=2.0, vertex1=
		mdb.models['Model-1'].sketches['__profile__'].vertices[0], vertex2=
		mdb.models['Model-1'].sketches['__profile__'].vertices[1])
	mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Left Part', type=
		DEFORMABLE_BODY)
	mdb.models['Model-1'].parts['Left Part'].BaseShellExtrude(depth=2.0, sketch=
		mdb.models['Model-1'].sketches['__profile__'])
	del mdb.models['Model-1'].sketches['__profile__']


	# Create Left Part 2
	mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=2.0)
	mdb.models['Model-1'].sketches['__profile__'].ConstructionLine(point1=(0.0, 
		-0.0125), point2=(0.0, -0.0375000000465661))
	mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
		False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[2])
	mdb.models['Model-1'].sketches['__profile__'].ConstructionLine(point1=(0.0, 
		0.0), point2=(-0.0875, -0.0625))
	mdb.models['Model-1'].sketches['__profile__'].AngularDimension(line1=
		mdb.models['Model-1'].sketches['__profile__'].geometry[3], line2=
		mdb.models['Model-1'].sketches['__profile__'].geometry[2], textPoint=(
		-0.0451008677482605, -0.175631746649742), value=44.5)
	mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-0.2, 0.15), point2=
		(-0.3125, 0.025))
	mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-0.3125, 0.025), 
		point2=(-0.290415614843369, 0.025))
	mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
		addUndoState=False, entity=
		mdb.models['Model-1'].sketches['__profile__'].geometry[5])
	mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
		mdb.models['Model-1'].sketches['__profile__'].geometry[5], ))
	mdb.models['Model-1'].sketches['__profile__'].ParallelConstraint(entity1=
		mdb.models['Model-1'].sketches['__profile__'].geometry[4], entity2=
		mdb.models['Model-1'].sketches['__profile__'].geometry[3])
	mdb.models['Model-1'].sketches['__profile__'].ObliqueDimension(textPoint=(
		-0.300531685352325, 0.0753911137580872), value=2.0, vertex1=
		mdb.models['Model-1'].sketches['__profile__'].vertices[0], vertex2=
		mdb.models['Model-1'].sketches['__profile__'].vertices[1])
	mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Left Part 2', type=
		DEFORMABLE_BODY)
	mdb.models['Model-1'].parts['Left Part 2'].BaseShellExtrude(depth=2.0, sketch=
		mdb.models['Model-1'].sketches['__profile__'])
	del mdb.models['Model-1'].sketches['__profile__']


	# Materials
	# Create
	mdb.models['Model-1'].Material(name='kapton')
	mdb.models['Model-1'].materials['kapton'].Elastic(table=((250000.0, 0.34), ))
	mdb.models['Model-1'].HomogeneousShellSection(idealization=NO_IDEALIZATION, 
		integrationRule=SIMPSON, material='kapton', name='PlateThickness', 
		nodalThicknessField='', numIntPts=5, poissonDefinition=DEFAULT, 
		preIntegrate=OFF, temperature=GRADIENT, thickness=0.005, thicknessField='', 
		thicknessModulus=None, thicknessType=UNIFORM, useDensity=OFF)	
		
	#Assign
	mdb.models['Model-1'].parts['Right Part'].SectionAssignment(offset=0.0, 
		offsetField='', offsetType=MIDDLE_SURFACE, region=Region(
		faces=mdb.models['Model-1'].parts['Right Part'].faces.getSequenceFromMask(
		mask=('[#1 ]', ), )), sectionName='PlateThickness', thicknessAssignment=
		FROM_SECTION)
	mdb.models['Model-1'].parts['Right Part 2'].SectionAssignment(offset=0.0, 
		offsetField='', offsetType=MIDDLE_SURFACE, region=Region(
		faces=mdb.models['Model-1'].parts['Right Part 2'].faces.getSequenceFromMask(
		mask=('[#1 ]', ), )), sectionName='PlateThickness', thicknessAssignment=
		FROM_SECTION)	
	mdb.models['Model-1'].parts['Left Part'].SectionAssignment(offset=0.0, 
		offsetField='', offsetType=MIDDLE_SURFACE, region=Region(
		faces=mdb.models['Model-1'].parts['Right Part'].faces.getSequenceFromMask(
		mask=('[#1 ]', ), )), sectionName='PlateThickness', thicknessAssignment=
		FROM_SECTION)
	mdb.models['Model-1'].parts['Left Part 2'].SectionAssignment(offset=0.0, 
		offsetField='', offsetType=MIDDLE_SURFACE, region=Region(
		faces=mdb.models['Model-1'].parts['Left Part 2'].faces.getSequenceFromMask(
		mask=('[#1 ]', ), )), sectionName='PlateThickness', thicknessAssignment=
		FROM_SECTION)	
		
	# Meshing
	mdb.models['Model-1'].parts['Right Part'].seedPart(deviationFactor=0.1, 
		minSizeFactor=0.1, size=MS)
	mdb.models['Model-1'].parts['Right Part'].generateMesh()
	mdb.models['Model-1'].parts['Right Part 2'].seedPart(deviationFactor=0.1, 
		minSizeFactor=0.1, size=MS)
	mdb.models['Model-1'].parts['Right Part 2'].generateMesh()
	mdb.models['Model-1'].parts['Left Part'].seedPart(deviationFactor=0.1, 
		minSizeFactor=0.1, size=MS)
	mdb.models['Model-1'].parts['Left Part'].generateMesh()
	mdb.models['Model-1'].parts['Left Part 2'].seedPart(deviationFactor=0.1, 
		minSizeFactor=0.1, size=MS)
	mdb.models['Model-1'].parts['Left Part 2'].generateMesh()

	# Assembly
	# Instances
	mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
	mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Left Part-1', 
		part=mdb.models['Model-1'].parts['Left Part'])
	mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Right Part-1', 
		part=mdb.models['Model-1'].parts['Right Part'])
	mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Left Part-2', 
		part=mdb.models['Model-1'].parts['Left Part 2'])
	mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Right Part-2', 
		part=mdb.models['Model-1'].parts['Right Part 2'])

	# Offset
	mdb.models['Model-1'].rootAssembly.instances['Left Part-2'].translate(vector=(1.54200040608827, 0.0, 0.0))
	mdb.models['Model-1'].rootAssembly.instances['Right Part-1'].translate(vector=(4.16946291626469, 0.0, 0.0))
	mdb.models['Model-1'].rootAssembly.instances['Right Part-2'].translate(vector=(5.71146329772436, 0.0, 0.0))		

	# Step
	mdb.models['Model-1'].StaticStep(name='LoadApp', previous='Initial')

	# Create Middle Reference Points
	mdb.models['Model-1'].rootAssembly.ReferencePoint(point=
		mdb.models['Model-1'].rootAssembly.instances['Left Part-1'].InterestingPoint(
		mdb.models['Model-1'].rootAssembly.instances['Left Part-1'].edges[3], 
		MIDDLE))
	mdb.models['Model-1'].rootAssembly.ReferencePoint(point=
		mdb.models['Model-1'].rootAssembly.instances['Left Part-1'].InterestingPoint(
		mdb.models['Model-1'].rootAssembly.instances['Left Part-1'].edges[1], 
		MIDDLE))

	mdb.models['Model-1'].rootAssembly.ReferencePoint(point=
		mdb.models['Model-1'].rootAssembly.instances['Left Part-2'].InterestingPoint(
		mdb.models['Model-1'].rootAssembly.instances['Left Part-2'].edges[3], 
		MIDDLE))
	mdb.models['Model-1'].rootAssembly.ReferencePoint(point=
		mdb.models['Model-1'].rootAssembly.instances['Left Part-2'].InterestingPoint(
		mdb.models['Model-1'].rootAssembly.instances['Left Part-2'].edges[1], 
		MIDDLE))	

	mdb.models['Model-1'].rootAssembly.ReferencePoint(point=
		mdb.models['Model-1'].rootAssembly.instances['Right Part-1'].InterestingPoint(
		mdb.models['Model-1'].rootAssembly.instances['Right Part-1'].edges[3], 
		MIDDLE))
	mdb.models['Model-1'].rootAssembly.ReferencePoint(point=
		mdb.models['Model-1'].rootAssembly.instances['Right Part-1'].InterestingPoint(
		mdb.models['Model-1'].rootAssembly.instances['Right Part-1'].edges[1], 
		MIDDLE))

	mdb.models['Model-1'].rootAssembly.ReferencePoint(point=
		mdb.models['Model-1'].rootAssembly.instances['Right Part-2'].InterestingPoint(
		mdb.models['Model-1'].rootAssembly.instances['Right Part-2'].edges[3], 
		MIDDLE))
	mdb.models['Model-1'].rootAssembly.ReferencePoint(point=
		mdb.models['Model-1'].rootAssembly.instances['Right Part-2'].InterestingPoint(
		mdb.models['Model-1'].rootAssembly.instances['Right Part-2'].edges[1], 
		MIDDLE))		
		
	# Coupling
	mdb.models['Model-1'].Coupling(controlPoint=Region(referencePoints=(
		mdb.models['Model-1'].rootAssembly.referencePoints[10], )), couplingType=
		STRUCTURAL, influenceRadius=WHOLE_SURFACE, localCsys=None, name=
		'LP1-1 Coupling', surface=Region(
		side1Edges=mdb.models['Model-1'].rootAssembly.instances['Left Part-1'].edges.getSequenceFromMask(
		mask=('[#8 ]', ), )), u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON, 
		weightingMethod=UNIFORM)
	mdb.models['Model-1'].Coupling(controlPoint=Region(referencePoints=(
		mdb.models['Model-1'].rootAssembly.referencePoints[11], )), couplingType=
		STRUCTURAL, influenceRadius=WHOLE_SURFACE, localCsys=None, name=
		'LP1-2 Coupling', surface=Region(
		side1Edges=mdb.models['Model-1'].rootAssembly.instances['Left Part-1'].edges.getSequenceFromMask(
		mask=('[#2 ]', ), )), u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON, 
		weightingMethod=UNIFORM)	
		
	mdb.models['Model-1'].Coupling(controlPoint=Region(referencePoints=(
		mdb.models['Model-1'].rootAssembly.referencePoints[12], )), couplingType=
		STRUCTURAL, influenceRadius=WHOLE_SURFACE, localCsys=None, name=
		'LP2-1 Coupling', surface=Region(
		side1Edges=mdb.models['Model-1'].rootAssembly.instances['Left Part-2'].edges.getSequenceFromMask(
		mask=('[#8 ]', ), )), u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON, 
		weightingMethod=UNIFORM)
	mdb.models['Model-1'].Coupling(controlPoint=Region(referencePoints=(
		mdb.models['Model-1'].rootAssembly.referencePoints[13], )), couplingType=
		STRUCTURAL, influenceRadius=WHOLE_SURFACE, localCsys=None, name=
		'LP2-2 Coupling', surface=Region(
		side1Edges=mdb.models['Model-1'].rootAssembly.instances['Left Part-2'].edges.getSequenceFromMask(
		mask=('[#2 ]', ), )), u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON, 
		weightingMethod=UNIFORM)

	mdb.models['Model-1'].Coupling(controlPoint=Region(referencePoints=(
		mdb.models['Model-1'].rootAssembly.referencePoints[14], )), couplingType=
		STRUCTURAL, influenceRadius=WHOLE_SURFACE, localCsys=None, name=
		'RP1-1 Coupling', surface=Region(
		side1Edges=mdb.models['Model-1'].rootAssembly.instances['Right Part-1'].edges.getSequenceFromMask(
		mask=('[#8 ]', ), )), u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON, 
		weightingMethod=UNIFORM)
	mdb.models['Model-1'].Coupling(controlPoint=Region(referencePoints=(
		mdb.models['Model-1'].rootAssembly.referencePoints[15], )), couplingType=
		STRUCTURAL, influenceRadius=WHOLE_SURFACE, localCsys=None, name=
		'RP1-2 Coupling', surface=Region(
		side1Edges=mdb.models['Model-1'].rootAssembly.instances['Right Part-1'].edges.getSequenceFromMask(
		mask=('[#2 ]', ), )), u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON, 
		weightingMethod=UNIFORM)	

	mdb.models['Model-1'].Coupling(controlPoint=Region(referencePoints=(
		mdb.models['Model-1'].rootAssembly.referencePoints[16], )), couplingType=
		STRUCTURAL, influenceRadius=WHOLE_SURFACE, localCsys=None, name=
		'RP2-1 Coupling', surface=Region(
		side1Edges=mdb.models['Model-1'].rootAssembly.instances['Right Part-2'].edges.getSequenceFromMask(
		mask=('[#8 ]', ), )), u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON, 
		weightingMethod=UNIFORM)
	mdb.models['Model-1'].Coupling(controlPoint=Region(referencePoints=(
		mdb.models['Model-1'].rootAssembly.referencePoints[17], )), couplingType=
		STRUCTURAL, influenceRadius=WHOLE_SURFACE, localCsys=None, name=
		'RP2-2 Coupling', surface=Region(
		side1Edges=mdb.models['Model-1'].rootAssembly.instances['Right Part-2'].edges.getSequenceFromMask(
		mask=('[#2 ]', ), )), u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON, 
		weightingMethod=UNIFORM)		
			
	# Translate
	mdb.models['Model-1'].rootAssembly.translate(instanceList=('Right Part-1', ), 
		vector=(-1.677182, 0.030108, 0.0))	
	mdb.models['Model-1'].rootAssembly.translate(instanceList=('Left Part-2', ), 
		vector=(1.271637, 0.0, 0.0))	
	mdb.models['Model-1'].rootAssembly.translate(instanceList=('Right Part-2', ), 
		vector=(-0.405545, 0.030108, 0.0))		
		
	# Constraint and Connector
	# Tie Constraint
	mdb.models['Model-1'].Tie(adjust=ON, master=Region(
		side1Edges=mdb.models['Model-1'].rootAssembly.instances['Left Part-1'].edges.getSequenceFromMask(
		mask=('[#2 ]', ), )), name='Tie LP1-RP1', positionToleranceMethod=COMPUTED, 
		slave=Region(
		side1Edges=mdb.models['Model-1'].rootAssembly.instances['Right Part-1'].edges.getSequenceFromMask(
		mask=('[#2 ]', ), )), thickness=ON, tieRotations=ON)
		
	mdb.models['Model-1'].Tie(adjust=ON, master=Region(
		side1Edges=mdb.models['Model-1'].rootAssembly.instances['Left Part-2'].edges.getSequenceFromMask(
		mask=('[#8 ]', ), )), name='Tie RP1-LP2', positionToleranceMethod=COMPUTED, 
		slave=Region(
		side1Edges=mdb.models['Model-1'].rootAssembly.instances['Right Part-1'].edges.getSequenceFromMask(
		mask=('[#8 ]', ), )), thickness=ON, tieRotations=ON)	
		
	mdb.models['Model-1'].Tie(adjust=ON, master=Region(
		side1Edges=mdb.models['Model-1'].rootAssembly.instances['Left Part-2'].edges.getSequenceFromMask(
		mask=('[#2 ]', ), )), name='Tie LP2-RP2', positionToleranceMethod=COMPUTED, 
		slave=Region(
		side1Edges=mdb.models['Model-1'].rootAssembly.instances['Right Part-2'].edges.getSequenceFromMask(
		mask=('[#2 ]', ), )), thickness=ON, tieRotations=ON)	
		
	# Revolute Connector
	# Create Section	
	mdb.models['Model-1'].ConnectorSection(name='REVOLUTE Section', rotationalType=
		REVOLUTE)
	mdb.models['Model-1'].sections['REVOLUTE Section'].setValues(behaviorOptions=(
		ConnectorElasticity(table=((0.0012, ), ), independentComponents=(), 
		components=(4, )), ))
	mdb.models['Model-1'].sections['REVOLUTE Section'].behaviorOptions[0].ConnectorOptions(
		)	
		
	# Create Datum for Revolute
	mdb.models['Model-1'].rootAssembly.DatumCsysByThreePoints(coordSysType=
		CARTESIAN, name='REVOLUTE Datum', origin=
		mdb.models['Model-1'].rootAssembly.referencePoints[11], point1=
		mdb.models['Model-1'].rootAssembly.instances['Left Part-1'].vertices[2], 
		point2=
		mdb.models['Model-1'].rootAssembly.instances['Right Part-1'].vertices[2])	
		
	# Create Wires
	mdb.models['Model-1'].rootAssembly.WirePolyLine(points=((
		mdb.models['Model-1'].rootAssembly.referencePoints[11], mdb.models['Model-1'].rootAssembly.
		referencePoints[15]), ), mergeType=IMPRINT, meshable=OFF)
	mdb.models['Model-1'].rootAssembly.Set(edges=mdb.models['Model-1'].rootAssembly.edges.
		getSequenceFromMask(mask=('[#1 ]', ), ), name='Wire LP1-RP1')	

	mdb.models['Model-1'].rootAssembly.WirePolyLine(points=((
		mdb.models['Model-1'].rootAssembly.referencePoints[13], mdb.models['Model-1'].rootAssembly.
		referencePoints[17]), ), mergeType=IMPRINT, meshable=OFF)
	mdb.models['Model-1'].rootAssembly.Set(edges=mdb.models['Model-1'].rootAssembly.edges.
		getSequenceFromMask(mask=('[#1 ]', ), ), name='Wire LP2-RP2')	

	# Assign Sections
	a = mdb.models['Model-1'].rootAssembly
	region=a.sets['Wire LP1-RP1']
	datum1 = mdb.models['Model-1'].rootAssembly.datums[40]
	csa = a.SectionAssignment(sectionName='REVOLUTE Section', region=region)
	a.ConnectorOrientation(region=csa.getSet(), localCsys1=datum1)

	a = mdb.models['Model-1'].rootAssembly
	region=a.sets['Wire LP2-RP2']
	datum1 = mdb.models['Model-1'].rootAssembly.datums[40]
	csa = a.SectionAssignment(sectionName='REVOLUTE Section', region=region)
	a.ConnectorOrientation(region=csa.getSet(), localCsys1=datum1)

	a = mdb.models['Model-1'].rootAssembly
	r11 = a.referencePoints
	wire = a.WirePolyLine(points=((r11[14], r11[12]), ), mergeType=IMPRINT, 
		meshable=False)
	oldName = wire.name
	mdb.models['Model-1'].rootAssembly.features.changeKey(fromName=oldName, 
		toName='Wire-4')
	a = mdb.models['Model-1'].rootAssembly
	e1 = a.edges
	edges1 = e1.getSequenceFromMask(mask=('[#1 ]', ), )
	a.Set(edges=edges1, name='Wire LP2-RP1')
	region = mdb.models['Model-1'].rootAssembly.sets['Wire LP2-RP1']
	csa = a.SectionAssignment(sectionName='REVOLUTE Section', region=region)
	#: The section "REVOLUTE Section" has been assigned to 1 wire or attachment line.
	dtmid1 = mdb.models['Model-1'].rootAssembly.datums[40]
	a.ConnectorOrientation(region=csa.getSet(), localCsys1=dtmid1)
		
	# Pinned Support 
	# Left-End
	mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
		distributionType=UNIFORM, fieldName='', localCsys=None, name='Left End Pinned', 
		region=Region(
		edges=mdb.models['Model-1'].rootAssembly.instances['Left Part-1'].edges.getSequenceFromMask(
		mask=('[#8 ]', ), )), u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=UNSET)
		
	# Right-End 
	mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
		distributionType=UNIFORM, fieldName='', localCsys=None, name='Right End Roller', 
		region=Region(
		edges=mdb.models['Model-1'].rootAssembly.instances['Right Part-2'].edges.getSequenceFromMask(
		mask=('[#8 ]', ), )), u1=UNSET, u2=SET, u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET)	

	# Load
	# Create Reference Point for Shell Load
	mdb.models['Model-1'].rootAssembly.DatumPointByOffset(point=
		mdb.models['Model-1'].rootAssembly.instances['Right Part-2'].InterestingPoint(
		mdb.models['Model-1'].rootAssembly.instances['Right Part-2'].edges[3], 
		MIDDLE), vector=(0.5, 0.0, 0.0))	
	mdb.models['Model-1'].rootAssembly.ReferencePoint(point=
		mdb.models['Model-1'].rootAssembly.datums[49])	
		
	# Create Load
	mdb.models['Model-1'].ShellEdgeLoad(createStepName='LoadApp', directionVector=(
		mdb.models['Model-1'].rootAssembly.instances['Right Part-2'].InterestingPoint(
		mdb.models['Model-1'].rootAssembly.instances['Right Part-2'].edges[3], 
		MIDDLE), mdb.models['Model-1'].rootAssembly.referencePoints[50]), 
		distributionType=UNIFORM, field='', localCsys=None, magnitude=P, name=
		'End Load', region=Region(
		side1Edges=mdb.models['Model-1'].rootAssembly.instances['Right Part-2'].edges.getSequenceFromMask(
		mask=('[#8 ]', ), )), resultant=ON, traction=GENERAL)	
		
		
	# MIDDLE SUPPORT - Assumption
	mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
		distributionType=UNIFORM, fieldName='', localCsys=None, name=
		'Middle Roller', region=Region(
		edges=mdb.models['Model-1'].rootAssembly.instances['Right Part-1'].edges.getSequenceFromMask(
		mask=('[#8 ]', ), )+\
		mdb.models['Model-1'].rootAssembly.instances['Left Part-2'].edges.getSequenceFromMask(
		mask=('[#8 ]', ), )), u1=UNSET, u2=SET, u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=
		UNSET)	
		
	# Job
	# Create
	# Create Job
	mdb.Job(name='MultiCreasesAnalysis', model='Model-1', description='', 
		type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
		memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
		explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
		modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
		scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
		numGPUs=0)	
	mdb.jobs['MultiCreasesAnalysis'].setValues(numCpus=4, numDomains=4)	

	# Submit
	# Submit job	
	mdb.jobs['MultiCreasesAnalysis'].submit(consistencyChecking=OFF)
	mdb.jobs['MultiCreasesAnalysis'].waitForCompletion()

	# Extracting Results
	o3 = session.openOdb(
		name='C:\Users\sajjaphnrj_j\Documents\MultiCrease\MultiCreasesAnalysis.odb')
	#: Model: C:\Users\sajjaphnrj_j\Documents\MultiCrease\MultiCreasesAnalysis.odb
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
		displayedObject=session.odbs['C:\Users\sajjaphnrj_j\Documents\MultiCrease\MultiCreasesAnalysis.odb'])
	session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
		predefinedFields=OFF, connectors=OFF)
		
	# Save Deflection	
	odb = session.odbs['C:\Users\sajjaphnrj_j\Documents\MultiCrease\MultiCreasesAnalysis.odb']
	session.writeFieldReport(fileName='abaqusMCMembrane'+str(P)+'.txt', append=OFF, 
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
	session.printToFile(fileName='DeformedMCMembrane'+str(P)+'.tif', format=TIFF, canvasObjects=(
		session.viewports['Viewport: 1'], )) 	

	odb.close()
	Mdb()  	