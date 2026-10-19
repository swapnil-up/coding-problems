# install postgres on ubuntu

Date: 2026-07-27 22:10

---

Ubuntu 24.04 didn't have PostgreSQL installed. Install server + contrib extras:

```
sudo apt update -qq && sudo apt install -y postgresql postgresql-contrib
```

`-qq` makes `apt update` nearly silent (errors only) — handy in scripts. `-q` is
less quiet; default is verbose progress bars.
