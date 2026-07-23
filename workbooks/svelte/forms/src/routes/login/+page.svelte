<script lang="ts">
	import LoginForm from './login-form.svelte';
	let { data } = $props();
</script>

<div class="flex min-h-screen items-center justify-center">
	<div class="w-full max-w-md p-6">
		<h1 class="mb-6 text-2xl font-bold">Login to your account</h1>
		<LoginForm data={data.form} />
	</div>
</div>
