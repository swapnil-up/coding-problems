

02-09-2024 16:07

Status:

Tags:



# threeJS project 3 - FreeCodeCamp

The wireframe wormhole effect. 
Spline- representation of a line in 3d space

Steps:
load the path data
create a spline from that
use as a basis for tube geometry.
then add edge geometry
make some obstacles
give the lines some glow

Start with the boilerplate. 
import spline from spline.js

first we add the line to the scene. get points from the spline. like a 100. then the geometry become a buffergeometry which we set from the points. then our material is a linebasicmaterial with whatever color. then load the line like you would a mesh. add to scene

next for the tube geometry. we load the parameters of the spline, the points along the line, the radius of the tube, the divisions along the radius and if it is close or not. the mesh should be a wireframe (duh), and it's doublesided so that we can enter into it later. 

now we gotta move the camera through the tube. for this our updatecamera is first called in the animate function with with a value of t. the function then multiplies the time, loops ... will fill in later. because wtf

MOTHERFUCKING FUCKING FUCK. ANOTHER TWO? THREE? FUCKING HOURS ON A STUPID ASS ERROR. 

function UpdateCamera() {
const t=Date.now()*0.5;
const time = t * 0.1;
const looptime = 10 * 1000; 
const p = (time % looptime) / looptime;
const pos = tubeGeo.parameters.path.getPointAt(p);
const lookAt = tubeGeo.parameters.path.getPointAt((p + 0.03) % 1);
camera.position.copy(pos);
camera.lookAt(lookAt);
}

I now understand all of this fucking code, spent so many hours trying to make my code work. The lookat was not working at all. A chance mistype an hour? earlier lookAtSphere.position.copy(lookAt);
this entered as the last line of the block and it magically started working. None of those tutorials had an answer. The problem was in the update / animate block. I called the renderer before the updatecamera. In hindsight the error was obvious too. There were errors related to that line for no discernible reason. Changing the order of the two solved the problem. 

I was very confused, but a happy stroke having had the lookAtSphere be the position helper. I'd probably have been here till 5 otherwise. 

FOR THE FUTURE, PUT THE DAMN RENDERER AT THE END. The order of the commands matter. I've had that problem before with adding stuff later but calling it before. Like with the earthgroup. A bittersweet lesson I'll have. THREE? fucking hours but happy that it's working now. 

As a sidenote, this is probably why following the tutorial by itself is a problem. It works when it's just the tutorial guidelines, but is a problem if you do anything outside it's constraints. Because you don't have the prerequisites to understand how that exact bit of code worked. You can follow the trail, but you'll die quick if you venture off of it.  


you can add fog to the scene. fogexp2(0x000000, 0.3) where 0.3 is the density?

next is the edges geometry. there's the edges geometry and the line material. it's tube geo and linesegments

for boxes we're creating n boxes of BoxGeometry. Then putting in a loop. we calculate the position like we did for the updatecamera in terms of pos. He added them to a position within the tube. then gave it a lil bit of randomness in term of position and rotation. We alo made boxhelpers. Not sure why

Add a glow. He just added a block of code from a previous project. 


# References

[[Learn Three.js by Building 5 projects]]
https://www.youtube.com/watch?v=KtYby2QN0kQ
https://threejs.org/docs/
