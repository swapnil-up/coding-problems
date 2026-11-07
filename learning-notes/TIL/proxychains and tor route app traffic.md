# Route an app's traffic through Tor with proxychains

Date: 2026-11-02

---

To force a single command (or an app like `opencode`) through Tor, use
`proxychains4` in front of it.

```bash
sudo apt install tor proxychains4 -y
sudo systemctl start tor

# proxychains4.conf should end with:  socks5 127.0.0.1 9050
sudo nano /etc/proxychains4.conf

# verify the exit IP changed
proxychains4 curl -s https://icanhazip.com

# run any app through it
proxychains4 opencode
```

Gotchas:

- Use `socks5` / `socks5h` (the `h` makes DNS resolve through the proxy). A plain
  `http` entry won't work with Tor's SOCKS port.
- Confirm Tor is actually listening on 9050: `ss -tlnp | grep 9050`.
- If it's not working, restart the daemon: `sudo systemctl restart tor`
  (a stale/half-started tor left the port closed here).
- Apps that honour proxy env vars can skip proxychains entirely:
  `export ALL_PROXY="socks5h://127.0.0.1:9050"`.
- `curl` can do it natively too: `curl --socks5-hostname 127.0.0.1:9050 -s https://icanhazip.com`.
