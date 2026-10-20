# raylib getframetime movement speed

Date: 2026-05-19 21:26

---

`GetFrameTime()` returns seconds since the last frame (~0.016 at 60 FPS), so this is far too slow:

```c
x += speed * GetFrameTime();   // speed=5 -> 0.08 px/frame
```

Either treat `speed` as pixels per second and use a realistic value:

```c
x += 300.0f * GetFrameTime();  // 300 px/s
```

or drop frame-time scaling for a fixed per-frame step:

```c
x += 5.0f;
```

Pick one convention for the whole game; mixing them makes speed depend on FPS.
