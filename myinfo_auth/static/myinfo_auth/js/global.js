export const domReady = new Promise(resolve => {
	if (document.readyState === "loading") {
		document.addEventListener('DOMContentLoaded', resolve);
	} else {
		resolve();
	}
});

export const windowReady = new Promise(resolve => {
	if (document.readyState === 'complete') {
		resolve();
	} else {
		window.addEventListener('load', resolve);
	}
});

export function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

axios.defaults.headers.common['X-CSRFToken'] = getCookie('csrftoken')