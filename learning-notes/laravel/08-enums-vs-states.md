Introduction
Enums and states both represent a fixed set of values, but they serve different purposes. Enums are simple value collections with basic behavior, while states represent complex behavior that changes based on value. Knowing when to use each pattern prevents over-engineering while keeping code maintainable.
Knowledge Points
Understanding Enums

[[What are Enums]]
[[Enums as Type-Safe Constants]]
[[Native PHP Enums (8.1+)]]
[[Enum Methods]]
[[Backed Enums vs Pure Enums]]

Enum Packages

[[myclabs/php-enum]]
[[spatie/enum]]
[[Comparing Enum Implementations]]
[[Native Enums vs Packages]]

Enum Patterns

[[Enum in Database Storage]]
[[Enum Casting in Eloquent]]
[[Enum Methods for Simple Logic]]
[[Enum Labels and Metadata]]
[[Enum Collections]]

When to Use Enums

[[Simple Value Collections]]
[[Minimal Conditional Logic]]
[[Enum as Configuration]]
[[Enum vs Constants]]

When to Use States

[[Complex State-Dependent Behavior]]
[[State Transitions and Validation]]
[[State-Specific Business Rules]]
[[Eliminating Conditionals]]

Comparing Approaches

[[Enum with Match vs State Classes]]
[[Complexity Thresholds]]
[[Refactoring Enums to States]]
[[Pragmatism vs Purity]]

Implementation Examples

[[Enum for Invoice Types]]
[[State for Invoice Status]]
[[Hybrid Approaches]]

Related Topics
[[State Pattern]], [[Type Systems]], [[Domain Models]]
Questions to Explore

At what point does an enum need to become states?
Can you use both enums and states in the same model?
How do native PHP enums change the decision?
What's the cost of over-engineering with states?

Practical Examples

 Create an enum for UserRole
 Refactor an enum with complex logic to states
 Compare native enum vs spatie/enum
 Build a decision matrix for enum vs state
