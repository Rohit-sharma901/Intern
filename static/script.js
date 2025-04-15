$(document).ready(function(){

var socket= io.connect('http://127.0.0.1:5000');

var socket_message = io('http://127.0.0.1:5000/message');
$('#send').on('click',function(){
    var message = $('#message').val();
    socket_message.emit('message from the user', message);
});

socket_message.on('from flask',function(msg){
    alert(msg);
})

socket.on('from server',function(msg){
    alert(msg);
})

var private_socket= io('http://127.0.0.1:5000/private');

$('#send_username').on('click', function() {
    private_socket.emit('username', $('#username').val())
});

$('#send_private_message').on('click',function(){
    var recipient = $('#send_to_username').val();
    var message_to_sender = $('#private_message').val();

    private_socket.emit('private_message',{'username': recipient, 'message': message_to_sender});
    });

    private_socket.on('new_private_message', function(msg){
        alert(msg);     

});
/*
socket.on('connect', function(){
    socket.send('i am conneted!!');

    socket.emit('custom event','the message is custom event !!')

    socket.on('message', function(msg){
        alert(msg)
    }); 
    */

});