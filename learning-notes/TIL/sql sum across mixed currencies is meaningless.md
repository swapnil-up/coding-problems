# sql sum across mixed currencies is meaningless

Date: 2026-06-10 21:47

---

`SUM(amount)` over transactions in different currencies is not a balance. It adds raw numbers with different units:

```sql
-- wrong
SELECT SUM(amount) FROM transactions;
```

Filter by the display currency, or convert every row to a base currency first:

```sql
SELECT SUM(amount)
FROM transactions
WHERE currency = :preferredCurrency;
```

For a multi-currency dashboard, store the exchange rate used at transaction time and sum `amount * rate_to_base`, not the raw amount. Keep one source of truth for the default currency; hardcoded `"USD"` defaults in state, ViewModel, and SQL drift apart.

Add an invariant test with two currencies and equal amounts: the filtered balance must change when the filter changes, while the raw sum stays misleadingly constant.
