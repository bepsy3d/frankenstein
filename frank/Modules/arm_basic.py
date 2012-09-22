#ARM MODULE
import maya.cmds as mc
import frank

def addAttributes(parentNode):
	# METHOD TO ADD THE ATTRIBUTES NEEDED FOR THIS RIG MODULE
	mc.setAttr((frank.addString('cucu', parentNode)), 'CULO', type='string')
	mc.setAttr((frank.addString('cuau', parentNode)), 'CUO', type='string')


def buildRigGuides(parentNode):
	mc.select(cl = 1)
	jnt1 = mc.joint(p = [1,8,0], n = 'L_arm1_rigGuides')
	mc.joint(p = [3,8,-0.2], n = 'L_arm2_rigGuides')
	mc.joint(p = [5,8,0], n = 'L_arm3_rigGuides')
	mc.select(cl = 1)
	mc.parent(jnt1, parentNode)
	print 'ARM RIG GUIDES BUILT'
	

def buildAnimRig(parentNode):
	print 'ARM RIG BUILT'