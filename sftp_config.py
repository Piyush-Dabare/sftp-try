import paramiko
import os

HOST = "0.0.0.0"
PORT = 22
USERNAME = "admin"
PASSWORD = "admin123"

def sftp_server():
    transport = paramiko.Transport((HOST, PORT))
    transport.add_server_key(paramiko.RSAKey.generate(2048))
    transport.start_server()
    print(f"SFTP Server running at {HOST}:{PORT}")
