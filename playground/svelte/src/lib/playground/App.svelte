<script>
	// ==========================================
	// SVELTE 5 REACTIVITY CARD TESTING PLAYGROUND
	// ==========================================
	// Instructions:
	// 1. Uncomment ONE test block at a time
	// 2. Check the output in the browser
	// 3. Verify it matches the card's expected answer
	// 4. Comment it out and move to the next
	
	// ==========================================
	// $STATE BASICS
	// ==========================================
	
	// TEST 1: Reassignment on primitives
	// let count = $state(0);
	// count = 5;
	// Expected: UI shows 5
	
	// TEST 2: Array .push() mutation
	// let items = $state([1, 2, 3]);
	// items.push(4);
	// Expected: UI shows [1, 2, 3, 4]
	
	// TEST 3: Object property mutation
	// let user = $state({ name: 'Alice' });
	// user.name = 'Bob';
	// Expected: UI shows "Bob"
	
	// TEST 4: Increment operator
	// let count = $state(0);
	// count++;
	// Expected: UI shows 1
	
	// TEST 5: Reference copying
	// let obj = $state({ a: 1 });
	// let copy = obj;
	// copy.a = 2;
	// Expected: obj.a is now 2 (same reference)
	
	// ==========================================
	// DEEP STATE & DESTRUCTURING
	// ==========================================
	
	// TEST 6: Destructuring breaks reactivity
	// let state = $state({ count: 0 });
	// let { count } = state;
	// count++;
	// Expected: UI still shows 0 (destructured value is separate)
	
	// TEST 7: Nested property mutation
	// let user = $state({ name: 'Alice', age: 30 });
	// user.name = 'Bob';
	// Expected: UI shows "Bob"
	
	// TEST 8: Class instances NOT proxied
	// class Person {
	// 	constructor(name) { this.name = name; }
	// }
	// let person = $state(new Person('Alice'));
	// person.name = 'Bob';
	// Expected: UI still shows "Alice" (class not proxied)
	
	// TEST 9: Deep nested mutation
	// let data = $state({ nested: { value: 1 } });
	// data.nested.value = 2;
	// Expected: UI shows 2
	
	// TEST 10: Adding new properties
	// let obj = $state({ a: 1 });
	// obj.b = 2;
	// Expected: UI shows both a:1 and b:2
	
	// ==========================================
	// $STATE.RAW
	// ==========================================
	
	// TEST 14: .raw can contain $state
	// let obj1 = $state({ a: 1 });
	// let arr = $state.raw([obj1]);
	// obj1.a = 2;
	// Expected: UI shows a: 2 (obj1 is still reactive)
	
	// ==========================================
	// $STATE.SNAPSHOT
	// ==========================================
	
	// TEST 15: Snapshot creates separate copy
	// let obj = $state({ count: 0 });
	// let snap = $state.snapshot(obj);
	// snap.count++;
	// obj.count++;
	// obj.count++;
	// Expected: snap.count = 1, obj.count = 1 (separate)
	
	// ==========================================
	// $DERIVED
	// ==========================================
	
	// TEST 16: Basic derived
	// let count = $state(0);
	// let doubled = $derived(count * 2);
	// count = 5;
	// Expected: doubled = 10
	
	// TEST 17: Derived recalculates
	// let a = $state(1);
	// let b = $state(2);
	// let sum = $derived(a + b);
	// a = 5;
	// Expected: sum = 7
	
	// TEST 18: Don't wrap in arrow function
	// let count = $state(0);
	// let result = $derived(() => count * 2);
	// Expected: result is a FUNCTION, not a number (MISTAKE)
	
	// TEST 19: Array methods in derived
	// let arr = $state([1, 2, 3]);
	// let filtered = $derived(arr.filter(x => x > 1));
	// arr.push(4);
	// Expected: filtered = [2, 3, 4]
	
	// ==========================================
	// $EFFECT BASICS
	// ==========================================
	
	// TEST 20: Effect runs on mount and change
	// let count = $state(0);
	// $effect(() => {
	// 	console.log('count is:', count);
	// });
	// setTimeout(() => count = 5, 1000);
	// Expected: logs "count is: 0" immediately, then "count is: 5" after 1s
	
	// TEST 21: Effect with no deps runs once
	// $effect(() => {
	// 	console.log('runs once');
	// });
	// Expected: logs once on mount
	
	// TEST 22: Conditional reads still track
	// let a = $state(1);
	// let b = $state(2);
	// $effect(() => {
	// 	if (a > 0) console.log('b is:', b);
	// });
	// setTimeout(() => b = 10, 1000);
	// Expected: logs "b is: 2" on mount, then "b is: 10" after 1s
	
	// TEST 23: setTimeout reads are untracked
	// let count = $state(0);
	// $effect(() => {
	// 	setTimeout(() => console.log('count:', count), 100);
	// });
	// setTimeout(() => count = 5, 50);
	// Expected: only logs "count: 5" once (not reactive)
	
	// TEST 24: Read outside setTimeout to track
	// let count = $state(0);
	// $effect(() => {
	// 	const val = count;
	// 	setTimeout(() => console.log('val:', val), 100);
	// });
	// setTimeout(() => count = 5, 50);
	// Expected: logs "val: 0" after 100ms, then "val: 5" after another run
	
	// ==========================================
	// $EFFECT CLEANUP
	// ==========================================
	
	// TEST 25: Cleanup runs before re-run
	// let count = $state(0);
	// $effect(() => {
	// 	console.log('setup', count);
	// 	return () => console.log('cleanup', count);
	// });
	// setTimeout(() => count++, 1000);
	// Expected: "setup 0" → (after 1s) → "cleanup 0" → "setup 1"
	
	// ==========================================
	// ACTIVE TEST (uncomment to run)
	// ==========================================
// 	let count = $state(0);
// $inspect(count).with((type, val) => {
//   if (typeof window !== 'undefined') {
//     alert(val);
//   }
// });
// count++;

let obj = $state({ a: 1 });
$inspect(obj.a);
obj.a = 2;
</script>

<div class="container">
	<h1>Svelte 5 Reactivity Test Playground</h1>
	
	<div class="instructions">
	</div>
	
	<div class="test-output">
		<h3>Current Test Output:</h3>
		<!-- <p>Count: {arr} {filtered}</p> -->
		<!-- <button onclick={increment}>Increment (for manual testing)</button> -->
	</div>
	
	<div class="console-note">
		💡 Many tests use <code>console.log()</code> — open your browser's DevTools Console (F12)
	</div>
</div>

<style>
	.container {
		max-width: 800px;
		margin: 2rem auto;
		padding: 2rem;
		font-family: system-ui, -apple-system, sans-serif;
	}
	
	h1 {
		color: #ff3e00;
		margin-bottom: 1rem;
	}
	
	.instructions {
		background: #f0f0f0;
		padding: 1.5rem;
		border-radius: 8px;
		margin-bottom: 2rem;
	}
	
	.instructions h2 {
		margin-top: 0;
		font-size: 1.2rem;
	}
	
	.instructions ol {
		margin-bottom: 0;
	}
	
	.instructions li {
		margin-bottom: 0.5rem;
	}
	
	.test-output {
		background: #e8f5e9;
		padding: 1.5rem;
		border-radius: 8px;
		margin-bottom: 1rem;
	}
	
	.test-output h3 {
		margin-top: 0;
		color: #2e7d32;
	}
	
	.test-output p {
		font-size: 1.5rem;
		font-weight: bold;
		margin: 1rem 0;
	}
	
	button {
		background: #ff3e00;
		color: white;
		border: none;
		padding: 0.75rem 1.5rem;
		border-radius: 4px;
		font-size: 1rem;
		cursor: pointer;
		transition: background 0.2s;
	}
	
	button:hover {
		background: #cc3100;
	}
	
	.console-note {
		background: #fff3e0;
		padding: 1rem;
		border-radius: 8px;
		border-left: 4px solid #ff9800;
	}
	
	code {
		background: #f5f5f5;
		padding: 0.2rem 0.4rem;
		border-radius: 3px;
		font-family: 'Courier New', monospace;
	}
</style>