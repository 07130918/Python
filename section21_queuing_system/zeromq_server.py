import time
import zmq

context = zmq.Context()
# socket = context.socket(zmq.PUSH)
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:5690")

id = 0
while True:
    id += 1

    #  Send reply back to client
    socket.send(('sub1:' + str(id)).encode())

    print(f"Sent: {id}")

    #  Do some 'work'
    time.sleep(1)
