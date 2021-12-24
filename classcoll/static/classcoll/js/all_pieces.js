document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#showPieces').addEventListener('click', () => {
        document.querySelector('#forms').style.display = 'none'
        document.querySelector('#pieces').style.display = 'block'
    })

    document.querySelector('#showForm').addEventListener('click', () => {
        document.querySelector('#forms').style.display = 'block'
        document.querySelector('#pieces').style.display = 'none'
    })
})