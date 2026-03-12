<script>
  let {name, role, avatarUrl}=$props();
</script>

<div class="user-card">
  <img src={avatarUrl} alt={name}/>
  <h3>{name}</h3>
  <p>{role}</p>
</div>