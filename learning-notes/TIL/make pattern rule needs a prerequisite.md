# make pattern rule needs a prerequisite

Date: 2026-05-19 21:14

---

A pattern rule with no prerequisite expands `$<` to an empty string:

```make
run-%:
	gcc $(CFLAGS) -o $@ $< $(LDFLAGS)
```

`make run-main.c` then runs `gcc ... -o run-main.c` with no source file.

Declare the source as a prerequisite and use a target without a dot in the stem:

```make
run-%: %.c
	gcc $(CFLAGS) -o $@ $< $(LDFLAGS)
```

Then invoke `make run-main`, not `make run-main.c`. With `run-main.c`, the stem is `main.c`, so `%.c` would look for `main.c.c`.

Use `$*` when constructing names from the stem, and quote paths if the stem can contain spaces. Phony convenience targets are easier to reason about when they don't contain the source suffix.
