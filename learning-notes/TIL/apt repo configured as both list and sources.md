# apt repo configured as both list and sources

Date: 2026-05-20 06:19

---

APT warns when the same repository is defined in both legacy `.list` and deb822 `.sources` files:

```text
W: Target Packages ... is configured multiple times in
   /etc/apt/sources.list.d/vscode.list:1 and
   /etc/apt/sources.list.d/vscode.sources:1
```

Find the duplicate definitions:

```bash
grep -R "packages.microsoft.com/repos/code" /etc/apt/sources.list /etc/apt/sources.list.d
```

Keep one format. If the bootstrap script writes a `.list` file, remove the older `.sources` file, or update the script to detect an existing repo before adding it:

```bash
sudo rm /etc/apt/sources.list.d/vscode.sources
sudo apt update
```

Don't ignore these warnings during bootstrap: duplicate targets slow every `apt update` and make it unclear which file owns the repository.
