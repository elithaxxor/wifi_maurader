# wifi_attack_gui/modules/packet_capture.py
# Real-time packet capture module using tshark
# Requires: tshark, pyshark, airmon-ng

import os
import subprocess
import threading
import pyshark
from datetime import datetime

CAPTURE_INTERFACE = 'wlan0mon'  # dynamically change via GUI settings later
CAPTURE_FOLDER = './captures'
os.makedirs(CAPTURE_FOLDER, exist_ok=True)

class PacketCapture:
    def __init__(self, interface=CAPTURE_INTERFACE):
        self.interface = interface
        self.capture = None
        self.thread = None
        self.running = False
        self.live_packets = []

    def _start_capture_thread(self):
        self.running = True
        self.capture = pyshark.LiveCapture(interface=self.interface)

        def sniff():
            for packet in self.capture.sniff_continuously():
                if not self.running:
                    break
                try:
                    self.live_packets.append({
                        'time': packet.sniff_time.strftime("%H:%M:%S"),
                        'src': packet["wlan"].sa if hasattr(packet, "wlan") else "N/A",
                        'dst': packet["wlan"].da if hasattr(packet, "wlan") else "N/A",
                        'protocol': packet.highest_layer,
                        'summary': packet.summary
                    })
                except Exception as e:
                    print(f"Error processing packet: {e}")

        self.thread = threading.Thread(target=sniff, daemon=True)
        self.thread.start()

    def start(self):
        if not self.running:
            self._start_capture_thread()

    def stop(self):
        self.running = False
        if self.capture:
            self.capture.close()

    def save_to_pcap(self):
        filename = os.path.join(CAPTURE_FOLDER, f"capture_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pcap")
        command = [
            'tshark',
            '-i', self.interface,
            '-a', 'duration:60',
            '-w', filename
        ]
        subprocess.run(command)
        return filename

    def get_live_packets(self, limit=50):
        return self.live_packets[-limit:]


def enable_monitor_mode(interface='wlan0'):
    subprocess.run(['airmon-ng', 'start', interface])

def disable_monitor_mode(interface='wlan0mon'):
    subprocess.run(['airmon-ng', 'stop', interface])


if __name__ == '__main__':
    enable_monitor_mode()
    pc = PacketCapture()
    pc.start()
    try:
        while True:
            packets = pc.get_live_packets()
            print(f"Captured {len(packets)} packets")
            for p in packets[-5:]:
                print(p)
    except KeyboardInterrupt:
        pc.stop()
        disable_monitor_mode()
