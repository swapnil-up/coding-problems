# sitemap namespace must be 0.9

Date: 2026-06-13 21:46

---

Google Search Console rejects a sitemap that declares the older 0.8 namespace, even though the XML shape is the same:

```xml
<!-- wrong -->
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.8">
<!-- right -->
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
```

For a sitemap index, use the same 0.9 namespace on `<sitemapindex>`. The error is "Your Sitemap or Sitemap index file does not properly declare the namespace."
