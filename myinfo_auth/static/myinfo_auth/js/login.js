import {domReady} from "./global.js";

domReady.then(() => {
	let vue = new Vue({
		el: '#app',
		delimiters: ['[[', ']]']
	});
})