import socket
from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from app.codec_loader import ensure_generated_codec

ensure_generated_codec()

from generated_codec import DeviceStatus
import time


def run_client():
    server_address = ('localhost', 65432)

    status = DeviceStatus(
        device_id=42,
        temperature=23.5,
        is_active=True,
        history={"last_seen": "2026-07-05", "errors": 0},
        status_message="all good",
        tags=["production", "stable"],
    )

    binary_data = status.serialize()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(server_address)
        print(f"Wysyłanie danych binarnych: {binary_data}")
        s.sendall(binary_data)

if __name__ == "__main__":
    run_client()