import socket
from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from app.codec_loader import ensure_generated_codec

ensure_generated_codec()

from generated_codec import DeviceStatus


def run_server():
    server_address = ('localhost', 65432)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(server_address)
        s.listen()
        print("Serwer TCP uruchomiony, oczekiwanie na połączenie...")
        
        conn, addr = s.accept()
        with conn:
            print(f"Połączono z {addr}")
            data = conn.recv(4096)
            if data:
                received_status = DeviceStatus.deserialize(data)
                print(received_status)

if __name__ == "__main__":
    run_server()