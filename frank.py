import maya.cmds as mc
import sys

def launch():
	if mc.objExists('frank'):	
		name = getRigName()	    
		buildUI(name)	
		appendFolder()	 
	else:
		createFrank()    		       		
		buildUI('Name')
		appendFolder()

       
def createFrank():
    # creating the Frank Node
	mc.group(em = 1, n = 'frank')
	mc.group(em = 1, n = 'modules')  
	mc.group(em = 1, n = 'base')  
	mc.parent('modules', 'frank')  
	mc.parent('base', 'modules')  
    
	# frank attributes
	obj = 'frank'
	mc.setAttr((addString('fileName',obj)), 'untitled', type = 'string')
		
	# frank attributes
	obj = 'frank'
	addString('Name',obj)

	# attributes
	obj = 'base'
	mc.setAttr((addString('Name',obj)), obj, type = 'string')


def buildUI(name):
	"Builds the Maya Frankie UI"
	title = (mc.getAttr('frank.fileName'))+' '+(buildUI.__doc__)
	if mc.window('FrankUI', ex = 1): mc.deleteUI('FrankUI')
	mc.window('FrankUI', title = 'Frank: '+title, menuBar = 1)
	mc.menu(label = 'File')
	mc.menuItem (label = 'New', c=  "frank.new()")	
	mc.menuItem (label = 'Open Session...', c=  "frank.openSession()")		
	mc.menuItem (label = 'Save Session...', c=  "frank.saveSession()")			
	mc.menuItem (label = 'Save Session As...', c=  "frank.saveSessionAs()")	
	
	mc.menu(label = 'Module')
	mc.menuItem (label = 'Add New Module', c=  "frank.newModule()")	
	mc.menu(label = 'Edit')
	mc.menuItem (label = 'Reset Settings', c=  "frank.reset()")

	mc.columnLayout('TOP')

	# NAME
	mc.textFieldGrp('nameUI',
	                label = 'Name',
	                text = name,
	                cc = "mc.setAttr ('frank.Name',mc.textFieldGrp('nameUI',text = 1, q=1),type = 'string')")                              
	
	mc.columnLayout('TabLayout')
	tabs = mc.tabLayout('Tab',innerMarginWidth=5, innerMarginHeight=5) 
	#MODULES
	mc.columnLayout('Modules')
	mc.rowColumnLayout(nc = 2, cw =[(1,70),(2,70)])
	mc.button(label = 'Save Pose', bgc = [.8,.3,.3], c = "frank.savePose()")
	mc.button(label = 'Load Pose', c = "frank.loadPose()")
	mc.checkBox('loadPoseChk',label = 'Auto Pose', value = 1 )
	
	mc.rowColumnLayout('ModulesSplit', w = 700, nc= 2, p = 'Modules')
	#LEFT PART
	mc.textScrollList('ModuleScrollList',numberOfRows=8, allowMultiSelection=True,
	                        append=getModules(),
	                        selectIndexedItem=1, 
	                        showIndexedItem=4, 
	                        sc ='frank.UIupdateModAttr()')
		                        	
	#RIGHT
	mc.columnLayout('ModAttr')
	mc.setParent('..')
	#LEFT UNDER THE SCROLL LAYOUT
	mc.rowColumnLayout('buttons', nc = 2)
	mc.button(label = 'Add Module..', w = 150, c = 'frank.newModule()')
	mc.button(label = 'Delete Module..', w = 150, c = 'frank.deleteModule()')		
	mc.setParent('..') 
	mc.setParent('..')	
	mc.setParent('..')	

	
	#BUILD RIG
	mc.rowColumnLayout('Build Rig')	
	UIupdateModAttr()
		
	#BUTTON TO CREATE THE RIG GUIDE(S)
	mc.button(label = 'Build rig Guides', w = 700, c = "frank.buildRigGuidesButton()", p = 'Modules' )
	
	mc.showWindow('FrankUI')


def getRigName():
    name= mc.getAttr('frank.Name')
    return name	

	
def getModules():
    modules = mc.listRelatives('modules', ad = 1)
    return modules


def UIgetItemSelected():	
	if mc.textScrollList('ModuleScrollList', ex = 1):
		i = mc.textScrollList('ModuleScrollList', q = 1, sii = 1)
	return i   	    

        
def UIupdateModAttr():
	i = UIgetItemSelected()[0]    
	module = getModules()[i-1]
	if mc.rowColumnLayout('CurrMod', ex = 1):
	    mc.deleteUI('CurrMod')
	mc.rowColumnLayout('CurrMod', p = 'ModAttr', columnAttach =  [1,'both',0])
	
	# ATTRIBUTES FOR THE MODULE
	mc.text('Attributes for "'+ module+ '" module',p = 'CurrMod')
	mc.separator( height=8, style='out' )
	buildModAttr(module)
	

def buildModAttr(module):	
	attrs = mc.listAttr(module, ud = 1)
	if mc.objExists(module+'.pose'):attrs.remove('pose')

	modulePathExists = 0 
	nameExists = 0		
	
	for attr in attrs:
		attrType = mc.getAttr(module+'.'+attr,type = 1)
		value = mc.getAttr(module+'.'+attr)

		if attr == 'Module_Path':
			mc.textFieldButtonGrp(attr, cl3 = ['left','left','left'],  cw3 = [100,200,100],  label=attr, text=value, buttonLabel='Browse',
			cc = "mc.setAttr('"+module+"."+attr+"',mc.textFieldGrp('"+attr+"',text = 1, q=1),type = 'string')",
			bc = "mc.textFieldButtonGrp('"+attr+"', e = 1, text = (mc.fileDialog2(fileMode=1, caption='Select module File')[0]));mc.setAttr('"+module+"."+attr+"',mc.textFieldGrp('"+attr+"',text = 1, q=1),type = 'string')")								
			modulePathExists = 1
		if attr == 'Name':				
			mc.textFieldGrp(attr, cal = [1,'left'], label = attr, text = value,
			cc = "mc.setAttr('"+module+"."+attr+"',mc.textFieldGrp('"+attr+"',text = 1, q=1),type = 'string')")  
			nameExists = 1
	# NOW THE MODULE CUSTOM ATTRIBUTE
	# REMOVING THE NAME AND MODULE PATH FROM THE attrs VARIABLE LIST, TO OPERATE ONLY ON MODULE CUSTOM ATTRIBUTES
	mc.separator()	
	if modulePathExists == 1: 
		attrs.remove('Module_Path')
	if nameExists == 1: 
		attrs.remove('Name')
	

def addString(attr, obj):
    mc.addAttr (obj, ln = attr,  dt = 'string')
    mc.setAttr (obj+'.'+attr , e =1,keyable = 1) 
    return obj+'.'+attr
    

def addVector(attr, obj):
    three = ['X','Y','Z']
    mc.addAttr (obj ,ln = attr,  at = 'double3')
    for c in three :
        mc.addAttr (obj ,ln = attr+c,  at = 'double', p = attr)
	return obj+'.'+attr


def appendFolder():
	
	# Method to import all the path for the modules created	
	modules = getModules()
	for module in modules:
		if mc.objExists(module+'.Module_Path'):
			path = mc.getAttr(module+'.Module_Path')
			pathSplittedExtension = path.split('.')[0]
			pathSplitted =pathSplittedExtension.split('/')
			#GET SCRIPT NAME (without extension)
			moduleScript=pathSplitted[(len(pathSplitted)-1)]
			#GET FOLDER NAME
			moduleFolder=pathSplittedExtension.replace('/'+moduleScript,'')
			moduleFolder = moduleFolder.replace('/','\\')
			#print '\nAdding Path ................. ' +moduleFolder
			sys.path.append( moduleFolder )
	

def deleteModule():
	indexToDelete = UIgetItemSelected()
	modToDelete = []
	rigGuideToDelete = []
	modToDeleteString = ''
	for i in indexToDelete:
		if not getModules()[i-1] == 'base':
			modToDelete.append(getModules()[i-1])
			# DELETE THE GROUP OF THE RIG GUIDE IF EXISTS	
			if mc.objExists(getModules()[i-1]+'RigGuide'):
				mc.delete(getModules()[i-1]+'RigGuide')
			modToDeleteString = modToDeleteString+', '+(getModules()[i-1])	
	if not len(modToDelete)==0:
		result = mc.confirmDialog( title='Delete Module', message='Delete module(s) '+modToDeleteString+'?', button=['Yes','No'], defaultButton='Yes', cancelButton='No', dismissString='No' )
		if result == 'Yes':			
			mc.delete(modToDelete)
			launch()
	else: mc.confirmDialog(title = 'FrankUI', message = "Can't delete base module.", button = ['OK'])							
		

def newModule():
	# MODULE NAME
	result = mc.promptDialog(
	                title='New Module Name',
	                message='Enter Name:',
	                button=['OK', 'Cancel'],
	                defaultButton='OK',
	                cancelButton='Cancel',
	                dismissString='Cancel')
	
	if result == 'OK':
	        name = mc.promptDialog(query=True, text=True)
	else: return
	        
	filename = mc.fileDialog2(fileMode=1, caption="Select module File")[0]	        	
	
	modGrp = mc.group(em = 1, n = name)
	mc.parent(modGrp, 'modules') 
	
	mc.setAttr((addString('Name',modGrp)), name, type = "string")
	mc.setAttr((addString('Module_Path',modGrp)), filename, type = "string")	
	# GET THE SCRIPT OF THE MODULE
	print getModuleScript(name)
				
	launch()
	

def getSelectedModules():
	selected = []
	selected_indices = UIgetItemSelected()
	modules = getModules()
	#print "Indices:"
	#print selected_indices
	#print "Modules:"
	#print modules
	for i in selected_indices:
		selected.append( modules[i-1] )
	return selected	
	

def getModuleScript(module):
	if mc.objExists(module+'.Module_Path'):
		path = mc.getAttr(module+'.Module_Path')
		pathSplittedExtension = path.split('.')[0]
		pathSplitted =pathSplittedExtension.split('/')
		#GET SCRIPT NAME (without extension)
		moduleScript=pathSplitted[(len(pathSplitted)-1)]	
		#print moduleScript
		return moduleScript	
	

def buildRigGuidesButton():
#	if not mc.objExists('rigGuidesGrp'):		
#		mc.group(em =1, n = 'rigGuidesGrp')		
	modules = getSelectedModules()	
	reset()	
	for mod in modules:	
		if mc.objExists(mod+'RigGuide'):
			mc.delete(mod+'RigGuide')
		parentNode = mc.group(em =1, n = mod+'RigGuide')#, p = 'rigGuidesGrp')			
		if mod == 'base':
			baseBuildRigGuides()
		else:			
			moduleScript= getModuleScript(mod)
			module = __import__(moduleScript)
			module = reload(module)
			# RUNNING THE METHOD TO BUILD THE RIG GUIDES
			module.buildRigGuides(parentNode)
			# RUNNING THE METHOD TO ADD THE ATTRIBUTES
			module.addAttributes(parentNode)
			
			if (mc.checkBox('loadPoseChk', q = 1, value = 1 )): loadPose([mod])


def baseBuildRigGuides():
	# BASE
	print "BASE RIG BUILT"

def savePose():
	# METHOD FOR SAVING THE POSE OF A MODULE
	modules = getSelectedModules()	
	for module in modules:
		print module
		if not module == 'base':
			# FILTERING JUST THE RIG GUIDES NODES
			children = mc.listRelatives(module+'RigGuide', ad = 1, type = "transform")
			rigGuides = []
			for obj in children:
				splitted = obj.split('rigGuides')
				if len(splitted) >1:
					rigGuides.append(obj)		
			#BUILDING OF THE STRING 								
			toWrite = ''
			channels = ['tx','ty','tz','rx','ry','rz','sx','sy','sz']									
			for rigGuide in rigGuides:
			    for channel in channels:
			        value =  mc.getAttr(rigGuide+'.'+channel)
			        toWrite = toWrite+('mc.setAttr("'+rigGuide+'.'+channel+'" , '+str(value)+')\n')
			
			if not mc.objExists(module+'.pose'):		
				addString ('pose', module)
			mc.setAttr(module+'.pose', toWrite, type = 'string')			


def loadPose(modules = ['ToGet']):
	if modules[0] == 'ToGet':
		modules = getSelectedModules()
	# METHOD FOR LOADING THE POSE OF A MODULE	
	for module in modules:
		if not module == 'base':
			if mc.objExists(module+'.pose'):
				pose = mc.getAttr(module+'.pose')
				exec(pose)

def reset():
	# THE RESET IS MADE BY EXPORTING THE FRANK NODE IN A TEMP .ma FILE IN THE FRANK FOLDER,  
	# THEN MAKE NEW FILE RE-IMPORT THE FILE, DELETE IT 
	import os
	import frank
	frankFile = frank.__file__
	path = frankFile.split(".")[0]
	path.replace('\\','/')
	tmpFile = path+"/tmp.ma"
	mc.select('frank')
	mc.file ( tmpFile, options =("v=0") , force =1,  typ = "mayaAscii", pr = 1,  es =1);
	mc.file (f = 1, new =1)
	mc.file (tmpFile, i = 1)
	os.remove(tmpFile)
	
def new():
	result = mc.confirmDialog( title='Session Not Saved', message='Save changes? ', button=['Save',"Don't Save", 'Cancel'], defaultButton='Save', cancelButton='Cancel', dismissString="Don't Save" )
	if result == 'Save':			
		fileName = mc.getAttr('frank.fileName')
		if fileName == 'untitled':saveSessionAs()
		else: saveSession()
	if result =='Cancel': return

	mc.file(f = 1, new = 1)
	launch()
	
def saveSession():
	multipleFilters = "Maya Files (*.ma *.mb);;Maya ASCII (*.ma);;Maya Binary (*.mb);;All Files (*.*)"
	fileName = mc.getAttr('frank.fileName')
	if fileName != 'untitled':
		mc.select('frank')
		mc.file (fileName, options =("v=0") , force =1,  typ = "mayaAscii", pr = 1,  es =1)
		launch()
		print 'Frank Session Saved : '+fileName
	else:
		saveSessionAs()		
		
def saveSessionAs():
	multipleFilters = "Maya Files (*.ma *.mb);;Maya ASCII (*.ma);;Maya Binary (*.mb);;All Files (*.*)"
	fileName = mc.fileDialog2(fileMode=0, caption="Save Session As...", fileFilter=multipleFilters)
	if fileName == None: return	
	fileName= fileName[0]			
	mc.setAttr('frank.fileName', fileName, type = 'string')
	mc.select('frank')
	mc.file ( fileName, options =("v=0") , force =1,  typ = "mayaAscii", pr = 1,  es =1)
	launch()
	print 'Frank Session Saved : '+fileName

def openSession():
	multipleFilters = "Maya Files (*.ma *.mb);;Maya ASCII (*.ma);;Maya Binary (*.mb);;All Files (*.*)"
	fileName = mc.fileDialog2(fileMode=1, caption="Open Session...", fileFilter=multipleFilters)
	if fileName == None: return			 
	fileName= fileName[0]	
	mc.file(f = 1, new = 1)
	mc.file (fileName, i = 1)
	launch()

