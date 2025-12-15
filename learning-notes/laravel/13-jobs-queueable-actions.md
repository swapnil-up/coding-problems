Introduction
Jobs manage asynchronous work in Laravel, but they shouldn't contain business logic - that belongs in actions. Jobs configure queue behavior (retries, delays, chains) while actions handle the actual work. This separation keeps both clean and testable.
Knowledge Points
Job Fundamentals

[[What are Jobs]]
[[Jobs vs Actions Responsibility]]
[[Jobs as Infrastructure]]
[[Queue Configuration]]

Queue Concepts

[[Synchronous vs Asynchronous Jobs]]
[[Job Queues and Workers]]
[[Job Serialization]]
[[Horizon for Queue Monitoring]]

Job Patterns

[[Simple Action Jobs]]
[[Job Middleware]]
[[Job Chaining]]
[[Batch Jobs]]
[[Job Delays and Scheduling]]

Queueable Actions

[[spatie/laravel-queueable-action]]
[[Actions with onQueue()]]
[[Queueable Action Benefits]]
[[When to Use Dedicated Jobs]]

Job Configuration

[[Max Retries]]
[[Retry Delays]]
[[Timeouts]]
[[Queue Selection]]
[[Job Rate Limiting]]

Error Handling

[[Failed Job Handling]]
[[Job Exceptions]]
[[Failed Job Notifications]]
[[Dead Letter Queues]]

Testing Jobs

[[Testing Queued Jobs]]
[[Faking Queues]]
[[Testing Job Chains]]
[[Testing Failed Jobs]]

Advanced Patterns

[[Job Uniqueness]]
[[Job Throttling]]
[[Conditional Dispatching]]
[[Job Events]]

Related Topics
[[Actions Pattern]], [[Domain Events]], [[Application Layer]]
Questions to Explore

When should you use a dedicated job vs queueable action?
How do you handle long-running jobs?
Should job logic be testable without the queue?
How do you monitor and debug failed jobs?

Practical Examples

 Create a SendInvoiceMailJob
 Convert an action to use onQueue()
 Build a job chain for multi-step process
 Handle failed job scenarios
