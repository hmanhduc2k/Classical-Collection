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
                    item.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-star-fill" viewBox="0 0 16 16">
                                        <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z"/>
                                    </svg>`
                } else {
                    item.parentElement.querySelector('#upvoteCount').innerHTML = (parseInt(count) - 1).toString()
                    item.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-star" viewBox="0 0 16 16">
                                        <path d="M2.866 14.85c-.078.444.36.791.746.593l4.39-2.256 4.389 2.256c.386.198.824-.149.746-.592l-.83-4.73 3.522-3.356c.33-.314.16-.888-.282-.95l-4.898-.696L8.465.792a.513.513 0 0 0-.927 0L5.354 5.12l-4.898.696c-.441.062-.612.636-.283.95l3.523 3.356-.83 4.73zm4.905-2.767-3.686 1.894.694-3.957a.565.565 0 0 0-.163-.505L1.71 6.745l4.052-.576a.525.525 0 0 0 .393-.288L8 2.223l1.847 3.658a.525.525 0 0 0 .393.288l4.052.575-2.906 2.77a.565.565 0 0 0-.163.506l.694 3.957-3.686-1.894a.503.503 0 0 0-.461 0z"/>
                                    </svg>`
                }
            })
        })
    })
})