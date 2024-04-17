<template>
	<div class="min-h-screen flex items-center justify-center bg-gray-100">
		<div class="bg-white p-8 rounded shadow-md max-w-sm w-full">
			<img src="../assets/logo.png" alt="Logo" class="mx-auto mb-4" style="max-width: 150px;">
			<h1 class="text-3xl font-bold mb-4 text-center text-gray-800">Please Login</h1>
			<form @submit.prevent="login">
				<div class="mb-4">
					<label for="username" class="block text-sm font-medium text-gray-700">Username</label>
					<input type="text" id="username" v-model="username" placeholder="Username"
						class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm" />
				</div>
				<div class="mb-4">
					<label for="password" class="block text-sm font-medium text-gray-700">Password</label>
					<input type="password" id="password" v-model="password" placeholder="Password"
						class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm" />
				</div>
				<button type="submit" :disabled="loading"
					:class="['w-full py-2 px-4 rounded-md text-white font-semibold focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50', loading ? 'bg-blue-200 text-blue-500 cursor-not-allowed' : 'bg-blue-500 hover:bg-blue-600']">
					<i v-if="loading" class="fa fa-spin fa-spinner mr-2"></i>
					{{ loading ? 'Signing in...' : 'Login' }}
				</button>
			</form>
			<div class="mt-4 text-sm text-center">
				<p>Forgot your Password? <router-link to="#" class="text-blue-500">Reset it</router-link></p>
				<p>Not registered yet? <router-link to="#" class="text-blue-500">Register</router-link></p>
			</div>
		</div>
	</div>
</template>

<script>
import { useNotification } from "@kyvg/vue3-notification";

export default {
	data() {
		return {
			username: "",
			password: "",
			loading: false
		};
	},
	methods: {
		async login() {
			try {
				const { notify } = useNotification();

				this.loading = true;
				if (this.username === "admin" && this.password === "admin") {
					notify({
						title: "Login",
						text: "Successful Login",
						duration: 5000
					});
					localStorage.setItem('userName', this.username)
					this.$router.push("/dashboard");
				} else {
					throw new Error("Invalid credentials");
				}
			} catch (error) {
				const { notify } = useNotification();
				notify({
					title: "Login Error",
					text: error.message,
					type: "error",
					duration: 2000
				});
			} finally {
				this.loading = false;
			}
		}
	}
};
</script>
