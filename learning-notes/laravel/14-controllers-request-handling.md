Introduction
In domain-oriented Laravel, controllers are thin coordinators. They receive HTTP requests, delegate to domain actions, and return responses. Business logic doesn't belong here - controllers are part of the application layer, handling the HTTP infrastructure.
Knowledge Points
Controller Philosophy

[[Thin Controllers]]
[[Controllers as Coordinators]]
[[Controllers in Application Layer]]
[[What Belongs in Controllers]]

Controller Structure

[[RESTful Resource Controllers]]
[[Single Action Controllers]]
[[Invokable Controllers]]
[[When to Use Each Type]]

Request Handling

[[Form Requests]]
[[Request Validation]]
[[Request Authorization]]
[[Custom Request Classes]]

Delegating to Domain

[[Injecting Actions in Controllers]]
[[Creating DTOs from Requests]]
[[Calling Actions from Controllers]]
[[Handling Action Results]]

Response Patterns

[[Returning Views]]
[[Returning JSON]]
[[Response Macros]]
[[Response Resources]]

Middleware

[[Controller Middleware]]
[[Route Middleware]]
[[Global Middleware]]
[[Custom Middleware]]

Testing Controllers

[[HTTP Tests]]
[[Testing Controller Flow]]
[[Mocking Action Dependencies]]
[[Testing Validation Rules]]

Advanced Patterns

[[Dependency Injection in Controllers]]
[[Route Model Binding]]
[[Controller Concerns]]
[[API Controllers vs Web Controllers]]

Related Topics
[[Actions Pattern]], [[View Models]], [[Application Modules]]
Questions to Explore

How thin is "thin enough" for a controller?
Should DTOs be created in controllers or requests?
How do you handle complex authorization?
When should you split a controller?

Practical Examples

 Refactor a fat controller to thin controller + actions
 Create a resource controller with proper separation
 Build a form request with complex validation
 Write HTTP tests for controller flow
