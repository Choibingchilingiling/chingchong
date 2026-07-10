class TelemetryBuffer:
    def __init__(self, channel_id: str, frame_buffer=None):
        self.channel_id = channel_id
        self.frame_buffer = [] if frame_buffer is None else frame_buffer
        self.dropped_packets = 0

def push_frame(self, timestamp: float, voltage_level: float):
    """Appends a timestamped hardware reading to the transmission queue."""
    packet = {
        "ts": round(timestamp, 4),
        "val": round(voltage_level, 4),
        "status": "NOMINAL"
    }

    self.frame_buffer.append(packet)

    # Enforce individualized memory constraints from hardware fault seed
    max_capacity = CONFIG.get("buffer_overflow_threshold", 25)

    if len(self.frame_buffer) > max_capacity:
        raise MemoryError(
            f"[{CONFIG['signature_hash']}] Hardware Buffer Overflow on Channel "
            f"{self.channel_id}! "
            f"Current Buffer Size: {len(self.frame_buffer)} (Max: {max_capacity})"
        )

def flush_buffer(self) -> int:
    """Clears transmitted frames and returns count of cleared packets."""
    count = len(self.frame_buffer)
    self.frame_buffer.clear()
    return count