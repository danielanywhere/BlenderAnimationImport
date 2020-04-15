# ImportKeyframes.py
# Copyright (c). 2016 - 2020 Daniel Patterson, MCSD (danielanywhere)
# Released for public access under the MIT License.
# http://www.opensource.org/licenses/mit-license.php
# bl_info = {
#    "name": "ImportKeyframes",
#    "author": "DanielAnywhere / Daniel Patterson", 
#    "version": (1, 0, 0),
#    "blender": (2, 78, 0),
#    "location": "3D window > Tool Shelf",
#    "description": "Allows the non-destructive, additive, or composite import of timed pose information from text file.",
#    "warning": "",
#    "wiki_url": "http://wiki.blender.org/index.php?title=Extensions:2.6/Py/"
#        "Scripts/Import-Export/{TopicID}",
#    "tracker_url": "https://developer.blender.org/{TrackerID}",
#    "category": "Import-Export"}
# 20200206.1224 - This script doesn't yet have a UI or registration.
# All values are set manually at the beginning of the file.
# If you want this script to improve, please request those improvements.
# This script is compatible with 2.78x and 2.79x. Please request updates for 2.8x.
import bpy, re
import json

# Settings.
# Name of the data file to load.
scnDataFilename = "C:\\Temp\\MyAnimationData.json";

# Functionality.
def getObjectByName(passedName= ""):
	# print("Searching for " + passedName);
	result = None;
	obs = bpy.data.objects;
	for ob in obs:
		# print("Checking: " + ob.name);
		if ob.name == passedName:
			# print("getObjectByName(" + passedName + ").Object found...");
			result = ob;
	return result;

def getVectorValue(record, default=[0.0, 0.0, 0.0]):
	result = default;
	if(len(str(record["X"])) > 0):
		result[0] = float(record["X"]);
	if(len(str(record["Y"])) > 0):
		result[1] = float(record["Y"]);
	if(len(str(record["Z"])) > 0):
		result[2] = float(record["Z"]);
	return result;

def importFrames():
	# Set the scene.
	print("*** Start ***");
	obj = bpy.context.object
	scene = bpy.context.scene
	scene.frame_start = 1
	selected = None;
	vector = [0.0, 0.0, 0.0];

	with open(scnDataFilename, "r") as read_file:
		data = json.load(read_file);
	for record in data:
		# Clear local values.
		transformType = "";
		# Each name / value record.
		recordName = "";
		recordValue = "";
		try:
			recordName = record["Name"];
			print("Record: " + str(recordName));
		except:
			print("Name not specified");
		try:
			recordValue = record["Value"];
			print(" Value: " + str(recordValue));
		except:
			print("");
		if recordName == "FrameCount":
			print("  setting frame count...");
			scene.frame_end = recordValue;
		elif recordName == "FrameIndex":
			# Activate the current frame.
			# bpy.ops.anim.change_frame(frame = recordValue);
			print("  setting frame index...");
			scene.frame_set(frame = recordValue);
		elif recordName == "SelectObject":
			# Select the active object.
			selected = getObjectByName(recordValue);
			if selected != None:
				print("  selected: " + recordValue);
			else:
				print("  matching object not selected. No actions will be set.");
		elif recordName == "Rotate" and selected != None:
			# Rotate the active object.
			vector = getVectorValue(record);
			print("Set the rotation to ", vector);
			selected.rotation_euler = vector;
			selected.keyframe_insert(data_path = "rotation_euler");
			# transformType = transformType + "rotate";
		elif recordName == "Translate" and selected != None:
			# Update the location of the active object.
			vector = getVectorValue(record);
			selected.location = vector;
			selected.keyframe_insert(data_path = "location");
		elif recordName == "Scale" and selected != None:
			# Update the scale of the active object.
			vector = getVectorValue(record, default=[1.0, 1.0, 1.0]);
			selected.scale = vector;
			selected.keyframe_insert(data_path = "scale");

importFrames();
