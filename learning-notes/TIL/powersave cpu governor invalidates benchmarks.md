# powersave cpu governor invalidates benchmarks

Date: 2026-06-05 22:39

---

An apparent 8–10x performance regression was CPU throttling, not code. The `powersave` governor held an i7-8550U at roughly 400–1200 MHz instead of its 4.0 GHz maximum.

Check the governor and current frequency before trusting any benchmark:

```bash
cpupower frequency-info
cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
grep MHz /proc/cpuinfo
```

Pin the CPU to `performance` for the run, then restore the previous governor:

```bash
sudo cpupower frequency-set -g performance
# benchmark
sudo cpupower frequency-set -g powersave
```

Record the governor, AC/battery state, and observed MHz alongside benchmark results. A result that moves by an integer multiple of the clock ratio is usually the governor, not the change under test.
