# Android Quick Settings tiles must be manifest-declared (no runtime registration)

Date: 2026-11-05

---

A Quick Settings tile is a manifest-declared `TileService` component. An app
**cannot create a brand-new tile while running** — there is no public API to
register an arbitrary user-defined tile. So a "let users add tiles as needed"
feature has to ship a fixed **catalog** of declared tile services, and the user
adds the ones they want from the QS edit (pencil) screen.

Manifest requirements that are easy to get wrong:

```xml
<service
    android:name=".TimerTileService"
    android:exported="true"
    android:icon="@drawable/ic_timer"
    android:label="@string/tile_label"
    android:permission="android.permission.BIND_QUICK_SETTINGS_TILE">
    <intent-filter>
        <action android:name="android.service.quicksettings.action.QS_TILE" />
    </intent-filter>
</service>
```

- The permission is **`BIND_QUICK_SETTINGS_TILE`**, not `BIND_TILE_SERVICE`
  (the latter doesn't exist and silently does nothing).
- To *prompt* the user to add the tile, use
  **`StatusBarManager.requestAddTileService()`** (Android 13 / API 33+), **not**
  a method on `TileService`. Below API 33 you can only show instructions.
- Verify the class/method exist in the SDK you compile against:
  `javap -classpath $ANDROID_HOME/platforms/android-36/android.jar android.service.quicksettings.TileService`

Design implication: multiple tiles = multiple declared services in the catalog
(`Timer5TileService`, `Timer15TileService`, …), each added individually.
