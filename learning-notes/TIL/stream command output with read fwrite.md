# stream command output with read fwrite

Date: 2026-06-05 22:41

---

A client that read a child process into a fixed 65 KB buffer silently truncated large search results. Don't accumulate output into a fixed buffer; stream it out as it arrives:

```c
char buf[65536];
ssize_t n;
while ((n = read(fd, buf, sizeof buf)) > 0) {
    if (fwrite(buf, 1, (size_t)n, stdout) != (size_t)n) {
        perror("fwrite");
        break;
    }
}
```

Handle `EINTR` by retrying `read`, and check `fwrite`'s return value. A loop that stops at the first short read also drops data.

If the output must be buffered, grow it dynamically or write to a temporary file. Test with output larger than the buffer, not just a small happy-path response.
