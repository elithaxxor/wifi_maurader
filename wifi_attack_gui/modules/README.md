
⸻

📡 modules/packet_capture.py

View full file here →
(Threaded PyShark capture, live packet logging, pcap saving, monitor mode toggling.)

⸻

🎯 modules/evil_twin.py

View full file here →
(Launches rogue AP with hostapd, dnsmasq; serves phishing portal via Flask.)

⸻

🎭 modules/phishing_portal_loader.py

View full file here →
(Manages phishing template switching and previews for the evil twin.)

⸻

✅ encrypt_portals.py:
	•	Generates an AES key (saved to .enc_key)
	•	Encrypts each file inside phishing_templates/<template>/
	•	Stores output as .enc files alongside originals

 
