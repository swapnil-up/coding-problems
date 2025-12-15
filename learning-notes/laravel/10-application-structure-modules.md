Introduction
Just as domains organize business logic, application modules organize infrastructure code by feature. Instead of "all controllers together", we group invoice controllers, requests, resources, and queries in an Invoices module. This prevents the application layer from becoming an unnavigable mess in large projects.
Knowledge Points
Application Layer Philosophy

[[Application vs Domain Separation]]
[[Application as Infrastructure]]
[[Multiple Applications in One Project]]
[[HTTP vs Console vs API Applications]]

Module Structure

[[What is an Application Module]]
[[Grouping by Feature Not Type]]
[[Module Folder Structure]]
[[Cross-Module Dependencies]]
[[Shared Application Code]]

Module Organization

[[Identifying Module Boundaries]]
[[Module Size Guidelines]]
[[When to Split Modules]]
[[When to Merge Modules]]

Application Components

[[Controllers in Modules]]
[[Requests and Validation in Modules]]
[[Resources and Transformers in Modules]]
[[Middleware in Modules]]
[[View Models in Modules]]

Global Application Code

[[Base Controllers and Requests]]
[[Global Middleware]]
[[The Support Namespace]]
[[Shared Utilities]]

Routing

[[Organizing Routes by Module]]
[[Route File Structure]]
[[Route Model Binding]]
[[Route Prefixes and Names]]

Real-World Example

[[Admin Module Structure]]
[[API Module Structure]]
[[Client Portal Module]]

Related Topics
[[Domain Organization]], [[View Models]], [[HTTP Queries]]
Questions to Explore

How do modules map to domains?
When should modules share code?
How do you prevent module coupling?
What goes in Support vs a module?

Practical Examples

 Reorganize a Laravel app by modules
 Create an Invoices module with all components
 Document module boundaries
 Refactor overlapping module code
