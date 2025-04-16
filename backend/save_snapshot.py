import json
import os
from datetime import datetime
from pathlib import Path

from wifi_attack_gui.modules.packet_capture import PacketCapture

SNAPSHOT_DIR = Path("./snapshots")
LOGS_DIR = Path("./phishing_portal/logs")

def get_latest_credentials():
    entries = []
    if LOGS_DIR.exists():
        for file in LOGS_DIR.glob("creds_*.txt"):
            with open(file) as f:
                entries.extend(line.strip() for line in f if line.strip())
    return entries

def save_snapshot():
    snapshot = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "packets": [],
        "credentials": get_latest_credentials()
    }

    pcap = PacketCapture()
    snapshot["packets"] = pcap.get_live_packets(limit=50)

    SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = SNAPSHOT_DIR / f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
    with open(out_path, "w") as f:
        json.dump(snapshot, f, indent=2)

    print(f"✅ Snapshot saved to: {out_path}")

if __name__ == "__main__":
    save_snapshot()
