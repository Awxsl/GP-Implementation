const cards = document.getElementById('cards')

cards.addEventListener('mouseup', e => {
    if (e.target.children[0].classList.contains('absent')) {
        e.target.children[0].classList.remove('absent')
        e.target.children[0].classList.add('attended')
        e.target.children[0].classList.remove('fa-regular')
        e.target.children[0].classList.add('fa-solid')
        e.target.children[0].classList.remove('fa-x')
        e.target.children[0].classList.add('fa-check')

    } else if(e.target.children[0].classList.contains('attended')) {
        e.target.children[0].classList.remove('attended')
        e.target.children[0].classList.add('absent')
        e.target.children[0].classList.remove('fa-solid')
        e.target.children[0].classList.add('fa-regular')
        e.target.children[0].classList.remove('fa-check')
        e.target.children[0].classList.add('fa-x')
    }
})
