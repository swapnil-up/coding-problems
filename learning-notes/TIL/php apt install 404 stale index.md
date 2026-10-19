# php apt install 404 stale index

Date: 2026-08-04 06:48

---

`404 Not Found` when installing e.g. `php8.3-pgsql` means the local package
index is stale — it points at a build the sury.org server no longer serves
(e.g. `8.3.32-1+0~20260708.85`).

Refresh first:

```
sudo apt update
```

then retry the install. If 404s persist, check the sources file has the right
distro name — on Ubuntu 24.04 it must be `noble`, not `bookworm`:

```
cat /etc/apt/sources.list.d/php*.sources /etc/apt/sources.list.d/php*.list
```
