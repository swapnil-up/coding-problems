# kmp android sdk bootstrap

Date: 2026-06-16 17:03

---

`setup/kmp.sh` — bootstraps a Kotlin Multiplatform / Android build environment on
a fresh machine. It:

1. installs **SDKMAN** (if missing)
2. installs **JDK 21 (Temurin)** via SDKMAN
3. downloads **Android cmdline-tools** into `~/Android/Sdk`
4. installs `platforms;android-36`, `build-tools;36.0.0`, `platform-tools`
5. writes **udev rules** for Google / Samsung / Xiaomi / OnePlus devices
6. adds the user to the **`plugdev`** group
7. persists `JAVA_HOME` and `ANDROID_HOME` in `.bashrc`

Then registered in `bootstrap.sh`'s `SCRIPTS` array (after `languages.sh`).

Note: the Android SDK is **required** to build the Android target — it supplies
`platforms;android-<n>` (compile against), `build-tools` (`aapt2`, `d8`, …) and
`platform-tools` (`adb`). Remember to **re-login** for the `plugdev` group to
take effect (device access via `adb` won't work until then).
