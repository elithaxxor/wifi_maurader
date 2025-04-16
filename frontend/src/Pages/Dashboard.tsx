import React, { useState, useEffect } from 'react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';

const Dashboard = () => {
  const [ssid, setSsid] = useState('Free_Public_WiFi');
  const [templates, setTemplates] = useState<string[]>([]);
  const [selectedTemplate, setSelectedTemplate] = useState('');

  useEffect(() => {
    fetch('/api/templates')
      .then(res => res.json())
      .then(data => setTemplates(data));
  }, []);

  const activateTemplate = () => {
    fetch('/api/activate_template', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name: selectedTemplate })
    });
  };

  const startEvilTwin = () => {
    fetch('/api/start_ap', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ ssid })
    });
  };

  const stopEvilTwin = () => {
    fetch('/api/stop_ap', { method: 'POST' });
  };

  const saveSnapshot = () => {
    fetch('/api/save_snapshot', { method: 'POST' })
      .then(() => alert('📸 Snapshot saved!'))
      .catch(() => alert('⚠️ Failed to save snapshot.'));
  };

  return (
    <div className="p-4 text-green-400 font-mono bg-black min-h-screen">
      <h1 className="text-2xl border-b border-green-400 pb-2 mb-4">Evil Twin Control Panel</h1>

      <div className="mb-4">
        <label>SSID:</label>
        <Input className="bg-black border-green-500 text-green-300" value={ssid} onChange={e => setSsid(e.target.value)} />
      </div>

      <div className="mb-4">
        <label>Template:</label>
        <select
          className="bg-black text-green-300 border border-green-400 p-2"
          value={selectedTemplate}
          onChange={e => setSelectedTemplate(e.target.value)}
        >
          <option value="">Choose template</option>
          {templates.map((t, i) => (
            <option key={i} value={t}>{t}</option>
          ))}
        </select>
      </div>

      <div className="flex gap-2 flex-wrap mt-4">
        <Button onClick={activateTemplate} className="bg-blue-600 text-black">Activate Template</Button>
        <Button onClick={startEvilTwin} className="bg-green-600 text-black">Start AP</Button>
        <Button onClick={stopEvilTwin} className="bg-red-600 text-black">Stop AP</Button>
        <Button onClick={saveSnapshot} className="bg-purple-600 text-black">📸 Save Snapshot</Button>
      </div>
    </div>
  );
};

export default Dashboard;
