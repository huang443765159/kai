const socket = new WebSocket('ws://localhost:19955');

socket.addEventListener('open', function (event) {
    console.log('opening...')
    // socket.send('WebSocket Online')
})
const contactServer = () => {
    console.log('init ing ...')
    socket.send('Initialize');
}

socket.addEventListener('message', function (event) {
    console.log('data recv...', event.data)
    go(event.data)
});
