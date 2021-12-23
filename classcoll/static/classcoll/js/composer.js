document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('#favoriteComposer').forEach(item => 
        item.addEventListener('click', () => {
        console.log(item.dataset.value)
        fetch(`/favcomposer/${item.dataset.value}`, {
            method: 'PUT',
            body: JSON.stringify()
        })
        .then(response => response.json())
        .then(result => {
            this.innerHTML = result.message
        })
    }))
})