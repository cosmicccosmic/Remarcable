document.addEventListener('DOMContentLoaded', function() {
    submitOnEnterKey();

});

function submitOnEnterKey() {
    const searchForm = document.querySelector('form[action*="search_products"]');
    const inputFields = searchForm.querySelectorAll('input[type="text"], select');

    inputFields.forEach(input => {
        input.addEventListener('keypress', function(event) {
            if (event.key === 'Enter') {
                event.preventDefault();
                searchForm.submit();
            }
        });
    });
}