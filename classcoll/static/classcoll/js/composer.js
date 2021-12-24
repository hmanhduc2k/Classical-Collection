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
            item.innerHTML = result.message
        })
    }))

    document.querySelectorAll('#showPieces').forEach(item => {
        item.addEventListener('click', () => {
            item.parentElement.querySelector('#allPieces').style.display = 'block'
            item.parentElement.querySelector('#biography').style.display = 'none'
        })
    })

    document.querySelectorAll('#showBiography').forEach(item => {
        item.addEventListener('click', () => {
            item.parentElement.querySelector('#allPieces').style.display = 'none'
            item.parentElement.querySelector('#biography').style.display = 'block'
        })
    })
})