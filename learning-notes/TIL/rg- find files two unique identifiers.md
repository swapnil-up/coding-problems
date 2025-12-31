# rg- find files two unique identifiers

Date: 2025-12-24 15:18

---

## Insight
If I need to find a specific file with two search queries either of which exist in lots of files, then it's better to use a ripgrep and pipe the results of first query into the second to get an intersection of relevant info.

## Example
rg -l "store_id" database/migrations | xargs rg -l "inv_catalogues"

will return:
database/migrations/2025_07_15_store_id_in_inv_catalogues/2025_07_16_122115_alter_store_id_in_inv_catalogue.php

## Why this matters
No need to manually sort through lots of files manually. Much quicker finding this stuff. 
