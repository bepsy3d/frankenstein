//Maya ASCII 2012 scene
//Name: ciccio.ma
//Last modified: Sat, Sep 22, 2012 11:50:42 AM
//Codeset: 1252
requires maya "2012";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2012";
fileInfo "version" "2012 x64";
fileInfo "cutIdentifier" "001200000000-796618";
fileInfo "osv" "Microsoft Windows 7 Home Premium Edition, 64-bit Windows 7  (Build 7600)\n";
createNode transform -n "frank";
	addAttr -ci true -sn "fileName" -ln "fileName" -dt "string";
	addAttr -ci true -sn "Name" -ln "Name" -dt "string";
	setAttr -k on ".fileName" -type "string" "D:/__beppe/python/frank/sessions/ciccio.ma";
	setAttr -k on ".Name" -type "string" "Ciccio";
createNode transform -n "modules" -p "frank";
createNode transform -n "base" -p "modules";
	addAttr -ci true -sn "Name" -ln "Name" -dt "string";
	setAttr -k on ".Name" -type "string" "base";
createNode transform -n "spine" -p "modules";
	addAttr -ci true -sn "Name" -ln "Name" -dt "string";
	addAttr -ci true -sn "Module_Path" -ln "Module_Path" -dt "string";
	setAttr -k on ".Name" -type "string" "spine";
	setAttr -k on ".Module_Path" -type "string" "D:/__beppe/python/frank/Modules/spine_basic.py";
createNode transform -n "arm" -p "modules";
	addAttr -ci true -sn "Name" -ln "Name" -dt "string";
	addAttr -ci true -sn "Module_Path" -ln "Module_Path" -dt "string";
	setAttr -k on ".Name" -type "string" "arm";
	setAttr -k on ".Module_Path" -type "string" "D:/__beppe/python/frank/Modules/arm_basic.py";
createNode transform -n "leg" -p "modules";
	addAttr -ci true -sn "Name" -ln "Name" -dt "string";
	addAttr -ci true -sn "Module_Path" -ln "Module_Path" -dt "string";
	setAttr -k on ".Name" -type "string" "leg";
	setAttr -k on ".Module_Path" -type "string" "D:/__beppe/python/frank/Modules/leg_basic.pyc";
select -ne :time1;
	setAttr ".o" 1;
	setAttr ".unw" 1;
select -ne :renderPartition;
	setAttr -s 2 ".st";
select -ne :initialShadingGroup;
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultShaderList1;
	setAttr -s 2 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
select -ne :renderGlobalsList1;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
select -ne :defaultHardwareRenderGlobals;
	setAttr ".fn" -type "string" "im";
	setAttr ".res" -type "string" "ntsc_4d 646 485 1.333";
// End of ciccio.ma
