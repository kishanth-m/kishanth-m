#!/usr/bin/env python3
"""
Generates all auxiliary SVG components for Kishanth M.'s GitHub Profile:
- terminal.svg (Realistic futuristic interactive terminal)
- tech-universe.svg (Bento-style Cyberpunk Technical Universe)
- projects-matrix.svg (Futuristic project laboratory with Quantum Council prominence)
- current-focus.svg (AI Engineering Roadmap)
- connect.svg (Cyberpunk Social Connect Buttons)
- footer.svg (Animated developer signature)
"""

import os

ASSETS_DIR = os.path.join(".github", "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. TERMINAL WINDOW SVG
# -------------------------------------------------------------
def build_terminal_svg():
    width = 980
    height = 360
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto">
  <defs>
    <filter id="termGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
    <linearGradient id="termBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00FF66" stop-opacity="0.8" />
      <stop offset="50%" stop-color="#004d1f" stop-opacity="0.2" />
      <stop offset="100%" stop-color="#00f5d4" stop-opacity="0.7" />
    </linearGradient>
    <style>
      @keyframes blinkCursor {{
        0%, 49% {{ opacity: 1; }}
        50%, 100% {{ opacity: 0; }}
      }}
      @keyframes lineFadeIn {{
        0% {{ opacity: 0; }}
        100% {{ opacity: 1; }}
      }}
      .cursor {{
        animation: blinkCursor 1s infinite;
      }}
      .glow {{
        filter: drop-shadow(0 0 4px #00FF66);
      }}
    </style>
  </defs>

  <!-- Terminal Window Background -->
  <rect width="{width}" height="{height}" rx="10" fill="#060b08" />
  <rect x="1.5" y="1.5" width="{width-3}" height="{height-3}" rx="9" fill="none" stroke="url(#termBorder)" stroke-width="1.5" />
  
  <!-- Terminal Header / Titlebar -->
  <rect x="0" y="0" width="{width}" height="36" rx="10" fill="#0a140f" />
  <rect x="0" y="26" width="{width}" height="10" fill="#0a140f" />
  <line x1="0" y1="36" x2="{width}" y2="36" stroke="#00FF66" stroke-opacity="0.2" stroke-width="1" />
  
  <!-- Window Controls -->
  <circle cx="22" cy="18" r="5.5" fill="#ff5f56" />
  <circle cx="38" cy="18" r="5.5" fill="#ffbd2e" />
  <circle cx="54" cy="18" r="5.5" fill="#27c93f" />
  
  <!-- Window Title -->
  <g font-family="JetBrains Mono, Consolas, monospace" font-size="11" font-weight="bold">
    <text x="{width/2}" y="22" fill="#55FF99" text-anchor="middle" letter-spacing="1">kishanth@neural-matrix: ~/identity (zsh)</text>
    <text x="{width-24}" y="22" fill="#7a9988" font-size="9" text-anchor="end">SYS.ARCH: LINUX/AMD64</text>
  </g>

  <!-- Terminal Content Lines -->
  <g font-family="JetBrains Mono, Consolas, Courier New, monospace" font-size="13" font-weight="500">
    <!-- Command 1: whoami -->
    <g transform="translate(26, 68)">
      <text x="0" y="0" fill="#00f5d4" font-weight="700">&gt; $ whoami</text>
      <text x="0" y="22" fill="#E6FFF2" font-weight="600">Kishanth M. — Aspiring AI Engineer &amp; Generative AI Developer</text>
    </g>

    <!-- Command 2: education -->
    <g transform="translate(26, 126)">
      <text x="0" y="0" fill="#00f5d4" font-weight="700">&gt; $ cat /sys/education</text>
      <text x="0" y="22" fill="#55FF99">B.Tech — Artificial Intelligence and Data Science</text>
      <text x="0" y="40" fill="#7a9988" font-size="11.5">Institution: Adhiyamaan College of Engineering</text>
    </g>

    <!-- Command 3: current_focus -->
    <g transform="translate(26, 202)">
      <text x="0" y="0" fill="#00f5d4" font-weight="700">&gt; $ cat /sys/current_focus</text>
      <text x="0" y="22" fill="#00FF66" font-weight="600">Generative AI  |  LLMs  |  RAG Architecture  |  AI Agents &amp; Multi-Agent Systems</text>
      <text x="0" y="40" fill="#7a9988" font-size="11.5">Stack: LangChain, LangGraph, ChromaDB, PostgreSQL, Groq, Ollama, YOLOv8</text>
    </g>

    <!-- Command 4: mission -->
    <g transform="translate(26, 278)">
      <text x="0" y="0" fill="#00f5d4" font-weight="700">&gt; $ echo $MISSION_STATEMENT</text>
      <text x="0" y="22" fill="#E6FFF2" font-weight="700" letter-spacing="0.5">"Building practical intelligent systems that reason, collaborate, and perceive."</text>
    </g>

    <!-- Prompt line with blinking cursor -->
    <g transform="translate(26, 334)">
      <text x="0" y="0" fill="#00FF66" font-weight="700">kishanth@matrix-core:~$</text>
      <text x="210" y="0" fill="#a7f3d0" font-weight="500">python3 -m run_agent --collaborative</text>
      <rect x="532" y="-12" width="8.5" height="15" fill="#00FF66" class="cursor" />
    </g>
  </g>
</svg>'''
    
    path = os.path.join(ASSETS_DIR, "terminal.svg")
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {path}")

# -------------------------------------------------------------
# 2. TECHNICAL UNIVERSE BENTO SVG
# -------------------------------------------------------------
def build_tech_universe_svg():
    width = 980
    height = 540
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto">
  <defs>
    <linearGradient id="cardBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#09140e" stop-opacity="0.95" />
      <stop offset="100%" stop-color="#050a08" stop-opacity="0.95" />
    </linearGradient>
    <linearGradient id="neonBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00FF66" stop-opacity="0.6" />
      <stop offset="50%" stop-color="#004d1f" stop-opacity="0.2" />
      <stop offset="100%" stop-color="#00f5d4" stop-opacity="0.6" />
    </linearGradient>
    <style>
      .card-title {{ font-family: JetBrains Mono, Consolas, monospace; font-size: 11px; font-weight: 800; fill: #00f5d4; letter-spacing: 1.5px; }}
      .pill-text {{ font-family: JetBrains Mono, Consolas, monospace; font-size: 10px; font-weight: 600; fill: #E6FFF2; }}
      .sub-desc {{ font-family: JetBrains Mono, Consolas, monospace; font-size: 9px; fill: #7a9988; }}
      .pill-bg {{ fill: #0d2217; stroke: #00FF66; stroke-opacity: 0.35; stroke-width: 1; rx: 4; }}
      .tag-num {{ font-family: JetBrains Mono, Consolas, monospace; font-size: 9px; fill: #00FF66; font-weight: bold; opacity: 0.8; }}
    </style>
  </defs>

  <!-- Background Void -->
  <rect width="{width}" height="{height}" rx="12" fill="#040705" />
  
  <!-- Header Bar -->
  <g transform="translate(24, 28)">
    <text x="0" y="0" font-family="JetBrains Mono, Consolas, monospace" font-size="14" font-weight="900" fill="#00FF66" letter-spacing="2">⚡ MY TECHNICAL UNIVERSE // CORE STACK</text>
    <text x="{width-48}" y="0" font-family="JetBrains Mono, Consolas, monospace" font-size="9" fill="#7a9988" text-anchor="end">VERIFIED SKILLS ONLY // ZERO PLACEHOLDERS</text>
    <line x1="0" y1="12" x2="{width-48}" y2="12" stroke="#00FF66" stroke-opacity="0.25" stroke-width="1" />
  </g>

  <!-- 6 BENTO CARDS GRID (3 cols x 2 rows) -->
  
  <!-- CARD 1: Programming Languages -->
  <g transform="translate(24, 58)">
    <rect width="298" height="215" rx="8" fill="url(#cardBg)" stroke="url(#neonBorder)" stroke-width="1.2" />
    <text x="16" y="24" class="tag-num">01 // COMPUTATION</text>
    <text x="16" y="42" class="card-title">PROGRAMMING LANGUAGES</text>
    <line x1="16" y1="52" x2="282" y2="52" stroke="#00FF66" stroke-opacity="0.15" />
    
    <!-- Python -->
    <g transform="translate(16, 66)">
      <rect width="125" height="28" class="pill-bg" stroke="#00FF66" />
      <text x="10" y="18" class="pill-text">🐍 Python</text>
    </g>
    <!-- Java -->
    <g transform="translate(150, 66)">
      <rect width="125" height="28" class="pill-bg" />
      <text x="10" y="18" class="pill-text">☕ Java</text>
    </g>
    <!-- C -->
    <g transform="translate(16, 104)">
      <rect width="125" height="28" class="pill-bg" />
      <text x="10" y="18" class="pill-text">⚙️ C</text>
    </g>
    <!-- SQL -->
    <g transform="translate(150, 104)">
      <rect width="125" height="28" class="pill-bg" />
      <text x="10" y="18" class="pill-text">🗄️ SQL</text>
    </g>

    <!-- Core Paradigms -->
    <g transform="translate(16, 150)">
      <rect width="260" height="26" class="pill-bg" />
      <text x="10" y="17" class="pill-text">🧩 Object-Oriented Programming (OOP)</text>
    </g>
    <text x="16" y="200" class="sub-desc">Clean architecture &amp; scalable modular logic</text>
  </g>

  <!-- CARD 2: Artificial Intelligence & Generative AI -->
  <g transform="translate(341, 58)">
    <rect width="298" height="215" rx="8" fill="url(#cardBg)" stroke="url(#neonBorder)" stroke-width="1.2" />
    <text x="16" y="24" class="tag-num">02 // INTELLIGENCE</text>
    <text x="16" y="42" class="card-title">ARTIFICIAL INTELLIGENCE &amp; GENAI</text>
    <line x1="16" y1="52" x2="282" y2="52" stroke="#00FF66" stroke-opacity="0.15" />

    <!-- LLMs -->
    <g transform="translate(16, 66)">
      <rect width="125" height="28" class="pill-bg" />
      <text x="10" y="18" class="pill-text">⚡ LLMs</text>
    </g>
    <!-- RAG -->
    <g transform="translate(150, 66)">
      <rect width="125" height="28" class="pill-bg" />
      <text x="10" y="18" class="pill-text">📚 RAG Systems</text>
    </g>
    <!-- Prompt Engineering -->
    <g transform="translate(16, 104)">
      <rect width="260" height="28" class="pill-bg" />
      <text x="10" y="18" class="pill-text">🎯 Advanced Prompt Engineering</text>
    </g>
    <!-- Embeddings & Semantic Search -->
    <g transform="translate(16, 142)">
      <rect width="125" height="28" class="pill-bg" />
      <text x="10" y="18" class="pill-text">🧬 Embeddings</text>
    </g>
    <g transform="translate(150, 142)">
      <rect width="125" height="28" class="pill-bg" />
      <text x="10" y="18" class="pill-text">🔍 Semantic Search</text>
    </g>
    <text x="16" y="200" class="sub-desc">Grounding models with factual retrieval</text>
  </g>

  <!-- CARD 3: LLM Frameworks & Multi-Agent Development -->
  <g transform="translate(658, 58)">
    <rect width="298" height="215" rx="8" fill="url(#cardBg)" stroke="url(#neonBorder)" stroke-width="1.2" />
    <text x="16" y="24" class="tag-num">03 // ORCHESTRATION</text>
    <text x="16" y="42" class="card-title">FRAMEWORKS &amp; AI AGENTS</text>
    <line x1="16" y1="52" x2="282" y2="52" stroke="#00FF66" stroke-opacity="0.15" />

    <!-- LangChain -->
    <g transform="translate(16, 66)">
      <rect width="125" height="28" class="pill-bg" />
      <text x="10" y="18" class="pill-text">🦜🔗 LangChain</text>
    </g>
    <!-- LangGraph -->
    <g transform="translate(150, 66)">
      <rect width="125" height="28" class="pill-bg" />
      <text x="10" y="18" class="pill-text">🕸️ LangGraph</text>
    </g>
    <!-- Hugging Face -->
    <g transform="translate(16, 104)">
      <rect width="125" height="28" class="pill-bg" />
      <text x="10" y="18" class="pill-text">🤗 Hugging Face</text>
    </g>
    <!-- Ollama -->
    <g transform="translate(150, 104)">
      <rect width="125" height="28" class="pill-bg" />
      <text x="10" y="18" class="pill-text">🦙 Ollama (Local)</text>
    </g>
    <!-- Groq API -->
    <g transform="translate(16, 142)">
      <rect width="260" height="28" class="pill-bg" />
      <text x="10" y="18" class="pill-text">⚡ Groq API (High-Speed Inference)</text>
    </g>
    <text x="16" y="200" class="sub-desc">Multi-agent consensus &amp; cyclical workflows</text>
  </g>

  <!-- CARD 4: Vector Databases & Storage -->
  <g transform="translate(24, 292)">
    <rect width="298" height="215" rx="8" fill="url(#cardBg)" stroke="url(#neonBorder)" stroke-width="1.2" />
    <text x="16" y="24" class="tag-num">04 // KNOWLEDGE STORE</text>
    <text x="16" y="42" class="card-title">VECTOR DATABASES &amp; STORAGE</text>
    <line x1="16" y1="52" x2="282" y2="52" stroke="#00FF66" stroke-opacity="0.15" />

    <!-- ChromaDB -->
    <g transform="translate(16, 66)">
      <rect width="260" height="28" class="pill-bg" />
      <text x="10" y="18" class="pill-text">🟣 ChromaDB (Vector Store)</text>
    </g>
    <!-- PostgreSQL -->
    <g transform="translate(16, 104)">
      <rect width="260" height="28" class="pill-bg" />
      <text x="10" y="18" class="pill-text">🐘 PostgreSQL (Relational &amp; State Store)</text>
    </g>
    <!-- Persistent Memory -->
    <g transform="translate(16, 142)">
      <rect width="260" height="28" class="pill-bg" />
      <text x="10" y="18" class="pill-text">🧠 Conversational Checkpointing</text>
    </g>
    <text x="16" y="200" class="sub-desc">State persistence &amp; ultra-fast ANN search</text>
  </g>

  <!-- CARD 5: Computer Vision & Data Processing -->
  <g transform="translate(341, 292)">
    <rect width="298" height="215" rx="8" fill="url(#cardBg)" stroke="url(#neonBorder)" stroke-width="1.2" />
    <text x="16" y="24" class="tag-num">05 // PERCEPTION</text>
    <text x="16" y="42" class="card-title">COMPUTER VISION &amp; DATA</text>
    <line x1="16" y1="52" x2="282" y2="52" stroke="#00FF66" stroke-opacity="0.15" />

    <!-- OpenCV -->
    <g transform="translate(16, 66)">
      <rect width="125" height="28" class="pill-bg" />
      <text x="10" y="18" class="pill-text">👁️ OpenCV</text>
    </g>
    <!-- YOLOv8 -->
    <g transform="translate(150, 66)">
      <rect width="125" height="28" class="pill-bg" />
      <text x="10" y="18" class="pill-text">🎯 YOLOv8</text>
    </g>
    <!-- Pandas & NumPy -->
    <g transform="translate(16, 104)">
      <rect width="125" height="28" class="pill-bg" />
      <text x="10" y="18" class="pill-text">🐼 Pandas</text>
    </g>
    <g transform="translate(150, 104)">
      <rect width="125" height="28" class="pill-bg" />
      <text x="10" y="18" class="pill-text">🔢 NumPy</text>
    </g>
    <!-- Matplotlib -->
    <g transform="translate(16, 142)">
      <rect width="260" height="28" class="pill-bg" />
      <text x="10" y="18" class="pill-text">📊 Matplotlib (Data Visualization)</text>
    </g>
    <text x="16" y="200" class="sub-desc">Object detection, pose analysis, analytics</text>
  </g>

  <!-- CARD 6: Tools & Development Ecosystem -->
  <g transform="translate(658, 292)">
    <rect width="298" height="215" rx="8" fill="url(#cardBg)" stroke="url(#neonBorder)" stroke-width="1.2" />
    <text x="16" y="24" class="tag-num">06 // WORKSPACE</text>
    <text x="16" y="42" class="card-title">TOOLS &amp; ECOSYSTEM</text>
    <line x1="16" y1="52" x2="282" y2="52" stroke="#00FF66" stroke-opacity="0.15" />

    <!-- Git & GitHub -->
    <g transform="translate(16, 66)">
      <rect width="125" height="28" class="pill-bg" />
      <text x="10" y="18" class="pill-text">🐙 Git / GitHub</text>
    </g>
    <!-- VS Code -->
    <g transform="translate(150, 66)">
      <rect width="125" height="28" class="pill-bg" />
      <text x="10" y="18" class="pill-text">💻 VS Code</text>
    </g>
    <!-- Postman & REST APIs -->
    <g transform="translate(16, 104)">
      <rect width="125" height="28" class="pill-bg" />
      <text x="10" y="18" class="pill-text">📮 Postman</text>
    </g>
    <g transform="translate(150, 104)">
      <rect width="125" height="28" class="pill-bg" />
      <text x="10" y="18" class="pill-text">🌐 REST APIs</text>
    </g>
    <!-- Web Fundamentals -->
    <g transform="translate(16, 142)">
      <rect width="260" height="28" class="pill-bg" />
      <text x="10" y="18" class="pill-text">🎨 HTML5, CSS3, JSON Schema</text>
    </g>
    <text x="16" y="200" class="sub-desc">Robust CI/CD, modular code &amp; endpoints</text>
  </g>

</svg>'''

    path = os.path.join(ASSETS_DIR, "tech-universe.svg")
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {path}")

# -------------------------------------------------------------
# 3. FEATURED PROJECTS SVG
# -------------------------------------------------------------
def build_projects_svg():
    width = 980
    height = 680
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto">
  <defs>
    <filter id="neonAura" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
    <linearGradient id="quantumGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0e2a1b" stop-opacity="0.95" />
      <stop offset="50%" stop-color="#071710" stop-opacity="0.95" />
      <stop offset="100%" stop-color="#040a07" stop-opacity="0.95" />
    </linearGradient>
    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#09140e" stop-opacity="0.95" />
      <stop offset="100%" stop-color="#040806" stop-opacity="0.95" />
    </linearGradient>
    <linearGradient id="borderQuantum" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00FF66" />
      <stop offset="50%" stop-color="#00f5d4" />
      <stop offset="100%" stop-color="#00FF66" />
    </linearGradient>
    <style>
      @keyframes pulseNode {{
        0%, 100% {{ r: 4; opacity: 0.6; }}
        50% {{ r: 6.5; opacity: 1; filter: drop-shadow(0 0 4px #00FF66); }}
      }}
      @keyframes radarSweep {{
        0% {{ transform: rotate(0deg); }}
        100% {{ transform: rotate(360deg); }}
      }}
      .pulse-node {{ animation: pulseNode 2.5s infinite ease-in-out; }}
      .p-title {{ font-family: JetBrains Mono, Consolas, monospace; font-size: 15px; font-weight: 900; fill: #00FF66; letter-spacing: 1px; }}
      .p-tagline {{ font-family: JetBrains Mono, Consolas, monospace; font-size: 11px; font-weight: 700; fill: #00f5d4; }}
      .p-desc {{ font-family: JetBrains Mono, Consolas, monospace; font-size: 10px; fill: #a7f3d0; }}
      .tech-pill {{ font-family: JetBrains Mono, Consolas, monospace; font-size: 8.5px; fill: #55FF99; }}
      .btn-link:hover {{ filter: brightness(1.3); }}
    </style>
  </defs>

  <rect width="{width}" height="{height}" rx="12" fill="#040705" />

  <!-- Section Header -->
  <g transform="translate(24, 28)">
    <text x="0" y="0" font-family="JetBrains Mono, Consolas, monospace" font-size="14" font-weight="900" fill="#00FF66" letter-spacing="2">🧬 FEATURED AI PROJECTS // EXPERIMENTAL LAB</text>
    <text x="{width-48}" y="0" font-family="JetBrains Mono, Consolas, monospace" font-size="9" fill="#7a9988" text-anchor="end">PRODUCTION &amp; PROTOTYPE REPOSITORIES</text>
    <line x1="0" y1="12" x2="{width-48}" y2="12" stroke="#00FF66" stroke-opacity="0.25" stroke-width="1" />
  </g>

  <!-- ============================================================ -->
  <!-- PROJECT 1: QUANTUM COUNCIL (FLAGSHIP PROMINENT CARD)         -->
  <!-- ============================================================ -->
  <g transform="translate(24, 55)">
    <!-- Flagship Outer Aura & Card -->
    <rect width="{width-48}" height="195" rx="8" fill="url(#quantumGrad)" stroke="url(#borderQuantum)" stroke-width="1.8" />
    
    <!-- Top Cyber Decal -->
    <rect x="0" y="0" width="170" height="20" rx="4" fill="#00FF66" fill-opacity="0.15" />
    <text x="14" y="14" font-family="JetBrains Mono, Consolas, monospace" font-size="9" font-weight="900" fill="#55FF99" letter-spacing="1.5">FLAGSHIP ARCHITECTURE</text>

    <!-- Status Badge -->
    <g transform="translate({width-230}, 16)">
      <rect width="170" height="22" rx="4" fill="#141c16" stroke="#00FF66" stroke-opacity="0.4" stroke-width="1" />
      <circle cx="12" cy="11" r="3.5" fill="#00FF66" class="pulse-node" />
      <text x="24" y="15" font-family="JetBrains Mono, Consolas, monospace" font-size="8.5" fill="#a7f3d0" font-weight="600">STATUS: IN ACTIVE DEV</text>
    </g>

    <!-- Left Content Column -->
    <g transform="translate(24, 45)">
      <text x="0" y="0" class="p-title" font-size="20" filter="url(#neonAura)">01 // QUANTUM COUNCIL</text>
      <text x="0" y="20" class="p-tagline" font-size="12">Tagline: "Five Minds. One Intelligence."</text>
      <text x="0" y="38" font-family="JetBrains Mono, Consolas, monospace" font-size="9.5" fill="#55FF99" font-weight="600">Category: Multi-Agent Collaborative Intelligence</text>
      
      <text x="0" y="62" class="p-desc">A multi-agent AI system where five specialized AI agents collaborate through independent analysis,</text>
      <text x="0" y="78" class="p-desc">discussions, debate, and task coordination. A central orchestrator evaluates their contributions</text>
      <text x="0" y="94" class="p-desc">and produces a consolidated, highly reasoned consensus response.</text>
      
      <!-- Tech Pills -->
      <g transform="translate(0, 114)">
        <rect x="0" y="0" width="130" height="20" rx="3" fill="#081810" stroke="#00FF66" stroke-opacity="0.4" />
        <text x="8" y="13" class="tech-pill">Multi-Agent AI</text>

        <rect x="138" y="0" width="135" height="20" rx="3" fill="#081810" stroke="#00FF66" stroke-opacity="0.4" />
        <text x="8" y="13" class="tech-pill">LLM Orchestration</text>

        <rect x="281" y="0" width="125" height="20" rx="3" fill="#081810" stroke="#00FF66" stroke-opacity="0.4" />
        <text x="8" y="13" class="tech-pill">AI Debate Engine</text>

        <rect x="414" y="0" width="145" height="20" rx="3" fill="#081810" stroke="#00FF66" stroke-opacity="0.4" />
        <text x="8" y="13" class="tech-pill">Local + Cloud LLMs</text>
      </g>
    </g>

    <!-- Right Side: Five Minds Multi-Agent Node Visualizer -->
    <g transform="translate(685, 30)">
      <rect width="215" height="145" rx="6" fill="#030805" stroke="#00FF66" stroke-opacity="0.3" stroke-width="1" />
      <text x="12" y="18" font-family="JetBrains Mono, Consolas, monospace" font-size="8" fill="#7a9988">AGENT TOPOLOGY // 5 NODES</text>

      <!-- Central Orchestrator -->
      <circle cx="107" cy="80" r="16" fill="#082b18" stroke="#00FF66" stroke-width="1.8" />
      <text x="107" y="83" font-family="JetBrains Mono, Consolas, monospace" font-size="7.5" fill="#E6FFF2" font-weight="bold" text-anchor="middle">CORE</text>

      <!-- 5 Surrounding Specialized Agents -->
      <!-- Agent 1: Top -->
      <line x1="107" y1="64" x2="107" y2="40" stroke="#00FF66" stroke-dasharray="2,2" stroke-opacity="0.7" />
      <circle cx="107" cy="38" r="9" fill="#081d13" stroke="#00f5d4" stroke-width="1.2" class="pulse-node" />
      <text x="107" y="41" font-family="JetBrains Mono, Consolas, monospace" font-size="6" fill="#55FF99" text-anchor="middle">A1</text>

      <!-- Agent 2: Top Right -->
      <line x1="120" y1="72" x2="155" y2="52" stroke="#00FF66" stroke-dasharray="2,2" stroke-opacity="0.7" />
      <circle cx="157" cy="50" r="9" fill="#081d13" stroke="#00f5d4" stroke-width="1.2" class="pulse-node" />
      <text x="157" y="53" font-family="JetBrains Mono, Consolas, monospace" font-size="6" fill="#55FF99" text-anchor="middle">A2</text>

      <!-- Agent 3: Bottom Right -->
      <line x1="120" y1="88" x2="155" y2="108" stroke="#00FF66" stroke-dasharray="2,2" stroke-opacity="0.7" />
      <circle cx="157" cy="110" r="9" fill="#081d13" stroke="#00f5d4" stroke-width="1.2" class="pulse-node" />
      <text x="157" y="113" font-family="JetBrains Mono, Consolas, monospace" font-size="6" fill="#55FF99" text-anchor="middle">A3</text>

      <!-- Agent 4: Bottom Left -->
      <line x1="94" y1="88" x2="59" y2="108" stroke="#00FF66" stroke-dasharray="2,2" stroke-opacity="0.7" />
      <circle cx="57" cy="110" r="9" fill="#081d13" stroke="#00f5d4" stroke-width="1.2" class="pulse-node" />
      <text x="57" y="113" font-family="JetBrains Mono, Consolas, monospace" font-size="6" fill="#55FF99" text-anchor="middle">A4</text>

      <!-- Agent 5: Top Left -->
      <line x1="94" y1="72" x2="59" y2="52" stroke="#00FF66" stroke-dasharray="2,2" stroke-opacity="0.7" />
      <circle cx="57" cy="50" r="9" fill="#081d13" stroke="#00f5d4" stroke-width="1.2" class="pulse-node" />
      <text x="57" y="53" font-family="JetBrains Mono, Consolas, monospace" font-size="6" fill="#55FF99" text-anchor="middle">A5</text>
      
      <!-- Footer tag -->
      <text x="107" y="136" font-family="JetBrains Mono, Consolas, monospace" font-size="7" fill="#00FF66" text-anchor="middle">DEBATE &amp; CONSENSUS MATRIX</text>
    </g>
  </g>

  <!-- ============================================================ -->
  <!-- PROJECT 2: MNEMOSYNE AI (PERSISTENT MEMORY RAG)              -->
  <!-- ============================================================ -->
  <g transform="translate(24, 265)">
    <a href="https://github.com/kishanth-m/Mnemosyne-AI" target="_blank" class="btn-link">
      <rect width="298" height="385" rx="8" fill="url(#cardGrad)" stroke="#00FF66" stroke-opacity="0.35" stroke-width="1.2" />
      
      <g transform="translate(18, 28)">
        <text x="0" y="0" font-family="JetBrains Mono, Consolas, monospace" font-size="9" fill="#00f5d4" font-weight="700">PROJECT 02 // PERSISTENT MEMORY</text>
        <text x="0" y="22" class="p-title" font-size="14">Mnemosyne AI</text>
        <text x="0" y="38" font-family="JetBrains Mono, Consolas, monospace" font-size="9" fill="#55FF99">Long-Term Memory RAG Architecture</text>
        
        <line x1="0" y1="48" x2="262" y2="48" stroke="#00FF66" stroke-opacity="0.15" />
        
        <text x="0" y="68" class="p-desc">An AI memory architecture exploring</text>
        <text x="0" y="84" class="p-desc">persistent conversational state</text>
        <text x="0" y="100" class="p-desc">using PostgreSQL checkpointing,</text>
        <text x="0" y="116" class="p-desc">LangGraph agent memory, ChromaDB</text>
        <text x="0" y="132" class="p-desc">semantic recall &amp; Groq/Ollama LLMs.</text>
        
        <!-- Architectural diagram visual -->
        <g transform="translate(0, 150)">
          <rect width="262" height="70" rx="5" fill="#020503" stroke="#00FF66" stroke-opacity="0.2" />
          <text x="12" y="18" font-family="JetBrains Mono, Consolas, monospace" font-size="7.5" fill="#7a9988">DATA PIPELINE:</text>
          <text x="12" y="36" font-family="JetBrains Mono, Consolas, monospace" font-size="8" fill="#E6FFF2">User Prompt ➔ LangGraph State</text>
          <text x="12" y="52" font-family="JetBrains Mono, Consolas, monospace" font-size="8" fill="#55FF99">PostgreSQL Checkpoint + Chroma Recall</text>
        </g>

        <!-- Tech Stack -->
        <g transform="translate(0, 235)">
          <text x="0" y="0" font-family="JetBrains Mono, Consolas, monospace" font-size="8" fill="#7a9988">TECH STACK:</text>
          <rect x="0" y="8" width="62" height="18" rx="3" fill="#081810" stroke="#00FF66" stroke-opacity="0.3" />
          <text x="6" y="20" class="tech-pill">Python</text>

          <rect x="68" y="8" width="85" height="18" rx="3" fill="#081810" stroke="#00FF66" stroke-opacity="0.3" />
          <text x="6" y="20" class="tech-pill">LangGraph</text>

          <rect x="159" y="8" width="95" height="18" rx="3" fill="#081810" stroke="#00FF66" stroke-opacity="0.3" />
          <text x="6" y="20" class="tech-pill">PostgreSQL</text>

          <rect x="0" y="32" width="80" height="18" rx="3" fill="#081810" stroke="#00FF66" stroke-opacity="0.3" />
          <text x="6" y="44" class="tech-pill">ChromaDB</text>

          <rect x="86" y="32" width="70" height="18" rx="3" fill="#081810" stroke="#00FF66" stroke-opacity="0.3" />
          <text x="6" y="44" class="tech-pill">Groq API</text>

          <rect x="162" y="32" width="65" height="18" rx="3" fill="#081810" stroke="#00FF66" stroke-opacity="0.3" />
          <text x="6" y="44" class="tech-pill">Ollama</text>
        </g>

        <!-- Repo Link CTA -->
        <g transform="translate(0, 310)">
          <rect width="262" height="30" rx="4" fill="#0d2417" stroke="#00FF66" stroke-width="1.2" />
          <text x="131" y="19" font-family="JetBrains Mono, Consolas, monospace" font-size="9.5" font-weight="bold" fill="#00FF66" text-anchor="middle">⚡ VIEW ON GITHUB ➔</text>
        </g>
      </g>
    </a>
  </g>

  <!-- ============================================================ -->
  <!-- PROJECT 3: LOCAL PDF QUESTION ANSWERING SYSTEM               -->
  <!-- ============================================================ -->
  <g transform="translate(341, 265)">
    <a href="https://github.com/kishanth-m/Local-PDF-Question-Answering-System-RAG" target="_blank" class="btn-link">
      <rect width="298" height="385" rx="8" fill="url(#cardGrad)" stroke="#00FF66" stroke-opacity="0.35" stroke-width="1.2" />
      
      <g transform="translate(18, 28)">
        <text x="0" y="0" font-family="JetBrains Mono, Consolas, monospace" font-size="9" fill="#00f5d4" font-weight="700">PROJECT 03 // PRIVACY RAG</text>
        <text x="0" y="22" class="p-title" font-size="14">Local PDF QA System</text>
        <text x="0" y="38" font-family="JetBrains Mono, Consolas, monospace" font-size="9" fill="#55FF99">Zero-Leakage Document Intelligence</text>
        
        <line x1="0" y1="48" x2="262" y2="48" stroke="#00FF66" stroke-opacity="0.15" />
        
        <text x="0" y="68" class="p-desc">Privacy-oriented local document</text>
        <text x="0" y="84" class="p-desc">question-answering engine built</text>
        <text x="0" y="100" class="p-desc">entirely on local edge infrastructure.</text>
        <text x="0" y="116" class="p-desc">Zero cloud dependency, full privacy,</text>
        <text x="0" y="132" class="p-desc">and grounded Llama 3.2 synthesis.</text>
        
        <!-- Pipeline Visual -->
        <g transform="translate(0, 150)">
          <rect width="262" height="70" rx="5" fill="#020503" stroke="#00FF66" stroke-opacity="0.2" />
          <text x="12" y="18" font-family="JetBrains Mono, Consolas, monospace" font-size="7.5" fill="#7a9988">RAG PIPELINE FLOW:</text>
          <text x="12" y="36" font-family="JetBrains Mono, Consolas, monospace" font-size="8" fill="#E6FFF2">PDF Ingestion ➔ PyPDF Splitter</text>
          <text x="12" y="52" font-family="JetBrains Mono, Consolas, monospace" font-size="8" fill="#55FF99">Embeddings ➔ ChromaDB ➔ Llama 3.2</text>
        </g>

        <!-- Tech Stack -->
        <g transform="translate(0, 235)">
          <text x="0" y="0" font-family="JetBrains Mono, Consolas, monospace" font-size="8" fill="#7a9988">TECH STACK:</text>
          <rect x="0" y="8" width="62" height="18" rx="3" fill="#081810" stroke="#00FF66" stroke-opacity="0.3" />
          <text x="6" y="20" class="tech-pill">Python</text>

          <rect x="68" y="8" width="85" height="18" rx="3" fill="#081810" stroke="#00FF66" stroke-opacity="0.3" />
          <text x="6" y="20" class="tech-pill">LangChain</text>

          <rect x="159" y="8" width="95" height="18" rx="3" fill="#081810" stroke="#00FF66" stroke-opacity="0.3" />
          <text x="6" y="20" class="tech-pill">PyPDFLoader</text>

          <rect x="0" y="32" width="95" height="18" rx="3" fill="#081810" stroke="#00FF66" stroke-opacity="0.3" />
          <text x="6" y="44" class="tech-pill">Hugging Face</text>

          <rect x="101" y="32" width="75" height="18" rx="3" fill="#081810" stroke="#00FF66" stroke-opacity="0.3" />
          <text x="6" y="44" class="tech-pill">ChromaDB</text>

          <rect x="182" y="32" width="75" height="18" rx="3" fill="#081810" stroke="#00FF66" stroke-opacity="0.3" />
          <text x="6" y="44" class="tech-pill">Llama 3.2</text>
        </g>

        <!-- Repo Link CTA -->
        <g transform="translate(0, 310)">
          <rect width="262" height="30" rx="4" fill="#0d2417" stroke="#00FF66" stroke-width="1.2" />
          <text x="131" y="19" font-family="JetBrains Mono, Consolas, monospace" font-size="9.5" font-weight="bold" fill="#00FF66" text-anchor="middle">⚡ VIEW ON GITHUB ➔</text>
        </g>
      </g>
    </a>
  </g>

  <!-- ============================================================ -->
  <!-- PROJECT 4: AI-BASED PPE SAFETY MONITORING                    -->
  <!-- ============================================================ -->
  <g transform="translate(658, 265)">
    <a href="https://github.com/kishanth-m/PPE-Safety-Monitor" target="_blank" class="btn-link">
      <rect width="298" height="385" rx="8" fill="url(#cardGrad)" stroke="#00FF66" stroke-opacity="0.35" stroke-width="1.2" />
      
      <g transform="translate(18, 28)">
        <text x="0" y="0" font-family="JetBrains Mono, Consolas, monospace" font-size="9" fill="#00f5d4" font-weight="700">PROJECT 04 // COMPUTER VISION</text>
        <text x="0" y="22" class="p-title" font-size="14">PPE Safety Monitor</text>
        <text x="0" y="38" font-family="JetBrains Mono, Consolas, monospace" font-size="9" fill="#55FF99">Workplace Safety &amp; Pose Analysis</text>
        
        <line x1="0" y1="48" x2="262" y2="48" stroke="#00FF66" stroke-opacity="0.15" />
        
        <text x="0" y="68" class="p-desc">Industrial workplace safety vision</text>
        <text x="0" y="84" class="p-desc">system combining object detection</text>
        <text x="0" y="100" class="p-desc">and human pose estimation to monitor</text>
        <text x="0" y="116" class="p-desc">PPE compliance in real time and</text>
        <text x="0" y="132" class="p-desc">capture automated violation logs.</text>
        
        <!-- Detection Feature Visual -->
        <g transform="translate(0, 150)">
          <rect width="262" height="70" rx="5" fill="#020503" stroke="#00FF66" stroke-opacity="0.2" />
          <text x="12" y="18" font-family="JetBrains Mono, Consolas, monospace" font-size="7.5" fill="#7a9988">ACTIVE DETECTORS:</text>
          <text x="12" y="36" font-family="JetBrains Mono, Consolas, monospace" font-size="8" fill="#E6FFF2">🪖 Helmet • 😷 Mask • 🧤 Gloves</text>
          <text x="12" y="52" font-family="JetBrains Mono, Consolas, monospace" font-size="8" fill="#55FF99">🥾 Safety Shoes • 📐 Pose Estimation</text>
        </g>

        <!-- Tech Stack -->
        <g transform="translate(0, 235)">
          <text x="0" y="0" font-family="JetBrains Mono, Consolas, monospace" font-size="8" fill="#7a9988">TECH STACK:</text>
          <rect x="0" y="8" width="62" height="18" rx="3" fill="#081810" stroke="#00FF66" stroke-opacity="0.3" />
          <text x="6" y="20" class="tech-pill">Python</text>

          <rect x="68" y="8" width="75" height="18" rx="3" fill="#081810" stroke="#00FF66" stroke-opacity="0.3" />
          <text x="6" y="20" class="tech-pill">YOLOv8</text>

          <rect x="149" y="8" width="75" height="18" rx="3" fill="#081810" stroke="#00FF66" stroke-opacity="0.3" />
          <text x="6" y="20" class="tech-pill">OpenCV</text>

          <rect x="0" y="32" width="125" height="18" rx="3" fill="#081810" stroke="#00FF66" stroke-opacity="0.3" />
          <text x="6" y="44" class="tech-pill">Computer Vision</text>

          <rect x="131" y="32" width="120" height="18" rx="3" fill="#081810" stroke="#00FF66" stroke-opacity="0.3" />
          <text x="6" y="44" class="tech-pill">Evidence Capture</text>
        </g>

        <!-- Repo Link CTA -->
        <g transform="translate(0, 310)">
          <rect width="262" height="30" rx="4" fill="#0d2417" stroke="#00FF66" stroke-width="1.2" />
          <text x="131" y="19" font-family="JetBrains Mono, Consolas, monospace" font-size="9.5" font-weight="bold" fill="#00FF66" text-anchor="middle">⚡ VIEW ON GITHUB ➔</text>
        </g>
      </g>
    </a>
  </g>

</svg>'''

    path = os.path.join(ASSETS_DIR, "projects.svg")
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {path}")

# -------------------------------------------------------------
# 4. CURRENT FOCUS / ROADMAP SVG
# -------------------------------------------------------------
def build_current_focus_svg():
    width = 980
    height = 250
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto">
  <defs>
    <linearGradient id="focusBorder" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00FF66" stop-opacity="0.7" />
      <stop offset="50%" stop-color="#00f5d4" stop-opacity="0.7" />
      <stop offset="100%" stop-color="#00FF66" stop-opacity="0.7" />
    </linearGradient>
    <style>
      @keyframes pulseFocus {{
        0%, 100% {{ opacity: 0.4; r: 4; }}
        50% {{ opacity: 1; r: 5.5; filter: drop-shadow(0 0 5px #00FF66); }}
      }}
      .p-focus {{ animation: pulseFocus 2s infinite ease-in-out; }}
    </style>
  </defs>

  <rect width="{width}" height="{height}" rx="10" fill="#060b08" />
  <rect x="1.5" y="1.5" width="{width-3}" height="{height-3}" rx="9" fill="none" stroke="url(#focusBorder)" stroke-width="1.2" />

  <!-- Header -->
  <g transform="translate(24, 28)">
    <text x="0" y="0" font-family="JetBrains Mono, Consolas, monospace" font-size="13" font-weight="900" fill="#00FF66" letter-spacing="2">🗺️ CURRENT FOCUS // AI ENGINEERING ROADMAP</text>
    <text x="{width-48}" y="0" font-family="JetBrains Mono, Consolas, monospace" font-size="9" fill="#7a9988" text-anchor="end">CONTINUOUS LEARNING &amp; APPLIED RESEARCH</text>
    <line x1="0" y1="12" x2="{width-48}" y2="12" stroke="#00FF66" stroke-opacity="0.25" stroke-width="1" />
  </g>

  <!-- 5 Roadmap Nodes -->
  <g transform="translate(24, 60)">
    
    <!-- Step 1 -->
    <g transform="translate(0, 0)">
      <rect width="175" height="150" rx="6" fill="#0a1610" stroke="#00FF66" stroke-opacity="0.4" />
      <circle cx="18" cy="22" r="4" fill="#00FF66" class="p-focus" />
      <text x="30" y="25" font-family="JetBrains Mono, Consolas, monospace" font-size="8.5" fill="#55FF99" font-weight="bold">PHASE 01 // CORE</text>
      <text x="14" y="52" font-family="JetBrains Mono, Consolas, monospace" font-size="12" font-weight="bold" fill="#00f5d4">Generative AI &amp; LLMs</text>
      <text x="14" y="74" font-family="JetBrains Mono, Consolas, monospace" font-size="9" fill="#a7f3d0">Deep dive into</text>
      <text x="14" y="88" font-family="JetBrains Mono, Consolas, monospace" font-size="9" fill="#a7f3d0">foundation models,</text>
      <text x="14" y="102" font-family="JetBrains Mono, Consolas, monospace" font-size="9" fill="#a7f3d0">prompting &amp; tokens.</text>
      <text x="14" y="132" font-family="JetBrains Mono, Consolas, monospace" font-size="8" fill="#00FF66">● ACTIVE BASELINE</text>
    </g>

    <!-- Step 2 -->
    <g transform="translate(188, 0)">
      <rect width="175" height="150" rx="6" fill="#0a1610" stroke="#00FF66" stroke-opacity="0.4" />
      <circle cx="18" cy="22" r="4" fill="#00FF66" class="p-focus" />
      <text x="30" y="25" font-family="JetBrains Mono, Consolas, monospace" font-size="8.5" fill="#55FF99" font-weight="bold">PHASE 02 // AGENTS</text>
      <text x="14" y="52" font-family="JetBrains Mono, Consolas, monospace" font-size="12" font-weight="bold" fill="#00f5d4">Multi-Agent Systems</text>
      <text x="14" y="74" font-family="JetBrains Mono, Consolas, monospace" font-size="9" fill="#a7f3d0">LangGraph stateful</text>
      <text x="14" y="88" font-family="JetBrains Mono, Consolas, monospace" font-size="9" fill="#a7f3d0">graphs, orchestrator</text>
      <text x="14" y="102" font-family="JetBrains Mono, Consolas, monospace" font-size="9" fill="#a7f3d0">&amp; debate topologies.</text>
      <text x="14" y="132" font-family="JetBrains Mono, Consolas, monospace" font-size="8" fill="#00FF66">● IN PROGRESS</text>
    </g>

    <!-- Step 3 -->
    <g transform="translate(376, 0)">
      <rect width="175" height="150" rx="6" fill="#0a1610" stroke="#00FF66" stroke-opacity="0.4" />
      <circle cx="18" cy="22" r="4" fill="#00FF66" class="p-focus" />
      <text x="30" y="25" font-family="JetBrains Mono, Consolas, monospace" font-size="8.5" fill="#55FF99" font-weight="bold">PHASE 03 // RETRIEVAL</text>
      <text x="14" y="52" font-family="JetBrains Mono, Consolas, monospace" font-size="12" font-weight="bold" fill="#00f5d4">Advanced RAG</text>
      <text x="14" y="74" font-family="JetBrains Mono, Consolas, monospace" font-size="9" fill="#a7f3d0">Hybrid search,</text>
      <text x="14" y="88" font-family="JetBrains Mono, Consolas, monospace" font-size="9" fill="#a7f3d0">vector reranking,</text>
      <text x="14" y="102" font-family="JetBrains Mono, Consolas, monospace" font-size="9" fill="#a7f3d0">&amp; PostgreSQL recall.</text>
      <text x="14" y="132" font-family="JetBrains Mono, Consolas, monospace" font-size="8" fill="#00FF66">● ACTIVE PIPELINE</text>
    </g>

    <!-- Step 4 -->
    <g transform="translate(564, 0)">
      <rect width="175" height="150" rx="6" fill="#0a1610" stroke="#00FF66" stroke-opacity="0.4" />
      <circle cx="18" cy="22" r="4" fill="#00FF66" class="p-focus" />
      <text x="30" y="25" font-family="JetBrains Mono, Consolas, monospace" font-size="8.5" fill="#55FF99" font-weight="bold">PHASE 04 // LOCAL AI</text>
      <text x="14" y="52" font-family="JetBrains Mono, Consolas, monospace" font-size="12" font-weight="bold" fill="#00f5d4">Edge &amp; Local LLMs</text>
      <text x="14" y="74" font-family="JetBrains Mono, Consolas, monospace" font-size="9" fill="#a7f3d0">Privacy-first inference</text>
      <text x="14" y="88" font-family="JetBrains Mono, Consolas, monospace" font-size="9" fill="#a7f3d0">with Ollama, Groq</text>
      <text x="14" y="102" font-family="JetBrains Mono, Consolas, monospace" font-size="9" fill="#a7f3d0">&amp; quantized models.</text>
      <text x="14" y="132" font-family="JetBrains Mono, Consolas, monospace" font-size="8" fill="#00FF66">● DEPLOYING</text>
    </g>

    <!-- Step 5 -->
    <g transform="translate(752, 0)">
      <rect width="175" height="150" rx="6" fill="#0a1610" stroke="#00FF66" stroke-opacity="0.4" />
      <circle cx="18" cy="22" r="4" fill="#00FF66" class="p-focus" />
      <text x="30" y="25" font-family="JetBrains Mono, Consolas, monospace" font-size="8.5" fill="#55FF99" font-weight="bold">PHASE 05 // VISION</text>
      <text x="14" y="52" font-family="JetBrains Mono, Consolas, monospace" font-size="12" font-weight="bold" fill="#00f5d4">Computer Vision</text>
      <text x="14" y="74" font-family="JetBrains Mono, Consolas, monospace" font-size="9" fill="#a7f3d0">Object detection,</text>
      <text x="14" y="88" font-family="JetBrains Mono, Consolas, monospace" font-size="9" fill="#a7f3d0">pose estimation,</text>
      <text x="14" y="102" font-family="JetBrains Mono, Consolas, monospace" font-size="9" fill="#a7f3d0">&amp; spatial analytics.</text>
      <text x="14" y="132" font-family="JetBrains Mono, Consolas, monospace" font-size="8" fill="#00FF66">● EXPANDING</text>
    </g>

  </g>
</svg>'''

    path = os.path.join(ASSETS_DIR, "current-focus.svg")
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {path}")

# -------------------------------------------------------------
# 5. CONNECT WITH ME SVG
# -------------------------------------------------------------
def build_connect_svg():
    width = 980
    height = 140
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto">
  <defs>
    <linearGradient id="connBorder" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00FF66" stop-opacity="0.8" />
      <stop offset="50%" stop-color="#00f5d4" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#00FF66" stop-opacity="0.8" />
    </linearGradient>
    <style>
      .c-btn:hover {{ filter: brightness(1.25); }}
    </style>
  </defs>

  <rect width="{width}" height="{height}" rx="10" fill="#060b08" />
  <rect x="1.5" y="1.5" width="{width-3}" height="{height-3}" rx="9" fill="none" stroke="url(#connBorder)" stroke-width="1.2" />

  <g transform="translate(30, 35)">
    <text x="0" y="0" font-family="JetBrains Mono, Consolas, monospace" font-size="14" font-weight="900" fill="#00FF66" letter-spacing="2">🌐 CONNECT WITH ME // NEURAL HANDSHAKE</text>
    <text x="0" y="24" font-family="JetBrains Mono, Consolas, monospace" font-size="10.5" fill="#a7f3d0">Open to collaborations, AI engineering discussions, and intelligent system research.</text>
  </g>

  <!-- Buttons on right side -->
  <g transform="translate(560, 42)">
    <!-- GitHub Button -->
    <a href="https://github.com/kishanth-m" target="_blank" class="c-btn">
      <rect x="0" y="0" width="185" height="50" rx="6" fill="#0b1e14" stroke="#00FF66" stroke-width="1.5" />
      <text x="24" y="31" font-family="JetBrains Mono, Consolas, monospace" font-size="13" font-weight="bold" fill="#00FF66">⚡ GITHUB PROFILE</text>
    </a>

    <!-- LinkedIn Button -->
    <a href="https://www.linkedin.com/in/kishanth-m-aa055b2a3/" target="_blank" class="c-btn">
      <rect x="205" y="0" width="185" height="50" rx="6" fill="#071a22" stroke="#00f5d4" stroke-width="1.5" />
      <text x="229" y="31" font-family="JetBrains Mono, Consolas, monospace" font-size="13" font-weight="bold" fill="#00f5d4">💼 LINKEDIN</text>
    </a>
  </g>
</svg>'''

    path = os.path.join(ASSETS_DIR, "connect.svg")
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {path}")

# -------------------------------------------------------------
# 6. FOOTER ANIMATED DEVELOPER SIGNATURE SVG
# -------------------------------------------------------------
def build_footer_svg():
    width = 980
    height = 160
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto">
  <defs>
    <filter id="sigGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
    <linearGradient id="sigLine" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00FF66" stop-opacity="0" />
      <stop offset="30%" stop-color="#00FF66" stop-opacity="0.8" />
      <stop offset="50%" stop-color="#00f5d4" stop-opacity="1" />
      <stop offset="70%" stop-color="#00FF66" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#00FF66" stop-opacity="0" />
    </linearGradient>
    <style>
      @keyframes floatSignature {{
        0%, 100% {{ transform: translateY(0); }}
        50% {{ transform: translateY(-3px); }}
      }}
      @keyframes pulseSig {{
        0%, 100% {{ opacity: 0.6; }}
        50% {{ opacity: 1; filter: drop-shadow(0 0 6px #00FF66); }}
      }}
      .signature-text {{
        animation: floatSignature 4s ease-in-out infinite;
      }}
      .pulse-sig {{
        animation: pulseSig 3s infinite;
      }}
    </style>
  </defs>

  <rect width="{width}" height="{height}" rx="10" fill="#040705" />
  
  <!-- Subtle Matrix Digital Rain Stream in Footer -->
  <g opacity="0.18" font-family="JetBrains Mono, Consolas, monospace" font-size="7.5" fill="#00FF66">
    <text x="50" y="25">010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101</text>
    <text x="30" y="145">KISHANTH.M//NEURAL_SYSTEM//RAG_AGENT_ARCHITECTURE//CONTINUOUS_LEARNING//01001011 01001101//MATRIX_PORTRAIT_VERIFIED</text>
  </g>

  <!-- Accent Divider Line -->
  <line x1="40" y1="35" x2="{width-40}" y2="35" stroke="url(#sigLine)" stroke-width="1.5" />

  <!-- The Three Core Mantras -->
  <g class="signature-text" transform="translate({width/2}, 78)" text-anchor="middle" font-family="JetBrains Mono, Consolas, Monaco, monospace">
    <text x="0" y="0" font-size="16" font-weight="900" fill="#00FF66" letter-spacing="4" filter="url(#sigGlow)">
      DESIGNED TO THINK.  •  BUILT TO BUILD.  •  ALWAYS LEARNING.
    </text>
  </g>

  <!-- Terminal Status Line -->
  <g transform="translate({width/2}, 112)" text-anchor="middle" font-family="JetBrains Mono, Consolas, monospace" font-size="9" fill="#7a9988">
    <text x="0" y="0">
      CRAFTED BY <tspan fill="#55FF99" font-weight="bold">KISHANTH M.</tspan> // POWERED BY MATRIX ASCII ENGINE // HOSTED ON GITHUB
    </text>
  </g>

  <!-- Bottom Pulse Line -->
  <line x1="120" y1="130" x2="{width-120}" y2="130" stroke="url(#sigLine)" stroke-width="1" stroke-dasharray="8,6" />
</svg>'''

    path = os.path.join(ASSETS_DIR, "footer.svg")
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {path}")

if __name__ == "__main__":
    print("Generating auxiliary SVGs...")
    build_terminal_svg()
    build_tech_universe_svg()
    build_projects_svg()
    build_current_focus_svg()
    build_connect_svg()
    build_footer_svg()
    print("All auxiliary SVGs successfully generated!")

