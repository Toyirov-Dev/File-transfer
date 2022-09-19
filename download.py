import socket

s = socket.socket()
host = str(input("Please enter the host address of the sender: "))
port = 4628
s.connect((host, port))
print("\nConnected...\n")

filename = str(input("Please enter a filename for the incoming file: "))
file = open(filename, 'wb')
file_date = s.recv(1024) 
file.write(file_date)
file.close()

print("\nFile has been received!")