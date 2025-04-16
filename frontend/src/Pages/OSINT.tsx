import React, { useEffect, useRef } from 'react';
import ForceGraph3D from 'react-force-graph-3d';

const OSINT = () => {
  const fgRef = useRef<any>();

  const data = {
    nodes: [
      { id: 'MAC:00:11:22:33:44:55', group: 'mac' },
      { id: 'IP:192.168.1.10', group: 'ip' },
      { id: 'Hostname:corp-device', group: 'hostname' },
      { id: 'Org:Acme Corp', group: 'org' }
    ],
    links: [
      { source: 'MAC:00:11:22:33:44:55', target: 'IP:192.168.1.10' },
      { source: 'IP:192.168.1.10', target: 'Hostname:corp-device' },
      { source: 'Hostname:corp-device', target: 'Org:Acme Corp' }
    ]
  };

  return (
    <div className="h-screen bg-black">
      <ForceGraph3D
        ref={fgRef}
        graphData={data}
        nodeAutoColorBy="group"
        backgroundColor="#000000"
        linkColor={() => 'lime'}
        nodeLabel="id"
        nodeOpacity={0.9}
      />
    </div>
  );
};

export default OSINT;
