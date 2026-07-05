import struct

class DeviceStatus:
    def __init__(self, device_id, temperature, is_active):
        
        self.device_id = device_id
        
        self.temperature = temperature
        
        self.is_active = is_active
        

    def serialize(self) -> bytes:
        # Mapowanie typów na formaty biblioteki struct
        # i = int (4 bajty), f = float (4 bajty), ? = bool (1 bajt)
        format_str = "!" + "".join([
            "i" if f["type"] == "int" else "f" if f["type"] == "float" else "?" 
            for f in [{'name': 'device_id', 'type': 'int'}, {'name': 'temperature', 'type': 'float'}, {'name': 'is_active', 'type': 'bool'}]
        ])
        return struct.pack(
            format_str,
            
            self.device_id,
            
            self.temperature,
            
            self.is_active
            
        )

    @classmethod
    def deserialize(cls, data: bytes):
        format_str = "!" + "".join([
            "i" if f["type"] == "int" else "f" if f["type"] == "float" else "?" 
            for f in [{'name': 'device_id', 'type': 'int'}, {'name': 'temperature', 'type': 'float'}, {'name': 'is_active', 'type': 'bool'}]
        ])
        unpacked = struct.unpack(format_str, data)
        return cls(
            
            unpacked[0],
            
            unpacked[1],
            
            unpacked[2]
            
        )