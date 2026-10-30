import * as THREE from "three";
import { OrbitControls } from "jsm/controls/OrbitControls.js";
import spline from "./spline.js";

const w = window.innerWidth;
const h = window.innerHeight;
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, w / h, 0.1, 1000);
camera.position.z = 5;
const renderer = new THREE.WebGLRenderer();
renderer.setSize(w, h);
document.body.appendChild(renderer.domElement);

const ctrls = new OrbitControls(camera, renderer.domElement);
ctrls.enableDamping = true;

const points = spline.getPoints(100);
// const linegeo = new THREE.BufferGeometry().setFromPoints(points);
// const linemat = new THREE.LineBasicMaterial({ color: 0xff0000 });
// const lines = new THREE.Mesh(linegeo, linemat);
// scene.add(lines);

const tubeGeo = new THREE.TubeGeometry(spline, 200, 0.5, 7, true);
const tubemat = new THREE.MeshBasicMaterial({
  color: 0xff0000,
  wireframe: true,
});
const tube = new THREE.Mesh(tubeGeo, tubemat);
scene.add(tube);

function UpdateCamera(t) {
  const time = t * 0.1;
  const looptime = 10 * 1000;
  const p = (time % looptime) / looptime;
  const pos = tubeGeo.parameters.path.getPointAt(p);
  const lookAt = tubeGeo.parameters.path.getPointAt((p + 0.03) % 1);
  camera.position.copy(pos);
  camera.lookAt(lookAt);
}

function animate(t = 0) {
  requestAnimationFrame(animate);
  UpdateCamera(t);
  renderer.render(scene, camera);
  ctrls.update();
}

animate();
