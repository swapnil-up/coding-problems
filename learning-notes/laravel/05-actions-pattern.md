Introduction
Actions are classes that encapsulate a single piece of business logic. They represent user stories ("create an invoice", "send a notification") as first-class citizens in your codebase. Actions keep controllers thin, enable reusability, and make testing straightforward by isolating business logic from infrastructure concerns.
Knowledge Points
Core Concepts

[[What is an Action]]
[[Actions vs Fat Models]]
[[Actions vs Service Classes]]
[[Actions vs Commands and Handlers]]
[[Single Responsibility in Actions]]

Naming and Structure

[[Action Naming Conventions]]
[[Execute vs Handle vs Invoke]]
[[Action Suffixes]]
[[One Public Method Rule]]

Dependency Injection

[[Constructor Injection in Actions]]
[[Why Not Method Injection for Actions]]
[[Injecting Actions into Actions]]
[[Service Location vs Dependency Injection]]

Composition

[[Composing Actions from Other Actions]]
[[Avoiding Deep Action Chains]]
[[When to Split Actions]]
[[When to Merge Actions]]

Reusability

[[Action Reusability Patterns]]
[[Context-Specific vs Generic Actions]]
[[Premature Abstraction in Actions]]

Integration

[[Actions in Controllers]]
[[Actions in Jobs]]
[[Actions in Commands]]
[[Actions in Event Listeners]]

Test Helpers

[[Using Factories in Tests]]
[[Test Database Setup]]
[[Mocking External Services]]
[[Testing Time-Dependent Logic]]

Best Practices

[[Arrange Act Assert Pattern]]
[[Test Naming Conventions]]
[[Test Organization]]
[[When to Mock vs Use Real Objects]]

Related Topics
[[Test Factory Pattern]], [[Actions Pattern]], [[Domain Models]]
Questions to Explore

How much should you test in isolation vs integration?
When should you use database transactions in tests?
How do you test complex action chains?
Should domain tests use the database?

Practical Examples

 Write comprehensive tests for CreateInvoiceAction
 Test DTO mapping from different sources
 Test custom collection methods
 Test state transitions with edge cases
