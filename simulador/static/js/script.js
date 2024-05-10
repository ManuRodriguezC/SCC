const btlibreinversion = document.getElementById('bt-libreinversion')
const btlibranza = document.getElementById('bt-libranza')
const btcartera = document.getElementById('bt-cartera')

const divcartera = document.getElementById('cartera')
const divlibranza = document.getElementById('libranza')
const divlibreinversiob = document.getElementById('libreinversion')

btlibreinversion.addEventListener('click', () => {
    divcartera.style.display = 'none'
    divlibranza.style.display = 'none'
    divlibreinversiob.style.display = 'block'
})

btlibranza.addEventListener('click', () => {
    divcartera.style.display = 'none'
    divlibranza.style.display = 'block'
    divlibreinversiob.style.display = 'none'

})

btcartera.addEventListener('click', () => {
    divcartera.style.display = 'block'
    divlibranza.style.display = 'none'
    divlibreinversiob.style.display = 'none'
})