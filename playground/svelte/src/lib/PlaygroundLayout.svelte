<script lang="ts">
	import favicon from '$lib/assets/favicon.svg';

	let { children } = $props();
	const title = 'Hello world (edited)';
	const href = 'https://svelte.dev/playground/hello-world?version=5.53.0#H4sIAAAAAAAAA61Z727bOBJ_lTlfsbGvsSPZybVV3ABp4m6D6yZB4vSwqPuBkmibW0kURCqOLwhwn-4BFvf9cK-2T3CPcEOKkmVZdpyk2wWSkDPDmd_8JXXfiEhIG07jEw0CDjOeBD40qc8k9VuN3caYBVQ0nK_3DTmPFZ1awHXDdRzHHXFLA6nWXCJo3brHI0kjiWIafeElLJZHo2gk9_bg_db_GYbrL4PPwwEcwNXg-GR49uVs-CucHF-dwnBwPTw7_xkuPx__-vPVxc356XOPOIuETFJPMh4Jx6zZHbiJPB6GaAZcnA9AUiHBDbj3HYgEApKF1NB2O3AypbghpxR4KuNUAov0X27CZ4ImhrDXgS80YeM5MAkhkd6UCk3mkcTfEUDvYuqhG4BEYlZw7aN4owiyoXzc9iHktxQk1-wRvZOK-LkAvLoeHiPGH46vz06unyXEMCmfgO3AFSVCsEmkleYRxAkLmWS3VBjCgErweIq77-GVkETSptU6NJv5xkG-MDC4OHBzBmKKkMJB9dSuA8dJQubQiVMxbbYgTFEsurR0IoZ4KBYnfrV3obsLvW_FyZogE7Df2nB6zrkL-9-qivQcuHB_Qw60msc0kfMlVZQeKYbEQo17UCnkwM5xwDy6Aw_FyYquozaReOcDd3c2qDRqIMGoUdVm38Hw9hKaeQLVIZInWzvh9esNJ9rVsw6U48c0oZGHIc3jOYsmpaO4-1vZaOKAXbI1UyaeIwkSLrSI5x2Ca91VRZAMt5iAiM-gC02hgEpyBVovSYjTweASsqT4Cf-4Hl7dnAxvrrDcvDg7_urAKc3qTZogQFgiKPkuUHGCFeiWyXkJEI1VGTTtFQesCnBmAx6QVpNu5UXJgsD40oKmX2iFBeiWBClV2AoaE4yZJTi1HW8cOEcOpK0Nc6PYxkjfBTLBv3rWjw35tw6cBFh_sAbjsRgKAs4vhkrNO0b9HBhNcUkTgeXp3iyOJDauDAWeNJUWLYRWTpnIVVI_DuHB0D-ULI0zUYWtEZ0Z8U1jbqswMqPdwsySh0YNLWXUgGame8RlbtOKc96pIKMxNgbtoRrH-ESSJcdoSgfN1a7XuVlyiyLvZDSdLDZqU7JwTXelKVhYn31fBbxCxsQMW2oImwuESnf3kWNdLqfIZ-sO6TplLZ5cA7Km2Lk6_vvLOyK2xE5CZuBzKqIdCTIhOC5UvFOGYrlTKd7m13tgvoak0q--Wt86zF-PTCmItIAV7bpGu9OLwbVRLSk18EfUUq2wohFSFL11iy660kLtntFopbTAmLBArItjrdA9uGyCNYbrJrxTDWLcVDnnTUk0of42eZcJWq0z9r7R0iMRqImX4NCXKbIc1PYjbY8kSQVTxfStHPn2uiZYgIlysQfq01TZ1haYnvKyXmjy4Pr8-PL608Xw5cmAY8J1RGJUGzs-qoiTddFmdMNfXxLWtD-B4hYICiNcgVGQqcVOpRuqirK2QS4YUDIGakGs_sRho6YvPh3a08HV2ZfB8y4uS5jiVPGBCOaBj_eL26LLbZzwdPrw1A2oKh6vDGczo_8LdLeZxxf8trWi1BvVhbRQjESPBF4aKGeXI3-hl72kl7vY6C67Og3LyhJ4DW5BQOqVzHjerOiHg8IpV-V4lmD8YPJiIuIoOU4jr9ItN2KYUJEGsqwV3j7eH8EqkAuVDA9mKoGPN-d4sb0439UtnUCUhi5OTc1fzjDz_jZYae72u_yqE1I55b4adGr8Xq4qNVcdRYI3e0mTZfcjWydbb94pK-7gCOzF6KK2196PSvK-1lyPnp4fg48fByfDH3Ux7eIMMhiP1dUsSSOhLqah9pGaFrKGsI3PX1Etw3h5eXbkAe0EfNLcybiZcHDK1b8X7IvSJagcspDijX4pYjCGdzGdLKsGYZStWlIhHSwcCFkYUp-hksF8V70HREsUB0hBxugXsMUKInaByIzh6BRxDKRY5PB49CkmF0w7NbZWTFBkBf4rWuFAcsIjn6ksJLqN-XlL0-PJsyvIOjvYGLCUHIHVgiWTXONBdxvvuboKPuY6LRLn40ZhfuGzbMu2NjkMJ6PFwQYZklBAOQqZ7Sr_OhhqArIa0ot41oY-MaoP6oDhUTBfCuwsZnWINFVJrBtjMjT29VOTrx7FBPNpGRr1NFaJlWdltFQXImTSzIdbQoUsCij88eNgMggp0VAKEcsKRRFBenOR8ATRm-JPzMwfUYZPPg-Oz28uX16HD9QNnZIojbNK49IxT9TbTdto-kNKMCKcxivldyQTXE8iqIvwTKknl-zXr9dm_aih1dAe--Nfv2OZMZnd0n9ixBsgcoKcwV66cDzZZ_qtfJDh3UyLl2zMCoS49RIXXmJyzXmK0aWTMnsYxyijzqOeMwT4_4dUSqx_OknZZIKIZP1XAEYChIgIJp2SvHhCzMcynHbMeyZ6oOz6pUH-YRT19xafHqK-z26zR5_3o4a5rNFk1NDfJfpT--haf7tQ3xmKhzgYKtMuAzKfJCjd7-8hXW7HkkBW-oJgZCqp3aNPOE-ikamgDnJ38x0emN_w94AdPf6lIf-e8FMgDzOrfprIQwxHfWZ_D4WUBa58jnBpgJogtMvfJfLwXxFQ_5mi-D7h0im5ZShunPAwi4YxQjFV3zFWlXn844W2ucTY3zMI9fcQ5nrMFUs7M68Eee_oJE0SdZx23oXeV9j3cpIYFdJN5l6_VTz09-J860_tNvTdLDSx_QTM-_7-vgi3h6PFS3pzNUxb_b2M9Qja7ceUN7i3sUDTQvv__ef3_8IvJJprkUJFDfQ97tOjcpXCc_Qa_PHPf6sX_SjD33h0R-Cd63bIeSDUDKW4oPnR7rbKChWKRX0h5wHV53eKrMiyaiRDcteeMV9OHXhrWfHdYb6cTFiEMwxiASSV3KzHRL_vZRtmbYwy22MSsmCOg8tcIOLtlO1Cm8Qxmp-t7IIgkWgLFXOa7yHHbGrnung84IkDfx6Pe9SyljRpuxxhD3Fyys8t-DvlxMxFuTgVZAmt5FnqX9UCu3OwsMHlCV6O2gnxWYrz2dsKEMXx3UeOn3YXwGpGyWNs5WWkBPuHenrtPCaKBxVRuQ7WJq6AreNamLtgLeVXLXL07fiAvvshyNU4rnz6tLcJuDwyuvSN3-tuEBPnUpagPqgE64yyyRSrg8sDvxLwSs0qwqZa1IZWOVSNlrMpMx9ncnQcvHRFtAqj1XmjFNsI534BZ9mgBbmXJkKdGXMW4cxhVnEojoS-WaGNhbp4YFfUWeZMsVQntfZ5Xs-2qgFXLmxrUFGwrITNFkFjNgI6ltp4wIOYryS-e1vVQ1XI-uMP1L9VuHUxszr7a_XoLaOd17QdbCYJQ4TO6QznxpBHXMTEo7k6OIToCtvYxYZ1JxsOpiN9-IZ_ERbMWOQ3nDEJBH34P348TmSXIQAA';
	let prefersDark = $state(true);
	let isDark = $state(true);

	function switchTheme() {
		const value = isDark ? 'light' : 'dark';

		isDark = value === 'dark';
		localStorage.setItem('sv:theme', isDark === prefersDark ? 'system' : value);
	}

	$effect(() => {
		document.documentElement.classList.remove('light', 'dark');
		prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

		const theme = localStorage.getItem('sv:theme');

		isDark = !theme
			? prefersDark
			: theme === 'dark' || theme === 'system' && prefersDark;

		document.documentElement.classList.add(isDark ? 'dark' : 'light');
	});
</script>

<svelte:head>
	<title>--from-playground {title}</title>
	<script>{ const theme = localStorage.getItem('sv:theme'); document.documentElement.classList.add( !theme || theme === 'system' ? window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light' : theme ); }</script>
</svelte:head>

<div class="layout">
	<nav class="navbar">
		<div class="nav-left">
			<a href="/" class="svelte-icon"><img src={favicon} alt="Svelte" width="32" height="32" /></a>
			<p class="title">{title}</p>
		</div>

		<div class="nav-right">
			<a
				href={href}
				class="raised"
				target="_blank"
				rel="noopener noreferrer"
			>
				--to-playground 
				<span aria-hidden="true" style="margin-left:0.25em;">↗</span>
			</a>

			<button
				class="raised theme-toggle"
				onclick={switchTheme}
				aria-label="Toggle theme"
			><span class="icon"></span></button>
		</div>
	</nav>

	<main class="content">{@render children()}</main>
</div>

<style>
	:global(body) {
		margin: 0;
	}

	:global(html) {
		margin: 0;
		--bg-1: hsl(0, 0%, 100%);
		--bg-2: hsl(206, 20%, 90%);
		--bg-3: hsl(206, 20%, 80%);
		--navbar-bg: #fff;
		--fg-1: hsl(0, 0%, 13%);
		--fg-2: hsl(0, 0%, 50%);
		--fg-3: hsl(0, 0%, 60%);
		--link: hsl(208, 77%, 47%);
		--border-radius: 4px;
		--font: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans',
			'Helvetica Neue', sans-serif;
		color-scheme: light;
		background: var(--bg-1);
		color: var(--fg-1);
		font-family: var(--font);
		line-height: 1.5;
		height: calc(100vh - 2rem);
		accent-color: var(--link) !important;
		min-height: 100vh;
		background-color: var(--bg-1);
	}

	:global(html.dark) {
		color-scheme: dark;
		--bg-1: hsl(0, 0%, 18%);
		--bg-2: hsl(0, 0%, 30%);
		--bg-3: hsl(0, 0%, 40%);
		--navbar-bg: hsl(220, 14%, 16%);
		--fg-1: hsl(0, 0%, 75%);
		--fg-2: hsl(0, 0%, 40%);
		--fg-3: hsl(0, 0%, 30%);
		--link: hsl(206, 96%, 72%);
	}

	.navbar {
		color: var(--fg-1);
		display: flex;
		justify-content: space-between;
		align-items: center;
		padding: 0em 2.5rem;
		height: 3.7rem;
		background-color: var(--navbar-bg);
		box-shadow: 0 2px 8px 0 rgba(0, 0, 0, 0.08),
			0 1.5px 4px 0 rgba(0, 0, 0, 0.04);
	}

	.nav-left {
		display: flex;
		align-items: center;
		gap: 0.5rem;
	}

	.svelte-icon {
		display: flex;
		align-items: center;
		text-decoration: none;
		transition: opacity 0.2s ease;
	}

	.svelte-icon:hover {
		opacity: 0.8;
	}

	.title {
		font-size: 1.5rem;
		font-weight: 400;
		margin: 0;
	}

	.nav-right {
		display: flex;
		align-items: center;
		gap: 1rem;
	}

	.raised {
		background: var(--navbar-bg);
		border-left: 0.5px solid var(--fg-3);
		border-top: 0.5px solid var(--fg-3);
		border-bottom: none;
		border-right: none;
		border-radius: var(--border-radius);
		color: var(--fg-1);
		cursor: pointer;
		transition: all 0.2s ease;
		box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1),
			0 1px 2px rgba(0, 0, 0, 0.06);
		text-decoration: none;
		font-weight: 500;
		padding: 0.25rem 0.75rem;
		font-size: 0.8rem;
	}

	.raised:hover {
		border-left-color: var(--fg-2);
		border-top-color: var(--fg-2);
		box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15),
			0 2px 4px rgba(0, 0, 0, 0.1);
		transform: translate(-1px, -1px);
	}

	.content {
		padding: 1rem;
		color: var(--fg-1);
	}

	.theme-toggle {
		display: flex;
		align-items: center;
		justify-content: center;
		width: 1.8rem;
		height: 1.8rem;
		padding: 0;
		min-width: 2rem;
	}

	.icon {
		display: inline-block;
		width: 1.5rem;
		height: 1.5rem;
		-webkit-mask-size: 1.5rem;
		mask-size: 1.5rem;
		-webkit-mask-repeat: no-repeat;
		mask-repeat: no-repeat;
		-webkit-mask-position: center;
		mask-position: center;
		background-color: var(--fg-1);
	}

	.icon {
		mask-image: url('data:image/svg+xml,%3csvg%20xmlns="http://www.w3.org/2000/svg"%20viewBox="0%200%2024%2024"%3e%3cpath%20fill="%23666"%20d="M12%2021q-3.775%200-6.388-2.613T3%2012q0-3.45%202.25-5.988T11%203.05q.625-.075.975.45t-.025%201.1q-.425.65-.638%201.375T11.1%207.5q0%202.25%201.575%203.825T16.5%2012.9q.775%200%201.538-.225t1.362-.625q.525-.35%201.075-.037t.475.987q-.35%203.45-2.937%205.725T12%2021Zm0-2q2.2%200%203.95-1.213t2.55-3.162q-.5.125-1%20.2t-1%20.075q-3.075%200-5.238-2.163T9.1%207.5q0-.5.075-1t.2-1q-1.95.8-3.163%202.55T5%2012q0%202.9%202.05%204.95T12%2019Zm-.25-6.75Z"/%3e%3c/svg%3e');
	}

	:global(html.dark) .icon {
		mask-image: url("data:image/svg+xml,%3csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2024%2024'%3e%3cpath%20fill='%23d4d4d4'%20d='M12%2019a1%201%200%200%201%20.993.883L13%2020v1a1%201%200%200%201-1.993.117L11%2021v-1a1%201%200%200%201%201-1zm6.313-2.09.094.083.7.7a1%201%200%200%201-1.32%201.497l-.094-.083-.7-.7a1%201%200%200%201%201.218-1.567l.102.07zm-11.306.083a1%201%200%200%201%20.083%201.32l-.083.094-.7.7a1%201%200%200%201-1.497-1.32l.083-.094.7-.7a1%201%200%200%201%201.414%200zM4%2011a1%201%200%200%201%20.117%201.993L4%2013H3a1%201%200%200%201-.117-1.993L3%2011h1zm17%200a1%201%200%200%201%20.117%201.993L21%2013h-1a1%201%200%200%201-.117-1.993L20%2011h1zM6.213%204.81l.094.083.7.7a1%201%200%200%201-1.32%201.497l-.094-.083-.7-.7A1%201%200%200%201%206.11%204.74l.102.07zm12.894.083a1%201%200%200%201%20.083%201.32l-.083.094-.7.7a1%201%200%200%201-1.497-1.32l.083-.094.7-.7a1%201%200%200%201%201.414%200zM12%202a1%201%200%200%201%20.993.883L13%203v1a1%201%200%200%201-1.993.117L11%204V3a1%201%200%200%201%201-1zm0%205a5%205%200%201%201-4.995%205.217L7%2012l.005-.217A5%205%200%200%201%2012%207z'/%3e%3c/svg%3e");
	}
</style>