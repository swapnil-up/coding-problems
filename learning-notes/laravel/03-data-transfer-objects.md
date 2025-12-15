Introduction
Data Transfer Objects (DTOs) are classes that encapsulate data in a structured, type-safe way. They serve as the entry point for external data into your codebase, transforming unstructured input (arrays, requests) into predictable, strongly-typed objects.
Why DTOs matter: In large Laravel applications, passing around arrays of data creates cognitive overhead - you never know what keys exist or what types the values are without diving into the code. DTOs solve this by making data structures explicit and IDE-friendly.
Key principle: DTOs represent data only - no business logic, just pure data representation with type safety.

Knowledge Points
Core Concepts

[[Type Systems - Strong vs Weak]]
[[Type Systems - Static vs Dynamic]]
[[PHP Type Juggling]]
[[Static Analysis Benefits]]
[[Cognitive Load in Large Codebases]]

DTO Fundamentals

[[What is a DTO]]
[[DTOs vs Arrays]]
[[DTOs vs Value Objects]]
[[DTOs vs Models]]
[[When to Use DTOs]]
[[DTO Immutability]]

Implementation Patterns

[[Creating DTOs with Typed Properties]]
[[DTO Constructor Patterns]]
[[DTO Factory Methods]]
[[Named Parameters in DTOs (PHP 8+)]]
[[Constructor Property Promotion (PHP 8+)]]

Working with DTOs

[[Mapping Request Data to DTOs]]
[[DTO Validation Strategy]]
[[Nested DTOs]]
[[DTO Collections]]
[[Casting Data in DTOs]]

Packages & Tools

[[spatie/data-transfer-object Package]]
[[spatie/laravel-data Package]]
[[PHP 8 Attributes for DTOs]]
[[DocBlock Type Hints vs Typed Properties]]

Testing DTOs

[[Testing DTO Mapping]]
[[Testing DTO Type Safety]]
[[DTO Factory Classes for Tests]]

Advanced Patterns

[[DTOs in Domain Layer vs Application Layer]]
[[Transforming DTOs for Different Contexts]]
[[DTOs and API Resources]]
[[Handling Optional DTO Properties]]
[[Default Values in DTOs]]

Common Pitfalls

[[DTO Constructor Complexity]]
[[Application Logic Leaking into DTOs]]
[[Over-engineering with DTOs]]
[[DTO Serialization Issues]]


Related Topics

[[Actions Pattern]] - DTOs are typically consumed by actions
[[Request Validation]] - Validation happens before DTO creation
[[View Models]] - Similar pattern but for presenting data to views
[[Eloquent Models]] - Different purpose: persistence vs transport
[[Type Safety in PHP]] - Broader context for why DTOs help


Questions to Explore

How do DTOs reduce cognitive load compared to arrays?
When should you use DocBlocks vs typed properties?
What's the difference between a DTO and a Value Object?
Should DTOs live in the domain or application layer?
How do you handle complex nested data structures with DTOs?
What's the trade-off between flexibility and structure?


Practical Examples to Build

 Create a CustomerData DTO with typed properties
 Implement a fromRequest() factory method
 Build a nested DTO structure (Invoice → InvoiceLines)
 Compare array-based vs DTO-based controller code
 Write tests for DTO mapping edge cases
 Refactor an existing array-heavy controller to use DTOs
