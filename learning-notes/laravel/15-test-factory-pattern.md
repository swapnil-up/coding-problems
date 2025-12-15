Introduction
Test factories create model instances for tests with sensible defaults and flexibility. Unlike Laravel's default factories, the class-based factory pattern offers type safety, IDE support, immutability, and the ability to configure nested relationships. This makes test setup cleaner and more maintainable.
Knowledge Points
Factory Fundamentals

[[What are Test Factories]]
[[Laravel Factories vs Class-Based Factories]]
[[Factory as Test Helper]]
[[Factory Pattern Benefits]]

Factory Structure

[[Basic Factory Class]]
[[Static new() Constructor]]
[[Create vs Make Methods]]
[[Factory Method Naming]]

Immutability

[[Why Immutable Factories]]
[[Cloning Factory State]]
[[Avoiding Side Effects]]
[[Factory Reusability]]

Configuration

[[Fluent Configuration Methods]]
[[Factory States]]
[[Overriding Defaults]]
[[Random vs Fixed Data]]

Nested Factories

[[Factories Within Factories]]
[[Configuring Nested Factories]]
[[Relationship Setup]]
[[Complex Object Graphs]]

Factory Composition

[[Reusing Factory Logic]]
[[Base Factory Classes]]
[[Factory Traits]]
[[Abstract Factory Patterns]]

Laravel Integration

[[Factories for DTOs]]
[[Factories for Requests]]
[[Factories for Models]]
[[Database Seeding with Factories]]

Advanced Patterns

[[Factories with times()]]
[[Conditional Factory State]]
[[Factory Sequences]]
[[Factory Callbacks]]

Best Practices

[[Unique Values in Factories]]
[[Factory Organization]]
[[When to Use Factories]]
[[Factory Performance]]

Related Topics
[[Testing Strategy]], [[DTOs]], [[Domain Models]]
Questions to Explore

How do factories improve test readability?
When should you use Laravel factories vs custom factories?
How do you handle complex nested relationships?
Should factories be in tests/ or src/?

Practical Examples

 Create an InvoiceFactory with immutable state
 Build nested InvoiceFactory with InvoiceLineFactory
 Create a UserFactory with different roles
 Write a base factory class for reuse
