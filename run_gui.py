#!/bin/bash
echo "[*] Starting Evil Twin Toolkit..."
cd backend
uvicorn api_server:app --host 0.0.0.0 --port 8000 --reload
