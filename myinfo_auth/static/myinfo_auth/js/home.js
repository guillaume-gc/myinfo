import {domReady} from "./global.js";

domReady.then(() => {
	let vue = new Vue({
		el: '#app',
		delimiters: ['[[', ']]'],
		data() {
			return {
				user: {},
				newEmail: '',
				email: '',
				emailState: ''
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
				return axios.put('/api/me/', {
					"email": this.newEmail
				})
					.then((result) => {
						this.user = result["data"]
					})
					.catch(error => console.warn(error));
			},
			checkFormValidity() {
				const valid = this.$refs.form.checkValidity()
				this.emailState = valid
				return valid
			},
			resetModal() {
				this.email = ''
				this.emailState = null
			},
			handleOk(bvModalEvt) {
				// Prevent modal from closing
				bvModalEvt.preventDefault()
				// Trigger submit handler
				this.handleSubmit()
			},
			handleSubmit() {
				// Exit when the form isn't valid
				if (!this.checkFormValidity()) {
					return
				}
				axios.put('/api/me/', {
					"email": this.email
				})
					.then((result) => {
						this.user = result["data"]
						this.$nextTick(() => {
							this.$bvModal.hide('modal-info')
						})
					})
					.catch(error => console.warn(error));
			}
		}
	});
})