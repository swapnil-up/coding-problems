# TIL Learning Guide: Junior → Mid-Level Growth (AI Generated)

**Your Writing Style:** Problem → Personal Experience → Reflection → Actionable Takeaway. Write from real scenarios you've hit, not textbook theory. Keep it candid and direct.

---

## Systems Design & Scalability

The bridge between feature-focused coding and thinking about how systems actually behave under load.

- Why N+1 queries destroy your API response time
- Pagination patterns: offset vs cursor-based pagination when it actually matters
- Caching strategies: what Laravel (and Vue state) taught me about cache invalidation
- Database indexing: the time I added one index and saved 45 seconds per query
- Load balancing concepts: what happens when one server isn't enough
- Connection pooling: why your database connections are timing out in production
- API versioning strategies: the breaking change I almost shipped

---

## Testing & Reliability

From "it works on my machine" to confidence in deployments.

- Unit testing Laravel models: where the boundary actually is
- Integration tests that don't make you want to quit
- Testing async jobs: making sure background tasks don't silently fail
- Debugging production issues: reading logs when you can't run a debugger
- Error handling patterns: catching exceptions vs letting them bubble
- Test data factories: why fixtures are a pain and factories aren't
- Flaky tests and race conditions: the test that passes sometimes

---

## Performance & Optimization

Turning "it works" into "it works *fast*".

- Lazy loading in Vue: when components actually slow down your app
- Query optimization: GROUP BY, subqueries, and when to denormalize
- Frontend bundle size: the JavaScript death by a thousand imports
- Memory leaks in long-running processes: Kotlin background services that eat RAM
- Premature optimization vs real bottlenecks: measuring before guessing
- Batch processing: why looping through 10,000 records kills your database
- Frontend rendering: virtual scrolling when lists get too big

---

## Security Fundamentals

The things you need to know before they become incidents.

- CSRF tokens in SPAs: Vue + Laravel form authenticity
- XSS vulnerabilities: where templating saves you and where it doesn't
- SQL injection: why parameterized queries matter (and when Laravel does it for you)
- Authentication vs authorization: the permission system I built wrong the first time
- Secret management: where API keys should and shouldn't go
- CORS: why your Vue app can't talk to that API
- Input validation: server-side vs client-side and why both matter

---

## Async Patterns & Concurrency

Non-blocking code and handling things that take time.

- Laravel queues: when background jobs actually matter vs when they're overkill
- Race conditions: the job that ran twice and we didn't notice
- Promise chains vs async/await in Vue: which one won't make you regret your choices
- Timeout handling: what happens when an external API is slow
- Reactive state in Vue: managing async data without losing your mind
- Kotlin coroutines: async patterns on mobile that don't freeze the UI
- Throttling vs debouncing: the search input that hammered your database

---

## Code Quality & Architecture

Patterns that scale and decisions that matter.

- The abstraction trap: when extracting a method actually makes code harder to read
- Naming things: the variable name that took 30 minutes to get right
- Service vs repository pattern: which Laravel architecture actually works
- Composition vs inheritance: when Vue mixins make sense and when they don't
- Single responsibility: the 500-line method that needs to die
- Dependency injection: why it's worth learning even as a junior
- Domain logic vs framework code: keeping business rules independent

---

## Refactoring & Technical Debt

Changing code safely when the bus factor is you.

- The refactoring pattern that saved us 3 hours of debugging
- How to refactor without breaking things: the test-driven approach
- Incremental refactoring: small safe changes vs the big rewrite
- Identifying technical debt: knowing what to fix vs what to live with
- Legacy code patterns: how to work in a codebase written before you existed
- Feature branches vs trunk-based development: the workflow that matters
- Dead code: why you should delete it even if it might be useful later

---

## Vue.js Patterns

Frontend architecture and state management.

- Vue 3 Composition API: the mental model switch from Options API
- State management: Pinia vs prop drilling vs something simpler
- Component design: when to split, when to combine, when to use slots
- Form handling in Vue: controlled components and validation that doesn't suck
- Re-renders and performance: why your component updates everything
- Testing Vue components: when snapshot tests lie to you
- Real-time updates: handling WebSocket data in component state

---

## Laravel Patterns

Backend architecture, service patterns, and thinking in requests/responses.

- Service providers: the Laravel magic that initializes your whole app
- Middleware chains: request → middleware → response as a mental model
- Event listeners: when to use them vs when you're over-engineering
- Model relationships: N+1 queries hiding in eager loading
- Query scopes: making queries readable and reusable
- Form requests: validation logic that doesn't live in controllers
- Eloquent query builder: when to use raw SQL vs when the query builder is enough

---

## Kotlin & Mobile Fundamentals

Mobile development patterns and Android-specific thinking.

- Lifecycle management: why your Activity data disappeared
- Coroutines vs RxJava: async patterns on Android that make sense
- Dependency injection in Kotlin: Hilt vs manual vs too much ceremony
- Fragment state: the screen rotation that reset your data
- Memory management: why Kotlin references matter in long-running apps
- Testing on Android: emulator vs real device and what you can't test either way
- Threading: when the main thread blocks your entire app

---

## Collaboration & Communication

The non-code skills that separate mid-level from senior.

- Code review culture: giving feedback without being a jerk
- Handling technical debt conversations: persuading non-technical people to care
- Architecture discussions: convincing the team without being prescriptive
- Documentation: when to write it, when it becomes a lie
- Mentoring juniors: how to explain something without just giving the answer
- Disagreement: staying professional when someone's approach feels wrong
- On-call and production incidents: staying calm when things break

---

## Debugging & Problem-Solving

The mindset and techniques for finding what's broken.

- Reading stack traces: extracting signal from the noise
- Rubber duck debugging: explaining your code to find the bug
- Reproduction steps: making the bug happen consistently so you can fix it
- Logs analysis: what to log so production issues are solvable
- Breakpoints vs logging: when to use which tool
- Binary search debugging: eliminating half the possibilities each time
- External dependencies failing: database down, API timeout, what then?

