import socket

UDP_IP = "0.0.0.0"
UDP_PORT = 53

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(UDP_IP, UDP_PORT)

while True:
    data, addr = sock.recvfrom(1024)
    print(data)
    print(addr)
    # all_subs = []
    # with open('subdomains.txt','r+') as subs_file:
    #     all_subs = subs_file.readlines()
    # for line in all_subs:
    #     if line in str(data):
    #         with open('dnsleaks.txt','a+') as res_file:
    #             res_file.write("{}\n".format(addr[0]))
