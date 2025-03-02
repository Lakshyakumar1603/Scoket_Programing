#RCE=Remote code Execution
#IP address=192.168.10.200
#Protocol= tcp(transmission control protocol)/UDP(User Datagram Protocol)
import socket
#number of functions in socket module
#print(dir(socket))
#s=socket.socket() tcp protocol will be used by default
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#                IPaddress    ,  protocol
#finally is having capabitlty to create UDP socket
#target system address
target_ip='127.0.0.1'
target_port=9999
final_target=(target_ip,target_port)
#port=0-65535
#taking input from user
while 4>3:
    msg=input("Please enter your message:")
# since python3 is supporting minimum encoding
    new_msg=msg.encode('ascii')
#final lets send data
    s.sendto(new_msg,final_target)
    print('The Data is successfully sended')
    
