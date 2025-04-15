from flask import Flask, render_template, config, request 
from flask import _request_ctx_stack,has_request_context,json as flask_json
from flask_socketio  import SocketIO, send, emit

app=Flask(__name__)
app.config['SECRET_KEY']='secretkey'
app.config['DEBUG']=True
socketio=SocketIO(app)

users={}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/orginate')
def orginate():
     socketio.emit('from server','server is commanding you')
     return '<h1>sent!</h1>'

@socketio.on('message from the user', namespace='/message')
def recive_message(message):
      print('USER FROM THE MESSAGE :{}'.format(message))
      emit('from flask', message )

@socketio.on('username', namespace='/private')
def recive_message(username):
     users[username]= request.sid
     #users.append({username: request.sid})
     #print(users)
@socketio.on('private_message', namespace='/private')
def private_message(payload):
     recipient_session_id = users[payload['username']]
     message = payload['message']

     emit('new_private_message', message, room = recipient_session_id)


'''
@socketio.on('message')
def recive_message(message):
    print('#########{}'.format(message))
    send('this is from the flaskpip')

@socketio.on('custom evnet')
def recived_custom_event(message):
    print('This is custom event: {}'.format(message))
'''

if __name__ =='__main__':
    socketio.run(app)

