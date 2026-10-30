import * as THREE from "three";
import { OrbitControls } from "jsm/controls/OrbitControls.js";
import getStarfield from "./getStarfield.js";

const scene = new THREE.Scene();

const w = window.innerWidth;
const h = window.innerHeight;
const cam = new THREE.PerspectiveCamera(75, w / h, 0.5, 1000);

const renderer = new THREE.WebGLRenderer();
renderer.setSize(w, h);
document.body.appendChild(renderer.domElement);
renderer.setAnimationLoop(animate);

const controls = new OrbitControls(cam, renderer.domElement);
controls.enableDamping = true;
controls.update;

const loader = new THREE.TextureLoader();
const earthGroup = new THREE.Group();
const geo = new THREE.SphereGeometry(3, 32, 32);
const mat = new THREE.MeshStandardMaterial({
  map: loader.load("00_earthmap1k.jpg"),
});
const earth = new THREE.Mesh(geo, mat);
earthGroup.add(earth);

earthGroup.rotation.z = (23.4 * Math.PI) / 100;

const stars = getStarfield({ numStars: 5000 });
scene.add(stars);

const sun = new THREE.DirectionalLight(0xffffff, 0.6);
sun.position.set(-1, 0, 1);
scene.add(sun);

const lightsmat = new THREE.MeshBasicMaterial({
  map: loader.load("./03_earthlights1k.jpg"),
  blending: THREE.AdditiveBlending,
});
const lightsmesh = new THREE.Mesh(geo, lightsmat);
earthGroup.add(lightsmesh);

const cloudsmat = new THREE.MeshStandardMaterial({
  map: loader.load("04_earthcloudmap.jpg"),
  blending: THREE.AdditiveBlending,
  transparent: true,
  opacity: 0.8,
});
const cloudsmesh = new THREE.Mesh(geo, cloudsmat);
cloudsmesh.scale.setScalar(1.008);
earthGroup.add(cloudsmesh);

cam.position.z = 10;

scene.background = new THREE.Color(0x000000);

scene.add(earthGroup);

function animate() {
  // earth.rotation.y += 0.001;
  // lightsmesh.rotation.y+=0.001;
  earthGroup.rotation.y += 0.001;
  cloudsmesh.rotation.y += 0.0005;
  controls.update();
  renderer.render(scene, cam);
}

// function getStarfield({ numStars }) {
//   const starGeo = new THREE.BufferGeometry();
//   const positions = [];

//   for (let i = 0; i < numStars; i++) {
//     const x = THREE.MathUtils.randFloatSpread(2000);
//     const y = THREE.MathUtils.randFloatSpread(2000);
//     const z = THREE.MathUtils.randFloatSpread(2000);
//     positions.push(x, y, z);
//   }

//   starGeo.setAttribute(
//     "position",
//     new THREE.Float32BufferAttribute(positions, 3)
//   );

//   const starMaterial = new THREE.PointsMaterial({
//     color: 0x888888,
//     size:1
//   });

//   return new THREE.Points(starGeo, starMaterial);
// }
