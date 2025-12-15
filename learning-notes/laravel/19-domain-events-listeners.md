Introduction
Domain events represent something meaningful that happened in your domain - "InvoicePaid", "OrderShipped". Listeners respond to these events, often triggering side effects like sending emails or updating related data. This pattern keeps actions focused and makes side effects explicit and testable.
Knowledge Points
Domain Event Concepts

[[Domain Events Represent Past Facts]]
[[Events vs Commands]]
[[Event Naming - Past Tense]]
[[Event Granularity]]

Creating Domain Events

[[Event Class Structure]]
[[Event Properties]]
[[Event Serialization]]
[[Immutable Events]]

Event Payload

[[What Data to Include in Events]]
[[Full Models vs IDs in Events]]
[[Event DTOs]]
[[Enriching Events]]

Dispatching Events

[[From Actions]]
[[From Models]]
[[From Event Subscribers]]
[[Conditional Dispatching]]

Creating Listeners

[[Listener Class Structure]]
[[Listener Handle Method]]
[[Injecting Dependencies in Listeners]]
[[Queued vs Synchronous Listeners]]

Listener Patterns

[[Listeners Call Actions]]
[[Listeners for Side Effects]]
[[Cross-Domain Listeners]]
[[Listener Middleware]]

Model Events

[[Eloquent Events]]
[[Custom Model Events]]
[[Model Observers]]
[[Model Event Subscribers]]
[[Remapping Generic to Specific Events]]

Event Registration

[[Auto-Discovery]]
[[Manual Registration]]
[[Event Service Provider]]
[[Subscriber Registration]]

Testing

[[Testing Event Dispatch]]
[[Testing Listener Logic]]
[[Testing Event Payload]]
[[Faking Events in Tests]]

Advanced Patterns

[[Event Sourcing Integration]]
[[Event Replay]]
[[Event Store]]
[[Transactional Events]]

Related Topics
[[Event-Driven Architecture]], [[Actions Pattern]], [[Domain Models]]
Questions to Explore

Should events contain full models or just IDs?
How do you handle events that need to be ordered?
When should listeners be queued?
How do you prevent event listener coupling?

Practical Examples

 Create InvoicePaid event with listeners
 Build a subscriber for invoice events
 Remap model events to domain events
 Test event-listener workflows
