import * as THREE from "three";
import { OrbitControls } from "jsm/controls/OrbitControls.js";

const w = window.innerWidth;
const h = window.innerHeight;

const renderer = new THREE.WebGLRenderer();
renderer.setSize(w, h);
document.body.appendChild(renderer.domElement);

const camera = new THREE.PerspectiveCamera(75, w / h, 0.1, 10);

const scene = new THREE.Scene();

const geometry = new THREE.IcosahedronGeometry(2, 2);
const material = new THREE.MeshStandardMaterial({ color: 0xff3495, flatShading:true });
const mesh = new THREE.Mesh(geometry, material);
scene.add(mesh);

const wireframe = new THREE.WireframeGeometry(geometry);
const line = new THREE.LineSegments(wireframe);
scene.add(line);
line.scale.setScalar(1.001)
camera.position.z = 5;

const light = new THREE.HemisphereLight(0xffffbb, 0x080820, 3);
scene.add(light);

scene.background = new THREE.Color(0xffffff);

const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.setDampingFactor = 0.05;
controls.update();

function animate() {
  mesh.rotation.x += 0.01;
  mesh.rotation.y += 0.01;
  line.rotation.x += 0.01;
  line.rotation.y += 0.01;
  controls.update();
  renderer.render(scene, camera);
}
renderer.setAnimationLoop(animate);
