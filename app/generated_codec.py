import json
import struct


def _default_for_type(field_type: str):
    if field_type in {"int", "integer"}:
        return 0
    if field_type in {"float", "double"}:
        return 0.0
    if field_type in {"bool", "boolean"}:
        return False
    if field_type in {"str", "string"}:
        return ""
    return {}


class DeviceStatus:
    def __init__(self, **values):
        
        setattr(self, "device_id", values.pop("device_id", _default_for_type("int")))
        
        setattr(self, "temperature", values.pop("temperature", _default_for_type("float")))
        
        setattr(self, "is_active", values.pop("is_active", _default_for_type("bool")))
        
        setattr(self, "history", values.pop("history", _default_for_type("dict")))
        
        setattr(self, "status_message", values.pop("status_message", _default_for_type("str")))
        
        setattr(self, "tags", values.pop("tags", _default_for_type("list")))
        
        setattr(self, "battery_level", values.pop("battery_level", _default_for_type("int")))
        
        setattr(self, "is_encrypted", values.pop("is_encrypted", _default_for_type("bool")))
        
        setattr(self, "last_updated", values.pop("last_updated", _default_for_type("str")))
        
        setattr(self, "location", values.pop("location", _default_for_type("dict")))
        
        setattr(self, "firmware_version", values.pop("firmware_version", _default_for_type("str")))
        
        setattr(self, "signal_strength", values.pop("signal_strength", _default_for_type("float")))
        
        setattr(self, "error_codes", values.pop("error_codes", _default_for_type("list")))
        
        setattr(self, "uptime", values.pop("uptime", _default_for_type("int")))
        
        setattr(self, "maintenance_required", values.pop("maintenance_required", _default_for_type("bool")))
        
        if values:
            unexpected = ", ".join(values.keys())
            raise TypeError(f"Unexpected field(s): {unexpected}")

    def serialize(self) -> bytes:
        packed_parts = []
        
        value = getattr(self, "device_id")
        
        packed_parts.append(struct.pack("!i", value))
        
        
        value = getattr(self, "temperature")
        
        packed_parts.append(struct.pack("!f", value))
        
        
        value = getattr(self, "is_active")
        
        packed_parts.append(struct.pack("?", value))
        
        
        value = getattr(self, "history")
        
        payload = json.dumps(value).encode("utf-8")
        packed_parts.append(struct.pack("!I", len(payload)))
        packed_parts.append(payload)
        
        
        value = getattr(self, "status_message")
        
        payload = value.encode("utf-8")
        packed_parts.append(struct.pack("!I", len(payload)))
        packed_parts.append(payload)
        
        
        value = getattr(self, "tags")
        
        payload = json.dumps(value).encode("utf-8")
        packed_parts.append(struct.pack("!I", len(payload)))
        packed_parts.append(payload)
        
        
        value = getattr(self, "battery_level")
        
        packed_parts.append(struct.pack("!i", value))
        
        
        value = getattr(self, "is_encrypted")
        
        packed_parts.append(struct.pack("?", value))
        
        
        value = getattr(self, "last_updated")
        
        payload = value.encode("utf-8")
        packed_parts.append(struct.pack("!I", len(payload)))
        packed_parts.append(payload)
        
        
        value = getattr(self, "location")
        
        payload = json.dumps(value).encode("utf-8")
        packed_parts.append(struct.pack("!I", len(payload)))
        packed_parts.append(payload)
        
        
        value = getattr(self, "firmware_version")
        
        payload = value.encode("utf-8")
        packed_parts.append(struct.pack("!I", len(payload)))
        packed_parts.append(payload)
        
        
        value = getattr(self, "signal_strength")
        
        packed_parts.append(struct.pack("!f", value))
        
        
        value = getattr(self, "error_codes")
        
        payload = json.dumps(value).encode("utf-8")
        packed_parts.append(struct.pack("!I", len(payload)))
        packed_parts.append(payload)
        
        
        value = getattr(self, "uptime")
        
        packed_parts.append(struct.pack("!i", value))
        
        
        value = getattr(self, "maintenance_required")
        
        packed_parts.append(struct.pack("?", value))
        
        
        return b"".join(packed_parts)

    @classmethod
    def deserialize(cls, data: bytes):
        offset = 0
        values = {}
        
        
        values["device_id"] = struct.unpack_from("!i", data, offset)[0]
        offset += 4
        
        
        
        values["temperature"] = struct.unpack_from("!f", data, offset)[0]
        offset += 4
        
        
        
        values["is_active"] = struct.unpack_from("?", data, offset)[0]
        offset += 1
        
        
        
        length = struct.unpack_from("!I", data, offset)[0]
        offset += 4
        raw_payload = data[offset:offset + length]
        offset += length
        values["history"] = json.loads(raw_payload.decode("utf-8"))
        
        
        
        length = struct.unpack_from("!I", data, offset)[0]
        offset += 4
        raw_payload = data[offset:offset + length]
        offset += length
        values["status_message"] = raw_payload.decode("utf-8")
        
        
        
        length = struct.unpack_from("!I", data, offset)[0]
        offset += 4
        raw_payload = data[offset:offset + length]
        offset += length
        values["tags"] = json.loads(raw_payload.decode("utf-8"))
        
        
        
        values["battery_level"] = struct.unpack_from("!i", data, offset)[0]
        offset += 4
        
        
        
        values["is_encrypted"] = struct.unpack_from("?", data, offset)[0]
        offset += 1
        
        
        
        length = struct.unpack_from("!I", data, offset)[0]
        offset += 4
        raw_payload = data[offset:offset + length]
        offset += length
        values["last_updated"] = raw_payload.decode("utf-8")
        
        
        
        length = struct.unpack_from("!I", data, offset)[0]
        offset += 4
        raw_payload = data[offset:offset + length]
        offset += length
        values["location"] = json.loads(raw_payload.decode("utf-8"))
        
        
        
        length = struct.unpack_from("!I", data, offset)[0]
        offset += 4
        raw_payload = data[offset:offset + length]
        offset += length
        values["firmware_version"] = raw_payload.decode("utf-8")
        
        
        
        values["signal_strength"] = struct.unpack_from("!f", data, offset)[0]
        offset += 4
        
        
        
        length = struct.unpack_from("!I", data, offset)[0]
        offset += 4
        raw_payload = data[offset:offset + length]
        offset += length
        values["error_codes"] = json.loads(raw_payload.decode("utf-8"))
        
        
        
        values["uptime"] = struct.unpack_from("!i", data, offset)[0]
        offset += 4
        
        
        
        values["maintenance_required"] = struct.unpack_from("?", data, offset)[0]
        offset += 1
        
        
        return cls(**values)

    def __str__(self) -> str:
        lines = ["Odebrano i zdeserializowano dane:"]
        
        lines.append(f"  Device id: {getattr(self, 'device_id')}")
        
        lines.append(f"  Temperature: {getattr(self, 'temperature')}")
        
        lines.append(f"  Is active: {getattr(self, 'is_active')}")
        
        lines.append(f"  History: {getattr(self, 'history')}")
        
        lines.append(f"  Status message: {getattr(self, 'status_message')}")
        
        lines.append(f"  Tags: {getattr(self, 'tags')}")
        
        lines.append(f"  Battery level: {getattr(self, 'battery_level')}")
        
        lines.append(f"  Is encrypted: {getattr(self, 'is_encrypted')}")
        
        lines.append(f"  Last updated: {getattr(self, 'last_updated')}")
        
        lines.append(f"  Location: {getattr(self, 'location')}")
        
        lines.append(f"  Firmware version: {getattr(self, 'firmware_version')}")
        
        lines.append(f"  Signal strength: {getattr(self, 'signal_strength')}")
        
        lines.append(f"  Error codes: {getattr(self, 'error_codes')}")
        
        lines.append(f"  Uptime: {getattr(self, 'uptime')}")
        
        lines.append(f"  Maintenance required: {getattr(self, 'maintenance_required')}")
        
        return "\n".join(lines)