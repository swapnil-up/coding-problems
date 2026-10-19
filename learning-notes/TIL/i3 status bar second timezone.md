# i3 status bar second timezone

Date: 2026-08-06 11:59

---

Add a second clock (e.g. Melbourne) to i3status. First declare it in the `order`:

```
order += "tztime local"
order += "tztime melbourne"
```

Then add the block (the `instance` is the bit after `tztime`):

```
tztime local {
        format = "%Y-%m-%d %H:%M:%S"
}

tztime melbourne {
        format = "MEL %H:%M"
        timezone = "Australia/Melbourne"
}
```

i3status can't colour an individual block itself. Because the status command
here is a wrapper that rewrites the JSON, you can post-process it — match the
block and set a `color`:

```python
for block in blocks:
    if block.get("name") == "tztime" and block.get("instance") == "melbourne":
        block["color"] = "#FFA500"
```

Note the JSON `name` is just `tztime` and `instance` is `melbourne`, not a single
`"tztime melbourne"` string.

Apply with stow and restart i3:

```
stow -R -t ~ -d config i3status
i3-msg restart
```
