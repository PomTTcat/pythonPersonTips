# -*- coding: utf-8 -*-

print '-------socket-------'

# 导入socket库:
import socket
# 创建一个socket:	更先进的IPv6，就指定为AF_INET6
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('www.sina.com.cn', 80))
# 端口号小于1024的是Internet标准服务的端口，端口号大于1024的，可以任意使用。


s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = ''.join(buffer)

s.close()

header, html = data.split('\r\n\r\n', 1)

print header
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)

