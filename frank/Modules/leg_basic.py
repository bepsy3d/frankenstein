#LEG MODULE
import maya.cmds as mc
import frank

def addAttributes(parentNode):
	# METHOD TO ADD THE ATTRIBUTES NEEDED FOR THIS RIG MODULE
	mc.setAttr((frank.addString('cucu', parentNode)), 'CULO', type='string')

def buildRigGuides():
	mc.select(cl = 1)
	mc.joint(p = [0,3,0], n = 'L_arm1_rigGuides')
	mc.joint(p = [0,5,-1], n = 'L_arm2_rigGuides')
	mc.joint(p = [0,7,0], n = 'L_arm3_rigGuides')
	mc.select(cl = 1)
	print 'LEG RIG GUIDES BUILT'

def buildAnimRig():
	print 'LEG RIG BUILT'
