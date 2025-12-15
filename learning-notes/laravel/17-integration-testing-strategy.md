Introduction
Integration tests verify that different parts of your application work together correctly. In domain-oriented Laravel, this means testing the full flow from HTTP request through actions to database and back. These tests complement unit tests by catching integration issues while remaining fast and maintainable.
Knowledge Points
Integration Testing Philosophy

[[Unit vs Integration Tests Trade-offs]]
[[Testing Collaborations]]
[[Test Boundaries]]
[[How Much Integration Testing]]

HTTP Integration Tests

[[Testing Full Request Flow]]
[[Testing Controller to Action Flow]]
[[Testing Database Persistence]]
[[Testing Response Formats]]

Testing Patterns

[[Feature Test Structure]]
[[Testing Happy Paths]]
[[Testing Edge Cases]]
[[Testing Error Scenarios]]

Database Testing

[[Database Transactions in Tests]]
[[Database Refresh Strategies]]
[[Testing Database Constraints]]
[[Testing Complex Queries]]

Authentication Testing

[[Acting as Users]]
[[Testing Authorization]]
[[Testing Middleware]]
[[Testing Guards]]

Testing External Services

[[Mocking HTTP Clients]]
[[Faking Mail]]
[[Faking Queues]]
[[Faking Storage]]

Test Data Management

[[Using Factories in Integration Tests]]
[[Database Seeders for Tests]]
[[Cleaning Up Test Data]]
[[Shared Test State]]

Performance

[[Keeping Tests Fast]]
[[Parallel Testing]]
[[Selective Test Running]]
[[Test Database Optimization]]

Advanced Patterns

[[Testing Job Chains]]
[[Testing Event Flows]]
[[Testing State Transitions End-to-End]]
[[Testing File Uploads]]

Related Topics
[[Testing Domain Layer]], [[Test Factories]], [[Controllers]]
Questions to Explore

Where do you draw the line between unit and integration tests?
How do you test workflows that span multiple domains?
Should integration tests use real or fake external services?
How do you maintain integration test speed?

Practical Examples

 Write a full feature test for invoice creation
 Test a multi-step workflow end-to-end
 Test PDF generation and email sending
 Build a test suite with good coverage
