# Wi-Fi Attack Toolkit (Red Team Edition) 💀

A cross-platform Evil Twin and OSINT attack suite with full GUI and CLI support.

## 🎯 Features

- Rogue AP control (start/stop SSID)
- Live packet capture (PyShark)
- Credential log streaming
- Phishing template encryption (AES)
- Snapshot replay viewer
- OSINT graph (MAC/IP/ORG visual)
- Encrypted shell dropper deployment
- Cross-platform GUI: React + Tkinter fallback

---

## 🖥 GUI Overview

- Sidebar navigation (Dashboard, OSINT, Terminal, Downloads)
- Classic hacker-style font, green-on-black
- Auto-refreshing logs and packet feed
- Template selector and live activation

---

## 🔐 Encrypted Phishing Templates

Use `encrypt_portals.py` to encrypt:
```bash
python3 encrypt_portals.py

Then activate via GUI or API — a passphrase will be required.

⸻

🧠 OSINT Graph

Interactive graph displays:
	•	MAC ⇔ IP ⇔ Hostname ⇔ Org relationships
	•	Placeholder data supported
	•	Expandable via SpiderFoot or Shodan API

⸻

📊 Snapshot Viewer

Capture logs and PCAPs timestamped:
	•	Replay mode re-generates graphs and logs
	•	Perfect for audits, demos, or forensic reports

⸻

🛠 Installation (Linux/macOS)

chmod +x install.command
./install.command

On Linux:

chmod +x setup_and_run.sh
./setup_and_run.sh

Then launch with:

source venv/bin/activate
./run_gui.sh



⸻

🪟 Windows Notes

Use Git Bash or WSL for compatibility. Execute:

bash setup_and_run.sh



⸻

📦 Files

File	Purpose
setup_and_run.sh	Python venv + deps installer
run_gui.sh	Starts backend
frontend/src/	React GUI frontend
backend/api_server.py	FastAPI backend
modules/	Packet capture, phishing, etc.
encrypt_portals.py	Encrypts phishing templates (AES)
install.command	macOS install wrapper



⸻

🧨 Shell Dropper Usage

Use dropper script with AES-encrypted shell payloads. On decrypt:
	•	Decrypted payload runs in memory
	•	Supports self-delete, timed beacon

⸻

🔚 Credits

Dont do stupid shit with my work. Use responsibly, test legally. ⚔
~ elithaxxor

------------
```javascript 
import OSINT from './Pages/OSINT';
import Terminal from './Pages/Terminal';
import Downloads from './Pages/Downloads';
import Dashboard from './Pages/Dashboard';

const App = () => (
  <Router>
    <div className="min-h-screen bg-black text-green-400 font-mono flex">
      <aside className="w-60 bg-zinc-900 border-r border-green-700 p-4 space-y-4">
        <h1 className="text-xl border-b border-green-500 pb-2">☠ Toolkit Nav</h1>
        <nav className="space-y-2">
          <Link to="/" className="block hover:text-green-200">Dashboard</Link>
          <Link to="/osint" className="block hover:text-green-200">OSINT</Link>
          <Link to="/downloads" className="block hover:text-green-200">Downloads</Link>
          <Link to="/terminal" className="block hover:text-green-200">Mini Terminal</Link>
        </nav>
      </aside>
      <main className="flex-1 p-6">
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/osint" element={<OSINT />} />
          <Route path="/downloads" element={<Downloads />} />
          <Route path="/terminal" element={<Terminal />} />
        </Routes>
      </main>
    </div>
  </Router>
);
export default App;
```


