Introduction
HTTP Query Builders (distinct from Eloquent Query Builders) parse URL parameters and transform them into database queries. They handle filtering, sorting, pagination, and search in a type-safe, reusable way. This keeps controllers clean and makes complex data table requirements manageable.
Knowledge Points
Concept

[[HTTP Query Parameters]]
[[Query String Parsing]]
[[URL to Database Query Mapping]]
[[spatie/laravel-query-builder Package]]

Implementation

[[Creating Query Builder Classes]]
[[Allowed Filters]]
[[Allowed Sorts]]
[[Allowed Includes]]
[[Default Queries]]

Filter Types

[[Exact Filters]]
[[Partial Filters]]
[[Scope Filters]]
[[Custom Filter Classes]]
[[Relationship Filters]]

Advanced Features

[[Complex Joins for Filtering]]
[[Fuzzy Search Filters]]
[[Date Range Filters]]
[[Enum Filters]]
[[Multiple Sort Parameters]]

Integration

[[Injecting Query Builders in Controllers]]
[[Query Builders in View Models]]
[[Combining with Eloquent Scopes]]
[[Type-Safe Query Results]]

Frontend Integration

[[Building Filter UIs]]
[[URL State Management]]
[[AJAX Data Tables]]
[[Frontend Query Parameters]]

Security

[[Preventing SQL Injection]]
[[Validating Filter Input]]
[[Allowed vs Requested Filters]]

Testing

[[Testing Query Builder Filters]]
[[Testing Sort Behavior]]
[[Testing Edge Cases]]

Related Topics
[[Custom Query Builders]], [[Application Modules]], [[View Models]]
Questions to Explore

How do you handle complex multi-table filters?
Should query validation be in requests or query builders?
How do you document available filters for frontend?
What's the performance impact of dynamic queries?

Practical Examples

 Create InvoiceIndexQuery with filters and sorts
 Build a searchable, sortable data table
 Add relationship filtering
 Test complex filter combinations
