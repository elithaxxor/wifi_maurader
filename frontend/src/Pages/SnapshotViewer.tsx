import React, { useEffect, useState } from 'react';

const SnapshotViewer = () => {
  const [snapshots, setSnapshots] = useState([]);
  const [selected, setSelected] = useState(null);

  useEffect(() => {
    fetch('/api/snapshots')
      .then(res => res.json())
      .then(data => setSnapshots(data));
  }, []);

  return (
    <div className="bg-black text-green-400 p-6 min-h-screen font-mono">
      <h1 className="text-2xl border-b border-green-500 mb-4">📂 Snapshot Viewer</h1>
      <div className="mb-4">
        {snapshots.map((s: any, i) => (
          <button
            key={i}
            className="mr-2 mb-2 px-4 py-1 bg-zinc-800 border border-green-400 hover:bg-green-700"
            onClick={() => setSelected(s)}
          >
            {s.timestamp}
          </button>
        ))}
      </div>

      {selected && (
        <div className="bg-zinc-900 p-4 mt-4 rounded">
          <h2 className="text-xl mb-2">Snapshot: {selected.timestamp}</h2>
          <pre className="whitespace-pre-wrap text-green-200 text-sm">{JSON.stringify(selected.data, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

export default SnapshotViewer;
