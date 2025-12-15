Introduction
Event-driven architecture decouples different parts of your application by using events as the communication mechanism. Instead of Action A directly calling Action B, Action A dispatches an event that Action B listens for. This adds flexibility but also indirection - use it wisely in larger systems where coupling becomes a problem.
Knowledge Points
Event Fundamentals

[[What are Domain Events]]
[[Events vs Direct Calls]]
[[Event-Driven vs Action-Driven]]
[[When to Use Events]]
[[Event Coupling Trade-offs]]

Laravel Events

[[Event and Listener System]]
[[Event Discovery]]
[[Event Subscribers]]
[[Queued Listeners]]

Domain Events

[[Domain Events vs Framework Events]]
[[Creating Domain Event Classes]]
[[Event Payload Design]]
[[Event Naming Conventions]]

Event Dispatching

[[Dispatching Events from Actions]]
[[Dispatching Events from Models]]
[[Event Middleware]]
[[Conditional Event Dispatching]]

Event Listeners

[[Creating Listeners]]
[[Listener Responsibility]]
[[Listener as Action Wrapper]]
[[Multiple Listeners Per Event]]

Event Subscribers

[[Subscriber Pattern]]
[[Organizing Related Listeners]]
[[Subscriber Priority]]

Event Sourcing

[[Event Sourcing Basics]]
[[Event Store Concept]]
[[Rebuilding State from Events]]
[[When to Use Event Sourcing]]
[[Event Sourcing vs Domain Events]]

Testing Events

[[Testing Event Dispatch]]
[[Faking Events]]
[[Testing Listeners]]
[[Testing Event Flow]]

Patterns

[[Event Chains]]
[[Saga Pattern]]
[[Event Broadcasting]]
[[Event Versioning]]

Considerations

[[Event Complexity]]
[[Debugging Event Flows]]
[[Event Documentation]]
[[Over-Engineering with Events]]

Related Topics
[[Actions Pattern]], [[Domain Models]], [[Jobs]]
Questions to Explore

When should you use events vs direct action calls?
How do you debug complex event chains?
Should events cross domain boundaries?
How do you version events over time?

Practical Examples

 Create an InvoiceCreated domain event
 Build listeners for invoice workflow
 Replace direct calls with events in a workflow
 Test an event-driven feature
