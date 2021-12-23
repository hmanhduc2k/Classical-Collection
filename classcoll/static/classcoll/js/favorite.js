document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#btnPiece').addEventListener('click', () => {
        document.querySelector('#piece').style.display = 'block';
        document.querySelector('#composer').style.display = 'none'
    })

    document.querySelector('#btnComposer').addEventListener('click', () => {
        document.querySelector('#piece').style.display = 'none';
        document.querySelector('#composer').style.display = 'block'
    })
})