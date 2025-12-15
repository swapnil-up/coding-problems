Introduction
In domain-oriented Laravel, models have a focused responsibility: representing and persisting data. Business logic lives elsewhere (actions, states, domain services). This keeps model classes manageable and prevents them from becoming thousand-line monsters. We embrace Eloquent's features while being careful about what we add.
Knowledge Points
Philosophy

[[Models as Data Providers]]
[[Fat Models Anti-pattern]]
[[Models vs Business Logic]]
[[Anemic Domain Model Debate]]
[[Alan Kay's View on OOP]]

Model Responsibilities

[[What Belongs in a Model]]
[[Data Representation in Models]]
[[Simple Accessors and Mutators]]
[[Casting Data Types]]
[[Model Relationships]]

Extracting from Models

[[Moving Scopes to Query Builders]]
[[Custom Collection Classes]]
[[Custom Query Builder Classes]]
[[Model Subscribers for Events]]
[[Computed Properties vs Actions]]

Custom Query Builders

[[Creating Custom Query Builders]]
[[Named Scopes vs Query Builder Methods]]
[[Type Safety in Query Builders]]
[[Query Builder Reusability]]

Custom Collections

[[Creating Custom Collection Classes]]
[[Collection Methods for Domain Logic]]
[[Type-hinted Collections]]
[[When to Use Collections vs Actions]]

Model Events

[[Eloquent Event System]]
[[Model Observers]]
[[Dispatching Domain Events from Models]]
[[Event Subscribers]]

Calculated Properties

[[Calculating vs Storing Data]]
[[Database-Driven Calculations]]
[[Accessors for Simple Transformations]]
[[When to Pre-calculate]]

Related Topics
[[Actions Pattern]], [[State Pattern]], [[Domain Events]], [[Query Builders]]
Questions to Explore

Where do you draw the line between model and action responsibility?
How do you handle complex calculated properties?
When should logic be in a collection vs an action?
How do you prevent models from growing over time?

Practical Examples

 Create a custom query builder for Invoice
 Build a custom collection with domain methods
 Extract model scopes to a query builder class
 Refactor a fat model using actions
