

31-08-2024 21:19

Status:

Tags:



# Learn Three.js by Building 5 projects

The initial idea for now is to take notes as I watch the tutorial. Write thoughts and specific sections of interest. These might go into anki. No coding anything just yet. First watch the whole thing, then try to build while googling what I don't know at all. 

Get LiveServer in VSCode to get a quick feedback loop and gratification. 

The index has two things related to three js: an import map and loading the js file.

import * as THREE from "three";

For a scene three JS needs 3 things:
1. a renderer
2. a camera
3. a scene object

A renderer is just THREE.WebGLRenderer()

A perspective camera requires 4 things:
1. a field of view- 75 degree
2. an aspect- width/height
3. a near- 0.1 units 
4. a far- any value greater

you can move the camera a lil further away with changing camera position:
	camera.position.z
this is so that you're not in the same spot as the scene and can actually observe.

scene= new THREE.Scene();

renderer.render(scene,camera) // to start rendering

when you add an item you also need to set the renderer size as well as append the domElement to the document.

you can pass simple geometries that are built in as primitives using:
new THREE.icosahedronGeometry(size, detail)
it needs a material too which should have stuff like color

then just make the mesh.

you need to add the object to the scene. literally- scene.add(item);

but for animating and rendering it's better to do it in a loop, so the cool thing is actually to put it in a function which requests the animation frame then renders. Call said function once then you're good to go.
You can look inside the console to see how many frames it's changing during.
call the animation for the first time using: renderer.setAnimationLoop(animate); where animate is the name of the function.

By setting the wireframe as true, just the edge lines are shown
const material= new THREE.MeshBasicMaterial({color:0xff3495, wireframe:true});



There's all types of options like 
1. setting flatshading to true (don't care atm)
2. using hemisphere lights- doesn't work with MeshBasicMaterial, need to use MeshStandardMaterial or MeshPhongMaterial
3. rotating the image- {variable to rotate}.rotation.{axis} // need to increment this value with every animated frame.

We have addons to import such as orbitcontrol by:
import {OrbitControls} from "jsm/controls/OrbitControls.js"

then you can use it to move dom elements with a simple:
new OrbitControls(camera, renderer.domElement)
which would allow you to scroll and zoom in and out

The coolest thing is allowing damping so that when you click and flick even after releasing there's some extra movement that makes it look so much more natural. Just enable then set the damping factor to a small number.Done by changing those properties of the controls, not a scene object.

Be sure to update controls in the animate too.


If you're using cdn instead of vitejs then after putting orbit in the importmap, the import in the js looks as follows:
import { OrbitControls } from "jsm/controls/OrbitControls.js";

interesting that to save resources the animation stops when the website is not the actively focused window.


# References

https://www.youtube.com/watch?v=KtYby2QN0kQ
https://threejs.org/docs/
