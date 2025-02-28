import paramiko
import socketserver
import threading
from paramiko import ServerInterface, AUTH_SUCCESSFUL, AUTH_FAILED

USERNAME = "admin"
PASSWORD = "admin123"

class MySFTPServer(ServerInterface):
    def check_auth_password(self, username, password):
        if username == USERNAME and password == PASSWORD:
            return AUTH_SUCCESSFUL
        return AUTH_FAILED

def sftp_server():
    host_key = paramiko.RSAKey.generate(2048)
    transport = paramiko.Transport(("0.0.0.0", 10000))
    transport.add_server_key(host_key)

    server = MySFTPServer()
    transport.start_server(server=server)

    while True:
        channel = transport.accept(20)
        if channel is None:
            break
