# find your public ip v4 vs v6

Date: 2026-08-17 13:25

---

Quick ways to see your public IP:

```
curl -s ifconfig.me        # whatever family is available
curl -4 -s ifconfig.me     # force IPv4
curl -6 -s ifconfig.me     # force IPv6
hostname -I                # local interface addresses
```

Alternate echo services if one is down: `icanhazip.com`, `api.ipify.org`.

Gotcha: many ISPs use **CGNAT** — `curl -4` returns a shared NAT address, not your
own, and you'll be reachable over IPv6 (`2407:...` etc.) instead. So "I have no
public IP" usually means "I have a public IPv6 but only a shared IPv4".
