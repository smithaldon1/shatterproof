const input = document.getElementById('newsletter-email');
const showText = document.getElementById('terms');

input.addEventListener('input', function() {
    if (input.value.trim() !== '') {
        showText.classList.remove('d-none');
    } else {
        showText.classList.add('d-none');
    }
});