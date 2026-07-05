import socket
from generated_codec import DeviceStatus
import time

def run_client():
    server_address = ('localhost', 65432)
    
    # Tworzymy instancję danych i serializujemy ją
    status = DeviceStatus(device_id=42, temperature=23.5, is_active=True)
    binary_data = status.serialize()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(server_address)
        print(f"Wysyłanie danych binarnych: {binary_data}")
        s.sendall(binary_data)

if __name__ == "__main__":
    run_client()