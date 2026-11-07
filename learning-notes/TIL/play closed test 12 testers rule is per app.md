# Google Play's 12-tester / 14-day closed test rule is per app

Date: 2026-11-03

---

For a new Google Play developer account, getting **production** access requires a
closed test with **12 testers for 14 continuous days**. The key detail for
anyone shipping multiple apps: this is **per app, not per account**.

- Production access is applied for **per app**.
- Each app's closed test needs its own 12 opted-in testers for 14 continuous days.
- The same people can be reused, but they must **opt in to each app
  separately**, and the 14-day clock restarts for that app.
- Practically: budget **~2 weeks minimum per app**, plus review time — closed
  testing can't be parallelised across apps on one account.

Planning implication: for a portfolio of small apps, stagger the closed tests (or
get testers to opt into each app as it's ready) rather than assuming one 14-day
push unlocks everything.
