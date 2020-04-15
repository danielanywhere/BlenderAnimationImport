# Blender Animation Importer
Import animations directly into your Blender file from external sources that output activity elements as automation data.

## Usage
 - In Blender, open the **Text Editor** view.
 - Click the button titled **Open**.
 - Select the importer script file from this project **ImportKeyframes.py**, and click **Open Text Block**.
 - In the file, locate the variable assignment for **scnDataFilename**, and type the full path and filename of the data file into the quoted area.
 - Click the button **Run Script** to import the keyframes.

## Data File Format
The current data format of the file is JSON, with the following syntax.

| Command | Parameters | Description |
|---------|------------|-------------|
| Capture | (None) | Capture a keyframe for the current rotation, location, and scale of the selected object at the currently indexed frame. |
| FrameCount | Number | Set the total count of frames in the Blender animation. |
| FrameIndex | Number | Set the current frame at which to insert a keyframe. |
| SelectObject | String | Select the named object in Blender. Must match an existing object in the tree of the open file. |
| Rotate | 3D Vector | Rotate the selected object by the X, Y, Z Euler amount. |
| Translate | 3D Vector | Move the selected object by the X, Y, Z distance. |
| Scale | 3D Vector | Scale the selected object by the X, Y, Z amount. |

## Example
Following is example data that can be fed to the ImportKeyframes.py script.
<blockquote><pre>
[
 {
  &quot;Name&quot;: &quot;FrameCount&quot;,
  &quot;Value&quot;: 7224
 },
 {
  &quot;Name&quot;: &quot;FrameIndex&quot;,
  &quot;Value&quot;: 1
 },
 {
   &quot;Name&quot;: &quot;SelectObject&quot;,
   &quot;Value&quot;: &quot;TireLeft&quot;
 },
 {
   &quot;Name&quot;: &quot;Rotate&quot;,
   &quot;X&quot;: 0,
   &quot;Y&quot;: 0,
   &quot;Z&quot;: 0
 },
 {
   &quot;Name&quot;: &quot;Capture&quot;
 },
 {
   &quot;Name&quot;: &quot;SelectObject&quot;,
   &quot;Value&quot;: &quot;TireRight&quot;
 },
 {
   &quot;Name&quot;: &quot;Rotate&quot;,
   &quot;X&quot;: 0,
   &quot;Y&quot;: 0,
   &quot;Z&quot;: 0
 },
 {
   &quot;Name&quot;: &quot;Capture&quot;
 }
]
</pre></blockquote>

## Remarks
This is version 1, and very specific in operation, yet somewhat safe. If an unrecognized command is present in the data, that command will be ignored. This allows your automation export data to be much more verbose than what is handled by the script.

This script does not yet have any user interface elements, since the only variable is the filename and path. However, if you wish to use this as more of a plug-in style action with its own menu option, please request the feature, or vote for that feature if it has already been requested.

Thanks for your continued support,
Daniel
