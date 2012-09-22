#SPINE MODULE
import maya.cmds as mc
import frank

def addAttributes(parentNode):
	# METHOD TO ADD THE ATTRIBUTES NEEDED FOR THIS RIG MODULE
	mc.setAttr((frank.addString('cucu', parentNode)), 'CULO', type='string')

def buildRigGuides(parentNode):
	mc.select(cl = 1)
	jnt1 = mc.joint(p = [0,3,0], n = 'spine1_rigGuides')
	mc.joint(p = [0,4,0.1], n = 'spine2_rigGuides')
	mc.joint(p = [0,5,-0.1], n = 'spine3_rigGuides')
	mc.joint(p = [0,7,0], n = 'spine4_rigGuides')	
	mc.select(cl = 1)
	mc.parent(jnt1, parentNode)
	print 'SPINE RIG GUIDES BUILT'

def buildAnimRig():
	print 'SPINE RIG BUILT'
