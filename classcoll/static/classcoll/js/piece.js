document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('#showInfo').forEach(item => {
        item.addEventListener('click', () => {
            item.parentElement.querySelector('#pieceInfo').style.display = 'block'
            item.parentElement.querySelector('#commentSection').style.display = 'none'
        })
    })

    document.querySelectorAll('#showComment').forEach(item => {
        item.addEventListener('click', () => {
            item.parentElement.querySelector('#pieceInfo').style.display = 'none'
            item.parentElement.querySelector('#commentSection').style.display = 'block'
        })
    })

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

    document.querySelectorAll('#commentForm').forEach(item => 
        item.addEventListener('submit', () => {
            pieceId = item.dataset.value
            content = item.querySelector('#comment').value
            fetch(`/comment/${pieceId}`, {
                method: 'POST',
                body: JSON.stringify({
                    parent: -1,
                    content: content
                })
            })
            .then(response => response.json())
            .then(result => console.log(result))
        })
    )

    document.querySelectorAll('#edit').forEach(item => {
        item.addEventListener('click', () => {
            item.parentElement.querySelector('#commentEdit').style.display = 'block'
        })
    })

    document.querySelectorAll('#cancel').forEach(item => {
        item.addEventListener('click', () => {
            item.parentElement.querySelector('#commentEdit').style.display = 'none'
        })
    })

    document.querySelectorAll('#commentEdit').forEach(item => {
        item.addEventListener('submit', () => {
            newContent = item.querySelector('#newComment').value
            id = item.dataset.value
            fetch(`/comment/${id}`, {
                method: 'PUT',
                body: JSON.stringify({
                    content: newContent
                })
            })
            .then(response => response.json())
            .then(result => {
                item.style.display = 'none'
                item.parentElement.querySelector('#contentHolder').innerHTML = newContent
            })
        })
    })

    document.querySelectorAll('#delete').forEach(item => {
        item.addEventListener('click', () => {
            fetch(`/comment/${item.dataset.value}`, {
                method: 'DELETE',
                body: JSON.stringify()
            })
            .then(response => response.json())
            .then(result => {
                item.parentElement.style.display = 'none'
            })
        })
    })

    document.querySelectorAll('#upvote').forEach(item => {
        item.addEventListener('click', () => {
            count = item.parentElement.querySelector('#upvoteCount').innerHTML
            fetch(`/upvote/${item.dataset.value}`, {
                method: 'PUT',
                body: JSON.stringify()
            })
            .then(response => response.json())
            .then(result => {
                console.log(result)
                if (result.status) {
                    item.parentElement.querySelector('#upvoteCount').innerHTML = (parseInt(count) + 1).toString()
                    item.innerHTML = `<i class="bi bi-hand-thumbs-up-fill"></i>`
                } else {
                    item.parentElement.querySelector('#upvoteCount').innerHTML = (parseInt(count) - 1).toString()
                    item.innerHTML = `<i class="bi bi-hand-thumbs-up"></i>`
                }
            })
        })
    })
})