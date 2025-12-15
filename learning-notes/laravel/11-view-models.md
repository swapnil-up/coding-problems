Introduction
View models prepare data specifically for views, keeping controllers thin and avoiding logic in Blade templates. They encapsulate all data fetching, transformation, and presentation logic in one place, making it reusable across different controllers and easy to test.
Knowledge Points
View Model Fundamentals

[[What is a View Model]]
[[View Models vs Controllers]]
[[View Models vs View Composers]]
[[Data Providers for Views]]

Structure and Patterns

[[View Model Class Structure]]
[[Constructor Injection]]
[[Public Methods as View Data]]
[[Lazy-Loading in View Models]]

Laravel Integration

[[Arrayable Implementation]]
[[Responsable Implementation]]
[[Passing View Models to Views]]
[[View Model Factories]]

Advanced Patterns

[[Nested View Models]]
[[View Models with Resources]]
[[Paginated Data in View Models]]
[[View Models for AJAX Responses]]

Reusability

[[Sharing View Models Across Actions]]
[[View Models for Forms]]
[[Create vs Edit View Models]]
[[Polymorphic View Models]]

Testing

[[Testing View Models]]
[[Mocking Dependencies]]
[[Asserting View Model Data]]

Comparison

[[View Models vs View Composers]]
[[View Models vs Resources]]
[[When to Use Each Approach]]

Related Topics
[[Controllers]], [[Application Modules]], [[Resources]]
Questions to Explore

When should data fetching happen in controller vs view model?
How do you handle authorization in view models?
Should view models handle caching?
How do you test complex view models?

Practical Examples

 Create a PostFormViewModel
 Build a dashboard view model with multiple data sources
 Implement Arrayable and Responsable
 Refactor a controller to use view models
