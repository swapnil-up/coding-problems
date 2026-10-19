# bluetooth headset prefer a2dp over hfp

Date: 2026-08-15 21:19

---

Cheap/fake Bluetooth earbuds ("AirPods") often negotiate the low-quality **HFP**
profile (mono 16 kHz phone-call mode) instead of **A2DP** (hi-quality stereo),
and need several reconnects before the speaker + mic bind. PipeWire auto-switches
to HFP the moment any app opens the mic, which is what drags the output down.

Check what's actually active:

```
bluetoothctl menu audio
wpctl status          # look at the codec/profile on the bluez node
```

Stop the auto-switch and pin A2DP. Create
`~/.config/wireplumber/wireplumber.conf.d/51-bluez-prefer-a2dp.conf`:

```
wireplumber.settings = {
  bluetooth.autoswitch-to-headset-profile = false
}

monitor.bluez.properties = {
  bluez5.roles = [ a2dp_sink a2dp_source hfp_hf hfp_ag ]
  bluez5.codecs = [ sbc aac ]
}
```

Apply:

```
systemctl --user restart wireplumber
```

Reality check: this keeps it on A2DP, but the flaky reconnect is the fake chip's
Bluetooth stack (`running -> error` in the logs). Only a decent USB headset (or
genuine hardware) truly fixes the instability — and while on A2DP the mic won't
work at all, since A2DP is output-only.
