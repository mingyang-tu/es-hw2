import socket
import json
import numpy as np
import matplotlib.pyplot as plt

HOST = "192.168.50.153"  # IP address
PORT = 6538  # Port to listen on (use ports > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    mapping_of_title = dict()
    mapping_of_title[(0,0)] = 'Pressure(mbar)'
    mapping_of_title[(0,1)] = 'Humidity(%)'
    mapping_of_title[(0,2)] = 'Temperature(celsius)'
    mapping_of_title[(1,0)] = 'Acceleration of x'
    mapping_of_title[(1,1)] = 'Acceleration of y'
    mapping_of_title[(1,2)] = 'Acceleration of z'
    mapping_of_title[(2,0)] = 'Gyro-x'
    mapping_of_title[(2,1)] = 'Gyro-y'
    mapping_of_title[(2,2)] = 'Gyro-z'
    mapping_of_title[(3,0)] = 'Magneto-x'
    mapping_of_title[(3,1)] = 'Magneto-y'
    mapping_of_title[(3,2)] = 'Magneto-z'
    
    s.bind((HOST, PORT))
    s.listen()
    print("Starting server at: ", (HOST, PORT))
    conn, addr = s.accept()
    fig, axs = plt.subplots(4, 3)
    plt.tight_layout()
    
    for index in range(0,4):
            for j in range(0,3):
                axs[index,j].set_title(mapping_of_title[(index,j)])
    
    with conn:
        print("Connected at", addr)
        while True:
            data = conn.recv(1024)
            print("Received from socket server:", data,'/n')
                
            obj = json.loads(data)
            t = obj['s']
            
            axs[0,0].scatter(t, obj['pre'], color='tab:blue', s=25)
            axs[0,1].scatter(t, obj['hum'], color='tab:orange', s=25)
            axs[0,2].scatter(t, obj['temp'], color='tab:green', s=25)
            axs[1,0].scatter(t, obj['x_a'], color='tab:blue', s=25)
            axs[1,1].scatter(t, obj['y_a'], color='tab:orange', s=25)
            axs[1,2].scatter(t, obj['z_a'], color='tab:green', s=25)
            axs[2,0].scatter(t, obj['x_g'], color='tab:blue', s=25)
            axs[2,1].scatter(t, obj['y_g'], color='tab:orange', s=25)
            axs[2,2].scatter(t, obj['z_g'], color='tab:green', s=25)
            axs[3,0].scatter(t, obj['x_m'], color='tab:blue', s=25)
            axs[3,1].scatter(t, obj['y_m'], color='tab:orange', s=25)
            axs[3,2].scatter(t, obj['z_m'], color='tab:green', s=25)
            
            
            plt.pause(0.001)
