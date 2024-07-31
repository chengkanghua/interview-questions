import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname()
port =9999
# 连接服务,指定主机和端口
client_socket.connect((host,port))
#接收小于1024字节的数据
msg = client_socket.recv(1024)
client_socket.close()
print(msg.decode('utf-8'))



# server
'''
import socket
#创建socket 对象
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#获取主机名和设置端口号
host = socket.gethostname()
port = 9999
# 设置套接字选项，允许端口复用
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 绑定端口
server_socket.bind((host,port))
# 设置最大连接数,超过后排队
server_socket.listen(5)

while True:
    #建立客户端连接
    client_socket, addr = server_socket.accept()
    print("连接地址%s"% str(addr))

    msg = "欢迎访问服务器!\r\n"

    client_socket.send(msg.encode('utf-8'))
    client_socket.close()
'''
