//Maya ASCII 2012 scene
//Name: Pucci.ma
//Last modified: Mon, Jul 30, 2012 06:31:06 PM
//Codeset: 1252
requires maya "2012";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2012";
fileInfo "version" "2012 x64";
fileInfo "cutIdentifier" "001200000000-796618";
fileInfo "osv" "Microsoft Windows 7 Home Premium Edition, 64-bit Windows 7  (Build 7600)\n";
createNode transform -n "frank";
	addAttr -ci true -sn "fileName" -ln "fileName" -dt "string";
	addAttr -ci true -sn "Name" -ln "Name" -dt "string";
	setAttr -k on ".fileName" -type "string" "D:/__beppe/python/frank/sessions/Pucci.ma";
	setAttr -k on ".Name" -type "string" "Pucci";
createNode transform -n "modules" -p "frank";
createNode transform -n "base" -p "modules";
	addAttr -ci true -sn "Name" -ln "Name" -dt "string";
	setAttr -k on ".Name" -type "string" "base";
createNode transform -n "arm" -p "modules";
	addAttr -ci true -sn "Name" -ln "Name" -dt "string";
	addAttr -ci true -sn "Module_Path" -ln "Module_Path" -dt "string";
	addAttr -ci true -sn "pose" -ln "pose" -dt "string";
	setAttr -k on ".Name" -type "string" "arm";
	setAttr -k on ".Module_Path" -type "string" "D:/__beppe/python/frank/Modules/arm_basic.py";
	setAttr -k on ".pose" -type "string" (
		"mc.setAttr(\"L_arm3_rigGuides.tx\" , 2.17582885169)\nmc.setAttr(\"L_arm3_rigGuides.ty\" , -1.94465016536)\nmc.setAttr(\"L_arm3_rigGuides.tz\" , 1.48265877233)\nmc.setAttr(\"L_arm3_rigGuides.rx\" , 0.0)\nmc.setAttr(\"L_arm3_rigGuides.ry\" , 0.0)\nmc.setAttr(\"L_arm3_rigGuides.rz\" , 0.0)\nmc.setAttr(\"L_arm3_rigGuides.sx\" , 1.0)\nmc.setAttr(\"L_arm3_rigGuides.sy\" , 1.0)\nmc.setAttr(\"L_arm3_rigGuides.sz\" , 1.0)\nmc.setAttr(\"L_arm2_rigGuides.tx\" , 3.49377824571)\nmc.setAttr(\"L_arm2_rigGuides.ty\" , -1.88073546308)\nmc.setAttr(\"L_arm2_rigGuides.tz\" , -0.283226648406)\nmc.setAttr(\"L_arm2_rigGuides.rx\" , 0.0)\nmc.setAttr(\"L_arm2_rigGuides.ry\" , 0.0)\nmc.setAttr(\"L_arm2_rigGuides.rz\" , 0.0)\nmc.setAttr(\"L_arm2_rigGuides.sx\" , 1.0)\nmc.setAttr(\"L_arm2_rigGuides.sy\" , 1.0)\nmc.setAttr(\"L_arm2_rigGuides.sz\" , 1.0)\nmc.setAttr(\"L_arm1_rigGuides.tx\" , 1.0)\nmc.setAttr(\"L_arm1_rigGuides.ty\" , 8.0)\nmc.setAttr(\"L_arm1_rigGuides.tz\" , 0.0)\nmc.setAttr(\"L_arm1_rigGuides.rx\" , 0.0)\nmc.setAttr(\"L_arm1_rigGuides.ry\" , 0.0)\nmc.setAttr(\"L_arm1_rigGuides.rz\" , 0.0)\nmc.setAttr(\"L_arm1_rigGuides.sx\" , 1.0)\n"
		+ "mc.setAttr(\"L_arm1_rigGuides.sy\" , 1.0)\nmc.setAttr(\"L_arm1_rigGuides.sz\" , 1.0)\n");
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
// End of Pucci.ma
