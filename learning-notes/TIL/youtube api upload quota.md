# youtube api upload quota

Date: 2026-08-07 08:12

---

The YouTube Data API gives a new project 10,000 quota units per day. An upload costs about 1,600 units, so a fresh project can upload only about **6 videos per day**.

```text
10,000 units/day / 1,600 units/upload = 6.25 uploads/day
```

A bulk upload will fail partway through with quota errors, not with an authentication or encoding error. Check the Google Cloud project's quota usage before a batch:

```text
Google Cloud Console -> APIs & Services -> YouTube Data API v3 -> Quotas
```

For occasional uploads the default is fine. For a backlog, request a quota increase in advance, split the batch across days, or reuse the cached OAuth token so the failure is only quota, not repeated browser authorization.
