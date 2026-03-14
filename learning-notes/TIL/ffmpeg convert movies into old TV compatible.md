# ffmpeg convert movies into old TV compatible

Date: 2026-03-14 12:37

---

ffmpeg -i "[input video]" \
-vf "scale=-1:720" \
-c:v libx264 -profile:v main -level 3.1 -pix_fmt yuv420p \
-c:a aac -ac 2 -b:a 128k \
"output video"

With old TVs an x265 isn't supported nor are 1080p framerate and so on.
Take a bit to convert and the CPU usage is high during. Took more than 86 minutes for a long movie


