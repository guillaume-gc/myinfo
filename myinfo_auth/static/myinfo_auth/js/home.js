import {domReady} from "./global.js";

domReady.then(() => {
	let vue = new Vue({
		el: '#app',
		delimiters: ['[[', ']]'],
		data() {
			return {
				user: {},
				newEmail: ""
			}
		},
		mounted() {
			axios
				.get('/api/me/')
				.then(response => (this.user = response.data))
				.catch(error => console.warn(error))
		},
		methods: {
			change_info_click: function () {
				axios.put('/api/me/', {
					"email": this.newEmail
				}).then((result) => {
					console.log(result)
					this.user = result["data"]
				});
			}
		}
	});
})