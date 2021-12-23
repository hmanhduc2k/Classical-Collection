document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('#favoritePiece').forEach(item => 
        item.addEventListener('click', () => {
        console.log(item.dataset.value)
        fetch(`/favpiece/${item.dataset.value}`, {
            method: 'PUT',
            body: JSON.stringify()
        })
        .then(response => response.json())
        .then(result => {
            item.innerHTML = result.message
        })
    }))
})