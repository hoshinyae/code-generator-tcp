import socket
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
            # Nasza struktura (int+float+bool) zajmuje dokładnie 9 bajtów (4+4+1)
            data = conn.recv(9) 
            if data:
                # Deserializacja surowych bajtów z powrotem do obiektu klasy
                received_status = DeviceStatus.deserialize(data)
                print("Odebrano i zdeserializowano dane:")
                print(f"ID Urządzenia: {received_status.device_id}")
                print(f"Temperatura: {received_status.temperature}°C")
                print(f"Aktywny: {received_status.is_active}")

if __name__ == "__main__":
    run_server()