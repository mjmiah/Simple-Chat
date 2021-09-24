from website import create_app
from flask_socketio import SocketIO, send


app = create_app()
socketio = SocketIO(app)


@socketio.on('message')
def handleMessage(msg):
	print('Received message: ' + msg)
	send(msg, broadcast=True)


if __name__ == '__main__': #start server
    app.run(debug = True)
