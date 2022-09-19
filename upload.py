import socket

s = socket.socket()
host = socket.gethostname()
port = 4628
s.bind((host,port))
s.listen(1)
print("You host address: ", host)
print("waiting for any incoming connections...\n")
conn, addr = s.accept()
print(addr, " Has connected to the server. \n")

filename = str(input("Please enter the filename of the file: "))
file = open(filename, 'rb')
file_date = file.read(1024)

conn.send(file_date)
print("\nfile shared!")
