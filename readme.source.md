```aura width=860 height=210
<div style={{
  width: '100%', height: '100%', background: '#08080c',
  display: 'flex', alignItems: 'center', fontFamily: 'Inter, sans-serif',
  position: 'relative', overflow: 'hidden', borderRadius: 16,
  border: '1px solid rgba(16,185,129,0.22)'
}}>

  <style>
    {`
      @keyframes orb-slow {
        0%, 100% { transform: translateX(0px); opacity: 0.8; }
        50% { transform: translateX(320px); opacity: 1.1; }
      }
      @keyframes orb-medium {
        0%, 100% { transform: translateX(0px); opacity: 0.7; }
        50% { transform: translateX(-240px); opacity: 1.0; }
      }
      @keyframes orb-fast {
        0%, 100% { transform: translateX(0px); opacity: 0.85; }
        50% { transform: translateX(180px); opacity: 0.6; }
      }
      @keyframes orb-diagonal {
        0%, 100% { transform: translate(0px, 0px); opacity: 0.75; }
        50% { transform: translate(140px, -20px); opacity: 1.0; }
      }
      @keyframes orb-pulse {
        0%, 100% { transform: scale(1); opacity: 0.8; }
        50% { transform: scale(1.25); opacity: 0.45; }
      }
      #orb-1 { animation: orb-slow 9s ease-in-out infinite; }
      #orb-2 { animation: orb-medium 13s ease-in-out infinite; }
      #orb-3 { animation: orb-fast 8s ease-in-out infinite; }
      #orb-4 { animation: orb-diagonal 11s ease-in-out infinite reverse; }
      #orb-5 { animation: orb-pulse 7s ease-in-out infinite; }
    `}
  </style>

  <svg width="860" height="210" style={{ position: 'absolute', top: 0, left: 0 }}>
    <defs>
      <radialGradient id="rg1" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(16,185,129,0.55)" />
        <stop offset="45%" stopColor="rgba(5,150,105,0.25)" />
        <stop offset="70%" stopColor="rgba(5,150,105,0)" />
      </radialGradient>
      <radialGradient id="rg2" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(6,182,212,0.48)" />
        <stop offset="45%" stopColor="rgba(8,145,178,0.22)" />
        <stop offset="70%" stopColor="rgba(8,145,178,0)" />
      </radialGradient>
      <radialGradient id="rg3" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(59,130,246,0.38)" />
        <stop offset="50%" stopColor="rgba(37,99,235,0.16)" />
        <stop offset="70%" stopColor="rgba(37,99,235,0)" />
      </radialGradient>
      <radialGradient id="rg4" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(99,102,241,0.35)" />
        <stop offset="70%" stopColor="rgba(99,102,241,0)" />
      </radialGradient>
      <radialGradient id="rg5" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="rgba(16,185,129,0.42)" />
        <stop offset="70%" stopColor="rgba(16,185,129,0)" />
      </radialGradient>
    </defs>

    <ellipse id="orb-1" cx="160" cy="230" rx="260" ry="170" fill="url(#rg1)" />
    <ellipse id="orb-2" cx="340" cy="240" rx="220" ry="150" fill="url(#rg2)" />
    <ellipse id="orb-3" cx="520" cy="240" rx="190" ry="130" fill="url(#rg3)" />
    <ellipse id="orb-4" cx="700" cy="230" rx="160" ry="120" fill="url(#rg4)" />
    <ellipse id="orb-5" cx="420" cy="250" rx="180" ry="130" fill="url(#rg5)" />
  </svg>

  <div style={{
    position: 'absolute', left: 44, top: 55, width: 96, height: 96,
    borderRadius: 48, background: 'linear-gradient(135deg, #10b981, #06b6d4)',
    display: 'flex', alignItems: 'center', justifyContent: 'center',
  }}>
    <div style={{
      width: 88, height: 88, borderRadius: 44, background: '#0a0d10',
      display: 'flex', alignItems: 'center', justifyContent: 'center'
    }}>
      <svg width="48" height="48" viewBox="0 0 48 48">
        <circle cx="24" cy="12" r="4.5" fill="#10b981" />
        <circle cx="12" cy="34" r="4" fill="#06b6d4" />
        <circle cx="36" cy="34" r="4" fill="#3b82f6" />
        <circle cx="24" cy="24" r="5.5" fill="#ffffff" />
        <line x1="24" y1="12" x2="24" y2="24" stroke="#10b981" strokeWidth="2" strokeOpacity="0.8" />
        <line x1="12" y1="34" x2="24" y2="24" stroke="#06b6d4" strokeWidth="2" strokeOpacity="0.8" />
        <line x1="36" y1="34" x2="24" y2="24" stroke="#3b82f6" strokeWidth="2" strokeOpacity="0.8" />
        <line x1="12" y1="34" x2="36" y2="34" stroke="rgba(255,255,255,0.2)" strokeWidth="1.5" strokeDasharray="3,3" />
      </svg>
    </div>
  </div>

  <div style={{ display: 'flex', flexDirection: 'column', marginLeft: 168, gap: 7, paddingRight: 40 }}>
    <div style={{ display: 'flex', fontSize: 34, fontWeight: 800, color: '#ffffff', letterSpacing: '-0.8px', lineHeight: 1 }}>
      Kishanth M.
    </div>
    <div style={{ display: 'flex', fontSize: 13.5, color: 'rgba(167,243,208,0.9)', fontWeight: 500, letterSpacing: '0.2px' }}>
      Aspiring AI Engineer · B.Tech Artificial Intelligence &amp; Data Science
    </div>
    <div style={{ display: 'flex', fontSize: 11.5, color: 'rgba(203,213,225,0.78)', fontWeight: 400, lineHeight: 1.45, maxWidth: 640 }}>
      Artificial Intelligence and Data Science student building practical AI applications with LLMs, RAG pipelines, multi-agent systems, and computer vision.
    </div>
    <div style={{ display: 'flex', gap: 7, marginTop: 4 }}>
      {['Multi-Agent Systems', 'RAG Architecture', 'Local LLMs', 'Computer Vision'].map(function(tag) {
        return (
          <div key={tag} style={{
            display: 'flex', padding: '3px 11px', borderRadius: 14,
            background: 'rgba(16,185,129,0.12)', border: '1px solid rgba(16,185,129,0.28)',
            color: 'rgba(209,250,229,0.9)', fontSize: 11, fontWeight: 600,
          }}>{tag}</div>
        );
      })}
    </div>
  </div>
</div>
```

```aura width=860 height=220
(function() {
  var categories = [
    { title: 'Languages', color: '#10b981', items: ['Python', 'Java', 'C', 'SQL'] },
    { title: 'GenAI & LLMs', color: '#06b6d4', items: ['LLMs', 'RAG', 'Prompt Engineering', 'Embeddings', 'Semantic Search'] },
    { title: 'Frameworks', color: '#3b82f6', items: ['LangChain', 'LangGraph', 'Ollama', 'Groq API', 'Hugging Face'] },
    { title: 'Data & Vision', color: '#a855f7', items: ['PostgreSQL', 'ChromaDB', 'OpenCV', 'YOLOv8', 'Pandas', 'NumPy'] },
    { title: 'Workspace', color: '#94a3b8', items: ['Git & GitHub', 'VS Code', 'Postman', 'REST APIs', 'HTML / CSS'] },
  ];

  return (
    <div style={{
      width: '100%', height: '100%',
      background: '#08080c',
      display: 'flex', flexDirection: 'column',
      justifyContent: 'center',
      padding: '24px 38px',
      fontFamily: 'Inter, sans-serif', borderRadius: 16,
      border: '1px solid rgba(16,185,129,0.18)',
      position: 'relative', overflow: 'hidden', gap: 12,
    }}>

      <style>
        {`
          @keyframes glow-shift {
            0%, 100% { transform: translateX(0px); opacity: 0.65; }
            50% { transform: translateX(200px); opacity: 0.95; }
          }
          #stk-glow-1 { animation: glow-shift 10s ease-in-out infinite; }
          #stk-glow-2 { animation: glow-shift 14s ease-in-out infinite reverse; }
        `}
      </style>

      <svg width="860" height="220" style={{ position: 'absolute', top: 0, left: 0 }}>
        <defs>
          <radialGradient id="sg1" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stopColor="rgba(16,185,129,0.32)" />
            <stop offset="70%" stopColor="rgba(16,185,129,0)" />
          </radialGradient>
          <radialGradient id="sg2" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stopColor="rgba(6,182,212,0.28)" />
            <stop offset="70%" stopColor="rgba(6,182,212,0)" />
          </radialGradient>
        </defs>
        <ellipse id="stk-glow-1" cx="240" cy="190" rx="260" ry="140" fill="url(#sg1)" />
        <ellipse id="stk-glow-2" cx="620" cy="190" rx="220" ry="130" fill="url(#sg2)" />
      </svg>

      <div style={{ display: 'flex', fontSize: 10, fontWeight: 700, color: 'rgba(52,211,153,0.7)', letterSpacing: '3px' }}>
        TECHNICAL FOCUS &amp; VERIFIED STACK
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: 9 }}>
        {categories.map(function(cat) {
          return (
            <div key={cat.title} style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
              <div style={{ display: 'flex', fontSize: 10, fontWeight: 700, color: cat.color, letterSpacing: '1px', width: 110 }}>
                {cat.title.toUpperCase()}
              </div>
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: 6 }}>
                {cat.items.map(function(item) {
                  return (
                    <div key={item} style={{
                      display: 'flex', padding: '3px 10px', borderRadius: 6,
                      background: cat.color + '14', border: '1px solid ' + cat.color + '32',
                      color: 'rgba(241,245,249,0.88)', fontSize: 11, fontWeight: 600,
                    }}>{item}</div>
                  );
                })}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
})()
```

```aura width=860 height=395
(function() {
  var projects = [
    {
      title: 'Quantum Council',
      badge: 'IN DEVELOPMENT',
      badgeColor: '#10b981',
      tagline: 'Multi-Agent Collaborative Intelligence',
      desc: 'Collaborative AI architecture where five specialized agents debate, research, and coordinate under a central orchestrator.',
      tags: ['Multi-Agent AI', 'LLM Orchestration', 'Debate Engine', 'Local/Cloud'],
      link: 'https://github.com/kishanth-m'
    },
    {
      title: 'Mnemosyne AI',
      badge: 'PERSISTENT MEMORY',
      badgeColor: '#06b6d4',
      tagline: 'AI-Powered Persistent Memory RAG System',
      desc: 'Long-term conversational memory using PostgreSQL state checkpointing, LangGraph cyclic workflows, and ChromaDB semantic recall.',
      tags: ['LangGraph', 'PostgreSQL', 'ChromaDB', 'Groq API', 'Ollama'],
      link: 'https://github.com/kishanth-m/Mnemosyne-AI'
    },
    {
      title: 'Local PDF QA System',
      badge: 'PRIVACY RAG',
      badgeColor: '#3b82f6',
      tagline: 'Zero-Cloud Document Intelligence',
      desc: 'Privacy-oriented document QA extracting text, generating embeddings, and synthesizing answers with Llama 3.2 via Ollama.',
      tags: ['Python', 'LangChain', 'PyPDFLoader', 'ChromaDB', 'Llama 3.2'],
      link: 'https://github.com/kishanth-m/Local-PDF-Question-Answering-System-RAG'
    },
    {
      title: 'PPE Safety Monitor',
      badge: 'COMPUTER VISION',
      badgeColor: '#a855f7',
      tagline: 'Industrial Safety & Pose Compliance',
      desc: 'Computer vision monitoring system combining YOLOv8 detection (helmet, mask, gloves, shoes) and pose estimation for workplace safety.',
      tags: ['Python', 'YOLOv8', 'OpenCV', 'Pose Estimation', 'Violation Capture'],
      link: 'https://github.com/kishanth-m/PPE-Safety-Monitor'
    }
  ];

  return (
    <div style={{
      width: '100%', height: '100%',
      background: '#08080c',
      display: 'flex', flexDirection: 'column',
      padding: '24px 34px',
      fontFamily: 'Inter, sans-serif', borderRadius: 16,
      border: '1px solid rgba(16,185,129,0.18)',
      position: 'relative', overflow: 'hidden',
    }}>

      <style>
        {`
          @keyframes prj-glow {
            0%, 100% { transform: translateX(0px); opacity: 0.6; }
            50% { transform: translateX(260px); opacity: 0.9; }
          }
          #pg-1 { animation: prj-glow 11s ease-in-out infinite; }
          #pg-2 { animation: prj-glow 15s ease-in-out infinite reverse; }
        `}
      </style>

      <svg width="860" height="395" style={{ position: 'absolute', top: 0, left: 0 }}>
        <defs>
          <radialGradient id="pg1" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stopColor="rgba(16,185,129,0.30)" />
            <stop offset="70%" stopColor="rgba(16,185,129,0)" />
          </radialGradient>
          <radialGradient id="pg2" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stopColor="rgba(6,182,212,0.25)" />
            <stop offset="70%" stopColor="rgba(6,182,212,0)" />
          </radialGradient>
        </defs>
        <ellipse id="pg-1" cx="200" cy="330" rx="250" ry="160" fill="url(#pg1)" />
        <ellipse id="pg-2" cx="640" cy="340" rx="230" ry="150" fill="url(#pg2)" />
      </svg>

      <div style={{ display: 'flex', fontSize: 10, fontWeight: 700, color: 'rgba(52,211,153,0.7)', letterSpacing: '3px', marginBottom: 14 }}>
        FEATURED ARCHITECTURES // PROJECT SHOWCASE
      </div>

      <div style={{ display: 'flex', flexWrap: 'wrap', gap: 12 }}>
        {projects.map(function(p) {
          return (
            <div key={p.title} style={{
              display: 'flex', flexDirection: 'column',
              width: 390, padding: '16px 18px', borderRadius: 10,
              background: 'rgba(12,14,20,0.75)', border: '1px solid rgba(255,255,255,0.08)',
              gap: 6
            }}>
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                <div style={{ display: 'flex', fontSize: 15, fontWeight: 700, color: '#ffffff' }}>
                  {p.title}
                </div>
                <div style={{
                  display: 'flex', fontSize: 9, fontWeight: 700, color: p.badgeColor,
                  padding: '2px 7px', borderRadius: 4,
                  background: p.badgeColor + '18', border: '1px solid ' + p.badgeColor + '40',
                  letterSpacing: '0.5px'
                }}>
                  {p.badge}
                </div>
              </div>

              <div style={{ display: 'flex', fontSize: 11, fontWeight: 500, color: 'rgba(148,163,184,0.85)' }}>
                {p.tagline}
              </div>

              <div style={{ display: 'flex', fontSize: 10.5, color: 'rgba(203,213,225,0.72)', lineHeight: 1.4, marginTop: 2, height: 42 }}>
                {p.desc}
              </div>

              <div style={{ display: 'flex', flexWrap: 'wrap', gap: 5, marginTop: 6 }}>
                {p.tags.slice(0, 4).map(function(tag) {
                  return (
                    <div key={tag} style={{
                      display: 'flex', padding: '2px 7px', borderRadius: 4,
                      background: 'rgba(255,255,255,0.04)', border: '1px solid rgba(255,255,255,0.09)',
                      color: 'rgba(226,232,240,0.75)', fontSize: 9.5, fontWeight: 500
                    }}>{tag}</div>
                  );
                })}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
})()
```

```aura width=130 height=44 link="https://github.com/kishanth-m" inline align=center
<SocialMediaButton
  icon="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjI0IiBoZWlnaHQ9IjI0IiBmaWxsPSIjZmZmZmZmIj4KICA8cGF0aCBkPSJNMTIgMEM1LjM3IDAgMCA1LjM3IDAgMTJjMCA1LjMxIDMuNDM1IDkuNzk1IDguMjA1IDExLjM4NS42LjEwNS44MjUtLjI1NS44MjUtLjU3IDAtLjI4NS0uMDE1LTEuMjMtLjAxNS0yLjIzNS0zLjAxNS41NTUtMy43OTUtLjczNS00LjAzNS0xLjQxLS4xMzUtLjM0NS0uNzItMS40MS0xLjIzLTEuNjk1LS40Mi0uMjI1LTEuMDItLjc4LS4wMTUtLjc5NS45NDUtLjAxNSAxLjYyLjg3IDEuODQ1IDEuMjMgMS4wOCAxLjgxNSAyLjgwNSAxLjMwNSAzLjQ5NS45OS4xMDUtLjc4LjQyLTEuMzA1Ljc2NS0xLjYwNS0yLjY3LS4zLTUuNDYtMS4zMzUtNS40Ni01LjkyNSAwLTEuMzA1LjQ2NS0yLjM4NSAxLjIzLTMuMjI1LS4xMi0uMy0uNTQtMS41My4xMi0zLjE4IDAgMCAxLjAwNS0uMzE1IDMuMyAxLjIzLjk2LS4yNyAxLjk4LS40MDUgMy0uNDA1czIuMDQuMTM1IDMgLjQwNWMyLjI5NS0xLjU2IDMuMy0xLjIzIDMuMy0xLjIzLjY2IDEuNjUuMjQgMi44OC4xMiAzLjE4Ljc2NS44NCAxLjIzIDEuOTA1IDEuMjMgMy4yMjUgMCA0LjYwNS0yLjgwNSA1LjYyNS01LjQ3NSA1LjkyNS40MzUuMzc1LjgxIDEuMDk1LjgxIDIuMjIgMCAxLjYwNS0uMDE1IDIuODk1LS4wMTUgMy4zIDAgLjMxNS4yMjUuNjkuODI1LjU3QTEyLjAyIDEyLjAyIDAgMDAyNCAxMmMwLTYuNjMtNS4zNy0xMi0xMi0xMnoiLz4KPC9zdmc+"
  text="GitHub"
  backgroundColor="#08080c"
  textColor="#ffffff"
  width={130}
  height={44}
  gradientStops={[
    { offset: '0%', color: '#10b981' },
    { offset: '30%', color: '#08080c' },
    { offset: '60%', color: '#06b6d4' },
    { offset: '80%', color: '#08080c' },
    { offset: '100%', color: '#34d399' },
  ]}
/>
```

```aura width=140 height=44 link="https://www.linkedin.com/in/kishanth-m-aa055b2a3/" inline align=center
<SocialMediaButton
  icon="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjI0IiBoZWlnaHQ9IjI0IiBmaWxsPSIjZmZmZmZmIj4KICA8cGF0aCBkPSJNMTkgMGgtMTRjLTIuNzYxIDAtNSAyLjIzOS01IDV2MTRjMCAyLjc2MSAyLjIzOSA1IDUgNWgxNGMyLjc2MiAwIDUtMi4yMzkgNS01di0xNGMwLTIuNzYxLTIuMjM4LTUtNS01em0tMTEgMTloLTN2LTExaDN2MTF6bS0xLjUtMTIuMjY4Yy0uOTY2IDAtMS43NS0uNzktMS43NS0xLjc2NHMuNzg0LTEuNzY0IDEuNzUtMS43NjQgMS43NS43OSAxLjc1IDEuNzY0LS43ODMgMS43NjQtMS43NSAxLjc2NHptMTMuNSAxMi4yNjhoLTN2LTUuNjA0YzAtMy4zNjgtNC0zLjExMy00IDB2NS42MDRoLTN2LTExaDN2MS43NjVjMS4zOTYtMi41ODYgNy0yLjc3NyA3IDIuNDc2djYuNzU5eiIvPgo8L3N2Zz4="
  text="LinkedIn"
  backgroundColor="#08080c"
  textColor="#ffffff"
  width={140}
  height={44}
  gradientStops={[
    { offset: '0%', color: '#3b82f6' },
    { offset: '30%', color: '#08080c' },
    { offset: '60%', color: '#60a5fa' },
    { offset: '80%', color: '#08080c' },
    { offset: '100%', color: '#93c5fd' },
  ]}
/>
```

```aura width=125 height=44 link="mailto:m.kishanth001@gmail.com" inline align=center
<SocialMediaButton
  icon="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjI0IiBoZWlnaHQ9IjI0IiBmaWxsPSIjZmZmZmZmIj4KICA8cGF0aCBkPSJNMjAgNEg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMThjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY2YzAtMS4xLS45LTItMi0yem0wIDRsLTggNS04LTVWNmw4IDUgOC01djJ6Ii8+Cjwvc3ZnPg=="
  text="Email"
  backgroundColor="#08080c"
  textColor="#ffffff"
  width={125}
  height={44}
  gradientStops={[
    { offset: '0%', color: '#a855f7' },
    { offset: '30%', color: '#08080c' },
    { offset: '60%', color: '#c084fc' },
    { offset: '80%', color: '#08080c' },
    { offset: '100%', color: '#e879f9' },
  ]}
/>
```

<p align="center"><sub>designed with <a href="https://github.com/collectioneur/readme-aura">readme-aura</a></sub></p>
