# apt repo gpg key must be dearmored

Date: 2026-05-20 06:08

---

Adding a third-party apt repo by piping the vendor's ASCII-armored key straight
into a `.gpg` file leaves apt unable to read it:

```
W: ... The key(s) in the keyring /etc/apt/trusted.gpg.d/llvm-18.gpg are ignored as the file has an unsupported filetype.
E: Package 'clang-18' has no installation candidate
```

The file is ASCII-armored (`.asc` format) but named `.gpg`. Either save it as
`.asc`, or convert it to the binary keyring format apt expects:

```
wget -qO- https://apt.llvm.org/llvm-snapshot.gpg.key \
  | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/llvm-18.gpg
```

Then add the repo and refresh:

```
echo "deb http://apt.llvm.org/bookworm/ llvm-toolchain-bookworm-18 main" \
  | sudo tee /etc/apt/sources.list.d/llvm-18.list
sudo apt update
```

General rule: `gpg --dearmor` when the target ends in `.gpg`; plain copy when it
ends in `.asc`.
