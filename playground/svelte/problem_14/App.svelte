<script>
  let color = $state('#3b82f6');
  let keyLog = $state([]);
</script>

<div 
  class="swatch" 
  style:background={color} 
  style="height: 40px; width: 40px;"
></div>

<input type="color" value={color} oninput={(e) => color = e.target.value} />

<input 
  type="text" 
  placeholder="Press keys here..." 
  onkeydown={(e) => {
    const key = e.key; 
    if (keyLog.length < 5) {
      keyLog.push(key);
    } else {
      keyLog = [key];
    }
  }} 
/>

<ul data-testid="key-log">
  {#each keyLog as logItem}
    <li>{logItem}</li>
  {/each}
</ul>