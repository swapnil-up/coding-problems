# Cloudflare WARP: install and rotate the IP with warp-cli

Date: 2026-10-26

---

Cloudflare WARP gives you a Cloudflare-routed IP and a simple way to get a new
one on demand. Install via Cloudflare's apt repo (key must be dearmored):

```bash
curl -fsSL https://pkg.cloudflareclient.com/pubkey.gpg \
  | sudo gpg --yes --dearmor --output /usr/share/keyrings/cloudflare-warp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/cloudflare-warp-archive-keyring.gpg] https://pkg.cloudflareclient.com/ $(lsb_release -cs) main" \
  | sudo tee /etc/apt/sources.list.d/cloudflare-client.list
sudo apt update && sudo apt install cloudflare-warp -y
```

Then register and connect:

```bash
warp-cli registration new
warp-cli mode warp
warp-cli connect
```

To get a **fresh IP**, delete the registration and make a new one — the alias
`newip` just chains these:

```bash
warp-cli disconnect
warp-cli registration delete
warp-cli registration new
warp-cli connect
```

Notes / gotchas:

- The `warp-svc` systemd service must be running; `warp-cli status` talks to it.
- `warp-cli registration` also works via the `./wgcf` route (WireGuard config),
  but the apt package + `warp-cli` is far less fiddly.
- Verify the exit IP with `curl -s https://icanhazip.com`.

There is a companion `warp-new-ip.sh` in `~/github/scripts` and a `,newip` rofi
alias; `cloudflare-warp`/`warp-cli` were added to the bootstrap manifest.
