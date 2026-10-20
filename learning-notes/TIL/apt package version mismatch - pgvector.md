# apt package version mismatch - pgvector

Date: 2026-08-06 21:53

---

`sudo apt install postgresql-16-pgvector` failed with:

```
E: Unable to locate package postgresql-16-pgvector
```

Ubuntu 22.04 ships PostgreSQL 14, not 16, so the versioned package name does
not exist in the default repos. Match the package to the installed major
version:

```
psql --version
sudo apt install postgresql-14-pgvector
```

If that package is still unavailable, add the PGDG repo and install the whole
matching set (`postgresql-14` + `postgresql-14-pgvector`).

In setup scripts, don't let one missing package abort the whole bootstrap under
`set -e`; log it and continue.
