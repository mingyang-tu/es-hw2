import socket
import json
import matplotlib.pyplot as plt

HOST = "HOSTNAME"  # IP address
PORT = 6531  # Port to listen on (use ports > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Starting server at: ", (HOST, PORT))
    conn, addr = s.accept()
    with conn:
        print("Connected at", addr)
        while True:
            data = conn.recv(1024).decode('utf-8')
            print("Received from socket server:", data)
            if (data.count('{') != 1):
                # Incomplete data are received.
                choose = 0
                buffer_data = data.split('}')
                while buffer_data[choose][0] != '{':
                    choose += 1
                data = buffer_data[choose] + '}'
            obj = json.loads(data)
            t = obj['s']
            plt.scatter(t, obj['x'], color='tab:blue', s=25)
            plt.scatter(t, obj['y'], color='tab:orange', s=25)
            plt.scatter(t, obj['z'], color='tab:green', s=25)
            plt.xlabel("sample num")
            plt.legend(['x', 'y', 'z'], loc=1)
            plt.pause(0.001)
