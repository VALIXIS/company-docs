import os

def update_projects_page(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    old_section_target = """    <!-- 2. Active Development -->
    <section class="lifecycle-group">
      <div class="group-header">
        <span class="group-indicator ind-active"></span>
        <h2 class="group-title">2. Active Engineering Pipelines</h2>
      </div>

      <div class="project-grid">
        <div class="project-card">
          <h3 class="p-title">VALIXIS Flow</h3>
          <p class="p-desc">
            Autonomous agent workflow engine that manages distributed task queues, background intelligence pipelines, and lead analysis workflows with minimal latency.
          </p>
          <div class="p-tags">
            <span class="p-tag" style="color: var(--valixis-cyan); border-color: rgba(0,217,255,0.3);">In Development</span>
            <span class="p-tag">Python Daemons</span>
            <span class="p-tag">Agent Swarms</span>
            <span class="p-tag">Event Queues</span>
          </div>
        </div>

        <div class="project-card">
          <h3 class="p-title">Fitora</h3>
          <p class="p-desc">
            Next-generation consumer AI mobile platform combining real-time computer vision analysis with adaptive physical conditioning and bio-metric feedback.
          </p>
          <div class="p-tags">
            <span class="p-tag" style="color: var(--valixis-cyan); border-color: rgba(0,217,255,0.3);">Alpha Testing</span>
            <span class="p-tag">Flutter Mobile</span>
            <span class="p-tag">Vision Inference</span>
            <span class="p-tag">Adaptive Routines</span>
          </div>
        </div>

        <div class="project-card">
          <h3 class="p-title">VALIXIS Pulse</h3>
          <p class="p-desc">
            Observability and live telemetry dashboard tracking mesh network health, service uptime, event dispatch ratios, and node memory loads in real-time.
          </p>
          <div class="p-tags">
            <span class="p-tag" style="color: var(--valixis-cyan); border-color: rgba(0,217,255,0.3);">In Development</span>
            <span class="p-tag">Telemetry API</span>
            <span class="p-tag">Real-Time Metrics</span>
            <span class="p-tag">Node Health</span>
          </div>
        </div>

        <div class="project-card">
          <h3 class="p-title">VALIXIS Desk-AI</h3>
          <p class="p-desc">
            Native desktop workspace integrating local system-level neural models, automated engineering utilities, and background system health oversight.
          </p>
          <div class="p-tags">
            <span class="p-tag" style="color: var(--valixis-cyan); border-color: rgba(0,217,255,0.3);">Prototyping</span>
            <span class="p-tag">Local LLM Inference</span>
            <span class="p-tag">System Daemon</span>
            <span class="p-tag">Context Orchestration</span>
          </div>
        </div>
      </div>
    </section>

    <!-- 3. Planned & Research Pipeline -->
    <section class="lifecycle-group">
      <div class="group-header">
        <span class="group-indicator ind-planned"></span>
        <h2 class="group-title">3. Planned &amp; Frontier Research</h2>
      </div>

      <div class="project-grid">
        <div class="project-card">
          <h3 class="p-title">VALIXIS Cloud</h3>
          <p class="p-desc">
            Sovereign cloud storage and peer-to-peer distributed node mesh designed for cryptographic security, private key ownership, and decentralized file verification.
          </p>
          <div class="p-tags">
            <span class="p-tag" style="color: #A78BFA; border-color: rgba(124,58,237,0.3);">Architectural Research</span>
            <span class="p-tag">Distributed Storage</span>
            <span class="p-tag">Edge Cryptography</span>
          </div>
        </div>

        <div class="project-card">
          <h3 class="p-title">VALIXIS Gaming Studio (Next-Gen Titles)</h3>
          <p class="p-desc">
            Original interactive 3D simulations and video game titles exploring real-time rendering, procedural world generation, and spatial player dynamics.
          </p>
          <div class="p-tags">
            <span class="p-tag" style="color: #A78BFA; border-color: rgba(124,58,237,0.3);">Conceptual Phase</span>
            <span class="p-tag">Real-Time 3D</span>
            <span class="p-tag">Physics Engines</span>
            <span class="p-tag">Interactive Media</span>
          </div>
        </div>
      </div>
    </section>"""

    new_section = """    <!-- 2. Active Development Pipelines -->
    <section class="lifecycle-group">
      <div class="group-header">
        <span class="group-indicator ind-active"></span>
        <h2 class="group-title">2. Active Development Pipelines</h2>
      </div>

      <div class="project-grid">
        <div class="project-card">
          <h3 class="p-title">VALIXIS FLOW</h3>
          <p class="p-desc">
            Autonomous agent workflow engine managing continuous background task queues, human-paced email dispatch via Resend API, and real-time Telegram bot alerts.
          </p>
          <div class="p-tags">
            <span class="p-tag" style="color: var(--valixis-cyan); border-color: rgba(0,217,255,0.3);">Active Development</span>
            <span class="p-tag">Python Daemons</span>
            <span class="p-tag">Resend API</span>
            <span class="p-tag">Telegram Bot</span>
          </div>
          <div style="margin-top:14px;"><a href="../ecosystem/#flow" style="display:inline-flex; align-items:center; gap:6px; font-size:12px; font-weight:600; color:var(--valixis-cyan); text-decoration:none;"><span>Inspect FLOW Specifications</span> &rarr;</a></div>
        </div>

        <div class="project-card">
          <h3 class="p-title">VALIXIS PULSE</h3>
          <p class="p-desc">
            Real-time observability and fleet telemetry dashboard tracking multi-node server health, worker daemon latency, and website availability across all deployments.
          </p>
          <div class="p-tags">
            <span class="p-tag" style="color: var(--valixis-cyan); border-color: rgba(0,217,255,0.3);">Active Development</span>
            <span class="p-tag">Telemetry API</span>
            <span class="p-tag">WebSockets</span>
            <span class="p-tag">Fleet Health</span>
          </div>
          <div style="margin-top:14px;"><a href="../ecosystem/#pulse" style="display:inline-flex; align-items:center; gap:6px; font-size:12px; font-weight:600; color:var(--valixis-cyan); text-decoration:none;"><span>Inspect PULSE Specifications</span> &rarr;</a></div>
        </div>
      </div>
    </section>

    <!-- 3. Active Prototypes & Staging Builds -->
    <section class="lifecycle-group">
      <div class="group-header">
        <span class="group-indicator" style="background: #F59E0B; box-shadow: 0 0 10px #F59E0B;"></span>
        <h2 class="group-title">3. Active Prototypes &amp; Staging Builds</h2>
      </div>

      <div class="project-grid">
        <div class="project-card">
          <h3 class="p-title">Fitora</h3>
          <p class="p-desc">
            Next-generation consumer AI mobile platform combining real-time computer vision 33-point pose estimation with adaptive physical conditioning and biomechanical feedback.
          </p>
          <div class="p-tags">
            <span class="p-tag" style="color: #F59E0B; border-color: rgba(245,158,11,0.3);">Prototype (Alpha)</span>
            <span class="p-tag">Flutter Mobile</span>
            <span class="p-tag">MediaPipe / TFLite</span>
            <span class="p-tag">Vision Inference</span>
          </div>
          <div style="margin-top:14px;"><a href="../ecosystem/#fitora" style="display:inline-flex; align-items:center; gap:6px; font-size:12px; font-weight:600; color:#F59E0B; text-decoration:none;"><span>Inspect Fitora Prototype</span> &rarr;</a></div>
        </div>

        <div class="project-card">
          <h3 class="p-title">VALIXIS DESK_AI</h3>
          <p class="p-desc">
            Native desktop cognitive workspace integrating localized neural models (GGUF/ONNX), automated engineering utilities, and background system health oversight without cloud leakage.
          </p>
          <div class="p-tags">
            <span class="p-tag" style="color: #F59E0B; border-color: rgba(245,158,11,0.3);">Prototype</span>
            <span class="p-tag">Local LLM</span>
            <span class="p-tag">Tauri / Electron</span>
            <span class="p-tag">Zero Telemetry</span>
          </div>
          <div style="margin-top:14px;"><a href="../ecosystem/#desk-ai" style="display:inline-flex; align-items:center; gap:6px; font-size:12px; font-weight:600; color:#F59E0B; text-decoration:none;"><span>Inspect DESK_AI Prototype</span> &rarr;</a></div>
        </div>
      </div>
    </section>

    <!-- 4. Planned & Frontier Research -->
    <section class="lifecycle-group">
      <div class="group-header">
        <span class="group-indicator ind-planned"></span>
        <h2 class="group-title">4. Planned &amp; Frontier Research</h2>
      </div>

      <div class="project-grid">
        <div class="project-card">
          <h3 class="p-title">VALIXIS CLOUD</h3>
          <p class="p-desc">
            Sovereign cloud storage and peer-to-peer distributed node mesh designed for cryptographic security, client-side envelope key ownership, and decentralized data resilience.
          </p>
          <div class="p-tags">
            <span class="p-tag" style="color: #A78BFA; border-color: rgba(124,58,237,0.3);">Planned</span>
            <span class="p-tag">Distributed Storage</span>
            <span class="p-tag">AES-256-GCM</span>
            <span class="p-tag">P2P Mesh</span>
          </div>
          <div style="margin-top:14px;"><a href="../ecosystem/#cloud" style="display:inline-flex; align-items:center; gap:6px; font-size:12px; font-weight:600; color:#A78BFA; text-decoration:none;"><span>View CLOUD Architecture</span> &rarr;</a></div>
        </div>

        <div class="project-card">
          <h3 class="p-title">VALIXIS Gaming Studio</h3>
          <p class="p-desc">
            Original interactive 3D simulations, real-time spatial computing, and WebGL physics titles exploring real-time rendering, procedural world mechanics, and digital storytelling.
          </p>
          <div class="p-tags">
            <span class="p-tag" style="color: #A78BFA; border-color: rgba(124,58,237,0.3);">Planned</span>
            <span class="p-tag">Three.js / WebGL2</span>
            <span class="p-tag">GLSL Shaders</span>
            <span class="p-tag">Spatial Computing</span>
          </div>
          <div style="margin-top:14px;"><a href="../ecosystem/#gaming-studio" style="display:inline-flex; align-items:center; gap:6px; font-size:12px; font-weight:600; color:#A78BFA; text-decoration:none;"><span>View Gaming Studio Vision</span> &rarr;</a></div>
        </div>
      </div>
    </section>"""

    # Also update Portal card link
    portal_target = """          <div class="p-tags">
            <span class="p-tag" style="color: #10B981; border-color: rgba(16,185,129,0.3);">Live Production</span>
            <span class="p-tag">Flutter Web</span>
            <span class="p-tag">Supabase RLS</span>
            <span class="p-tag">GitHub Actions</span>
          </div>
        </div>"""
    
    portal_replacement = """          <div class="p-tags">
            <span class="p-tag" style="color: #10B981; border-color: rgba(16,185,129,0.3);">Live / Launched</span>
            <span class="p-tag">Flutter Web</span>
            <span class="p-tag">Supabase RLS</span>
            <span class="p-tag">GitHub Actions</span>
          </div>
          <div style="margin-top:14px;"><a href="../ecosystem/#portal" style="display:inline-flex; align-items:center; gap:6px; font-size:12px; font-weight:600; color:#10B981; text-decoration:none;"><span>Inspect Portal Platform</span> &rarr;</a></div>
        </div>"""

    if portal_target in content:
        content = content.replace(portal_target, portal_replacement)

    if old_section_target in content:
        content = content.replace(old_section_target, new_section)
    else:
        print("Note: old_section_target was not an exact match in", filepath)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

for p in ['projects/index.html', 'VALIXIS WEBSITE/projects/index.html']:
    if os.path.exists(p):
        update_projects_page(p)
