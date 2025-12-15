Introduction
Large Laravel projects often have multiple applications - an admin panel, public API, customer portal, and console commands. Each is a separate application layer that uses the same domain code. Understanding how to structure and share code between applications prevents duplication while maintaining clear boundaries.
Knowledge Points
Multiple Application Concept

[[What Constitutes an Application]]
[[HTTP vs Console vs API Applications]]
[[Application Independence]]
[[Shared Domain Layer]]

Application Types

[[Admin Applications]]
[[Public Web Applications]]
[[REST API Applications]]
[[Console Applications]]
[[Third-Party Integrations as Applications]]

Application Structure

[[Organizing Multiple Applications]]
[[Application Namespaces]]
[[Application Folder Structure]]
[[Route Organization per Application]]

Sharing Code

[[Shared Domain Code]]
[[Application-Specific Code]]
[[Shared Support Code]]
[[When to Share vs Duplicate]]

Configuration

[[Per-Application Configuration]]
[[Shared Configuration]]
[[Environment Variables]]
[[Application-Specific Service Providers]]

Authentication & Authorization

[[Different Auth per Application]]
[[Shared User Models]]
[[Application-Specific Guards]]
[[API Authentication]]

Routing

[[Separate Route Files]]
[[Route Prefixes]]
[[Subdomain Routing]]
[[API Versioning]]

Middleware

[[Application-Specific Middleware]]
[[Shared Middleware]]
[[Middleware Groups]]

Views & Resources

[[Separate View Directories]]
[[Shared Blade Components]]
[[API Resources per Application]]

Testing Strategy

[[Testing Per Application]]
[[Shared Test Helpers]]
[[Application-Specific Test Suites]]

Related Topics
[[Application Modules]], [[Domain Organization]], [[Controllers]]
Questions to Explore

How do you prevent code duplication between applications?
Should applications share controllers?
How do you handle versioning across applications?
When should you split into separate Laravel installations?

Practical Examples

 Create separate Admin and API applications
 Share authentication between applications
 Build application-specific middleware
 Document application boundaries
