<script>
  let name = $state('');
  let age = $state(0);
  let plan = $state('free');
  let newsletter = $state(false);
  let interests = $state([]);
  let contactMethod = $state('email');
</script>

<input type="text" bind:value={name}/>
<input type="number" bind:value={age}/>
<select bind:value={plan}>
  <option value="free">Free</option>
  <option value="pro">Pro</option>
  <option value="enterprise">Enterprise</option>
</select>
<label>
  <input type="checkbox" bind:checked={newsletter}/>Subscribe to newsletter
</label>
<div>
  Interests:
  <input type="checkbox" bind:group={interests} value="coding">coding
  <input type="checkbox" bind:group={interests} value="design">design
  <input type="checkbox" bind:group={interests} value="drawing">drawing
</div>
<div>
  <input type="radio" bind:group={contactMethod} value="email"/>Email
  <input type="radio" bind:group={contactMethod} value="phone"/>Phone
  <input type="radio" bind:group={contactMethod} value="None"/>None
</div>

<div data-testid="preview">
  <p>name={name} age={age} plan={plan} newsletter={newsletter} interests={interests} contact={contactMethod}</p>
</div>