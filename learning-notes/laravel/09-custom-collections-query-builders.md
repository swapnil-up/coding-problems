Introduction
Laravel's collections and query builders are powerful, but generic. Creating custom classes for specific models reduces code duplication, improves type safety, and centralizes domain logic. Custom query builders handle common queries, while custom collections add domain-specific operations on result sets.
Knowledge Points
Custom Query Builders

[[Extending Eloquent Builder]]
[[Creating Model-Specific Builders]]
[[Registering Custom Builders]]
[[Type-Safe Query Methods]]
[[Reusable Query Scopes]]

Query Builder Patterns

[[Named Query Methods]]
[[Chainable Query Builders]]
[[Complex Join Queries]]
[[Eager Loading in Builders]]
[[Performance Considerations]]

Custom Collections

[[Extending Eloquent Collection]]
[[Creating Model-Specific Collections]]
[[Registering Custom Collections]]
[[Domain Logic in Collections]]
[[Collection Pipelines]]

Collection Patterns

[[Filtering Collections]]
[[Transforming Collections]]
[[Calculating Aggregates]]
[[Collection Helper Methods]]
[[When Collections Replace Actions]]

Type Safety

[[Typed Collection Returns]]
[[Typed Query Results]]
[[IDE Autocompletion]]
[[Static Analysis Benefits]]

Testing

[[Testing Query Builders]]
[[Testing Collections]]
[[Database Fixtures for Tests]]
[[Collection Test Assertions]]

Related Topics
[[Domain Models]], [[Type Safety]], [[Testing]]
Questions to Explore

When should logic go in collections vs actions?
How do you handle complex multi-model queries?
What's the performance cost of custom collections?
Should query builders be in domain or application layer?

Practical Examples

 Create InvoiceQueryBuilder with whereUnpaid()
 Build InvoiceLineCollection with creditLines()
 Add type hints to all query methods
 Write tests for custom builder methods
