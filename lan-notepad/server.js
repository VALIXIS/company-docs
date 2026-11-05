const http = require('http');
const fs = require('fs');
const path = require('path');
const os = require('os');

const PORT = process.env.PORT || 5000;
const DATA_FILE = path.join(__dirname, 'data', 'store.json');
const UPLOADS_DIR = path.join(__dirname, 'uploads');
const PUBLIC_DIR = path.join(__dirname, 'public');

// Initialize data storage
if (!fs.existsSync(UPLOADS_DIR)) fs.mkdirSync(UPLOADS_DIR, { recursive: true });
if (!fs.existsSync(path.dirname(DATA_FILE))) fs.mkdirSync(path.dirname(DATA_FILE), { recursive: true });

let store = {
  notepadText: `# Welcome to LAN Notepad & Command Hub! 🚀
- Real-time sync between your current laptop and older laptop.
- Edit text here or post quick commands in the Snippets tab below.
- Everything typed here syncs instantly over your local Wi-Fi.`,
  snippets: [
    {
      id: 'demo-1',
      title: 'PowerShell Ping Test',
      type: 'command',
      content: 'ping 192.168.31.30',
      timestamp: new Date().toISOString()
    },
    {
      id: 'demo-2',
      title: 'Quick Git Status',
      type: 'command',
      content: 'git status',
      timestamp: new Date().toISOString()
    }
  ],
  files: []
};

// Load existing state if available
if (fs.existsSync(DATA_FILE)) {
  try {
    const raw = fs.readFileSync(DATA_FILE, 'utf-8');
    store = { ...store, ...JSON.parse(raw) };
  } catch (err) {
    console.error('Error loading store.json:', err.message);
  }
}

function saveStore() {
  try {
    fs.writeFileSync(DATA_FILE, JSON.stringify(store, null, 2), 'utf-8');
  } catch (err) {
    console.error('Error saving store.json:', err.message);
  }
}

// Active Server-Sent Events (SSE) clients
const sseClients = new Set();

function broadcastSSE(data) {
  const payload = `data: ${JSON.stringify(data)}\n\n`;
  for (const res of sseClients) {
    try {
      res.write(payload);
    } catch {
      sseClients.delete(res);
    }
  }
}

function getNetworkAddresses() {
  const nets = os.networkInterfaces();
  const addresses = [];
  for (const name of Object.keys(nets)) {
    for (const net of nets[name]) {
      if (net.family === 'IPv4' && !net.internal) {
        addresses.push({ interface: name, address: net.address });
      }
    }
  }
  return addresses;
}

// Request dispatcher
const server = http.createServer((req, res) => {
  // CORS & Security headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, DELETE, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    return;
  }

  const parsedUrl = new URL(req.url, `http://${req.headers.host}`);
  const pathname = parsedUrl.pathname;

  // 1. SSE Stream
  if (pathname === '/events' && req.method === 'GET') {
    res.writeHead(200, {
      'Content-Type': 'text/event-stream',
      'Cache-Control': 'no-cache',
      'Connection': 'keep-alive'
    });
    res.write(`data: ${JSON.stringify({ type: 'init', clientCount: sseClients.size + 1 })}\n\n`);
    sseClients.add(res);

    broadcastSSE({ type: 'client_count', count: sseClients.size });

    req.on('close', () => {
      sseClients.delete(res);
      broadcastSSE({ type: 'client_count', count: sseClients.size });
    });
    return;
  }

  // 2. Network Addresses API
  if (pathname === '/api/network' && req.method === 'GET') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ port: PORT, interfaces: getNetworkAddresses() }));
    return;
  }

  // 3. Full State API
  if (pathname === '/api/state' && req.method === 'GET') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify(store));
    return;
  }

  // 4. Update Notepad Text
  if (pathname === '/api/notepad' && req.method === 'POST') {
    let body = '';
    req.on('data', chunk => { body += chunk; });
    req.on('end', () => {
      try {
        const payload = JSON.parse(body || '{}');
        store.notepadText = typeof payload.text === 'string' ? payload.text : store.notepadText;
        saveStore();
        broadcastSSE({
          type: 'notepad_update',
          text: store.notepadText,
          senderId: payload.senderId || 'unknown'
        });
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ success: true }));
      } catch (e) {
        res.writeHead(400, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: e.message }));
      }
    });
    return;
  }

  // 5. Add Snippet / Command
  if (pathname === '/api/snippet' && req.method === 'POST') {
    let body = '';
    req.on('data', chunk => { body += chunk; });
    req.on('end', () => {
      try {
        const payload = JSON.parse(body || '{}');
        if (!payload.content) {
          res.writeHead(400, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ error: 'content is required' }));
          return;
        }
        const snippet = {
          id: Date.now().toString(36) + Math.random().toString(36).substring(2, 6),
          title: (payload.title || '').trim() || (payload.type === 'command' ? 'Terminal Command' : 'Quick Note'),
          type: payload.type || 'command',
          content: payload.content,
          timestamp: new Date().toISOString()
        };
        store.snippets.unshift(snippet);
        saveStore();
        broadcastSSE({ type: 'snippet_added', snippet });
        res.writeHead(201, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ success: true, snippet }));
      } catch (e) {
        res.writeHead(400, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: e.message }));
      }
    });
    return;
  }

  // 6. Delete Snippet
  if (pathname.startsWith('/api/snippet/') && req.method === 'DELETE') {
    const id = pathname.replace('/api/snippet/', '');
    store.snippets = store.snippets.filter(s => s.id !== id);
    saveStore();
    broadcastSSE({ type: 'snippet_deleted', id });
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ success: true }));
    return;
  }

  // 7. Clear All Snippets
  if (pathname === '/api/snippets/clear' && req.method === 'POST') {
    store.snippets = [];
    saveStore();
    broadcastSSE({ type: 'snippets_cleared' });
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ success: true }));
    return;
  }

  // 8. Upload File
  if (pathname === '/api/upload' && req.method === 'POST') {
    const rawFileName = req.headers['x-file-name'];
    if (!rawFileName) {
      res.writeHead(400, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ error: 'x-file-name header required' }));
      return;
    }
    const cleanFileName = Date.now() + '_' + path.basename(decodeURIComponent(rawFileName)).replace(/[^a-zA-Z0-9._-]/g, '_');
    const filePath = path.join(UPLOADS_DIR, cleanFileName);
    const writeStream = fs.createWriteStream(filePath);

    req.pipe(writeStream);
    req.on('end', () => {
      const stats = fs.statSync(filePath);
      const fileInfo = {
        id: cleanFileName,
        name: decodeURIComponent(rawFileName),
        storedAs: cleanFileName,
        size: stats.size,
        timestamp: new Date().toISOString()
      };
      store.files.unshift(fileInfo);
      saveStore();
      broadcastSSE({ type: 'file_added', file: fileInfo });
      res.writeHead(201, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ success: true, file: fileInfo }));
    });
    req.on('error', (err) => {
      res.writeHead(500, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ error: err.message }));
    });
    return;
  }

  // 9. Download File
  if (pathname.startsWith('/uploads/') && req.method === 'GET') {
    const fileName = path.basename(pathname);
    const filePath = path.join(UPLOADS_DIR, fileName);
    if (!fs.existsSync(filePath)) {
      res.writeHead(404, { 'Content-Type': 'text/plain' });
      res.end('File not found');
      return;
    }
    const fileRecord = store.files.find(f => f.storedAs === fileName);
    const downloadName = fileRecord ? fileRecord.name : fileName;
    res.writeHead(200, {
      'Content-Disposition': `attachment; filename="${encodeURIComponent(downloadName)}"`,
      'Content-Type': 'application/octet-stream'
    });
    fs.createReadStream(filePath).pipe(res);
    return;
  }

  // 10. Delete File
  if (pathname.startsWith('/api/file/') && req.method === 'DELETE') {
    const fileId = pathname.replace('/api/file/', '');
    const filePath = path.join(UPLOADS_DIR, fileId);
    if (fs.existsSync(filePath)) {
      try { fs.unlinkSync(filePath); } catch {}
    }
    store.files = store.files.filter(f => f.storedAs !== fileId);
    saveStore();
    broadcastSSE({ type: 'file_deleted', fileId });
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ success: true }));
    return;
  }

  // 11. Static files (public/index.html, etc.)
  let staticPath = path.join(PUBLIC_DIR, pathname === '/' ? 'index.html' : pathname);
  if (fs.existsSync(staticPath) && fs.statSync(staticPath).isFile()) {
    const ext = path.extname(staticPath).toLowerCase();
    const mimeTypes = {
      '.html': 'text/html; charset=utf-8',
      '.css': 'text/css; charset=utf-8',
      '.js': 'application/javascript; charset=utf-8',
      '.json': 'application/json; charset=utf-8',
      '.svg': 'image/svg+xml',
      '.ico': 'image/x-icon'
    };
    res.writeHead(200, { 'Content-Type': mimeTypes[ext] || 'application/octet-stream' });
    fs.createReadStream(staticPath).pipe(res);
    return;
  }

  // Fallback 404
  res.writeHead(404, { 'Content-Type': 'text/plain' });
  res.end('Not Found');
});

server.listen(PORT, '0.0.0.0', () => {
  const networks = getNetworkAddresses();
  console.log('\n======================================================');
  console.log(`🌐 LAN Notepad & Command Hub is running!`);
  console.log('======================================================');
  console.log(`💻 This Laptop (Localhost):  http://localhost:${PORT}`);
  networks.forEach(net => {
    console.log(`📡 ${net.interface.padEnd(20)}: http://${net.address}:${PORT}`);
  });
  console.log('======================================================');
  console.log(`👉 Open the Wi-Fi link on your older laptop!`);
  console.log('======================================================\n');
});
