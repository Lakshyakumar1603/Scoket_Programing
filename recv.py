import socket
import time
from read_file import ready

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
my_ip='0.0.0.0'
#--52.2.116.225--jecrc.delvex.io
my_port=9999
my_address=(my_ip,my_port)
#lets create a connection string
s.bind(my_address)
while 4>2:
    #data is coming 
    data=s.recvfrom(100)
    #print(data)
    new_data=data[0]
    final_msg=new_data.decode('ascii')
    print(final_msg)
    with open("try/combined.txt","w+") as f :
        f.write(final_msg+"\n")

    time.sleep(2)
    ready()
