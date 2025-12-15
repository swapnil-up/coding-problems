Introduction
Domain layer testing focuses on business logic in isolation. DTOs need validation of mapping logic, actions need unit tests with mocked dependencies, and models need tests for custom behavior. Factories make setup easy, and the separation of concerns makes tests clear and fast.
Knowledge Points
Testing Philosophy

[[Unit vs Integration Tests]]
[[Testing Business Logic]]
[[Test Pyramid in Laravel]]
[[What to Test in Domain Layer]]

Testing DTOs

[[Testing DTO Creation]]
[[Testing DTO Mapping]]
[[Testing DTO Validation]]
[[Testing Invalid DTO Data]]
[[Minimal DTO Test Assertions]]

Testing Actions

[[Unit Testing Actions]]
[[Mocking Action Dependencies]]
[[Testing Action Composition]]
[[Testing Action Side Effects]]
[[Setup Execute Assert Pattern]]

Testing Models

[[Testing Custom Accessors]]
[[Testing Custom Mutators]]
[[Testing Model Casts]]
[[Testing Model Events]]
[[Database Fixtures for Model Tests]]

Testing Query Builders

[[Testing Query Builder Methods]]
[[Testing Query Scopes]]
[[Database Assertions]]

Testing Collections

[[Testing Collection Methods]]
[[Testing Collection Transformations]]
[[Collection Test Assertions]]

Testing State Classes

[[Testing State Behavior]]
[[Testing State Transitions]]
[[Testing State Validation]]
