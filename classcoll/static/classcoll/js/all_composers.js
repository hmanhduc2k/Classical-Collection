document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#showComposers').addEventListener('click', () => {
        document.querySelector('#composerForm').style.display = 'none'
        document.querySelector('#allComposers').style.display = 'block'
    })

    document.querySelector('#showForm').addEventListener('click', () => {
        document.querySelector('#composerForm').style.display = 'block'
        document.querySelector('#allComposers').style.display = 'none'
    })
})