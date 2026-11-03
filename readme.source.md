```aura width=860 height=210
(function() {
  var portraitUri = "data:image/jpeg;base64,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";

  return (
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
        <img
          src={portraitUri}
          style={{
            width: 88, height: 88, borderRadius: 44,
            objectFit: 'cover', objectPosition: 'center'
          }}
        />
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
  );
})()
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

```aura width=860 height=410
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

  var col1 = [projects[0], projects[1]];
  var col2 = [projects[2], projects[3]];

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

      <svg width="860" height="410" style={{ position: 'absolute', top: 0, left: 0 }}>
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
        <ellipse id="pg-1" cx="200" cy="340" rx="250" ry="160" fill="url(#pg1)" />
        <ellipse id="pg-2" cx="640" cy="350" rx="230" ry="150" fill="url(#pg2)" />
      </svg>

      <div style={{ display: 'flex', fontSize: 10, fontWeight: 700, color: 'rgba(52,211,153,0.7)', letterSpacing: '3px', marginBottom: 14 }}>
        FEATURED ARCHITECTURES // PROJECT SHOWCASE
      </div>

      <div style={{ display: 'flex', gap: 14 }}>
        {[col1, col2].map(function(col, colIdx) {
          return (
            <div key={colIdx} style={{ display: 'flex', flexDirection: 'column', width: 388, gap: 12 }}>
              {col.map(function(p) {
                return (
                  <div key={p.title} style={{
                    display: 'flex', flexDirection: 'column',
                    padding: '16px 18px', borderRadius: 10,
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
  icon="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjI0IiBoZWlnaHQ9IjI0IiBmaWxsPSIjZmZmZmZmIj4KICA8cGF0aCBkPSJNMTkgMGgtMTRjLTIuNzYxIDAtNSAyLjIzOS01IDV2MTRjMCAyLjc2MSAyLjIzOSA1IDUgNWgxNGMyLjc2MiAwIDUtMi4yMzkgNS01di0xNGMwLTIuNzYxLTIuMjM4LTUtNS01em0tMTEgMTloLTN2LTExaDN2MTF6bS0xLjUtMTIuMjY4Yy0uOTY2IDAtMS43NS0uNzktMS43NS0xLjc2NHMuNzg0LTEuNzY0IDEuNzUtMS43NjQgMS43NS43OSAxLjc1IDEuNzY0LS43ODMsMS43NjQtMS43NSAxLjc2NHptMTMuNSAxMi4yNjhoLTN2LTUuNjA0YzAtMy4zNjgtNC0zLjExMy00IDB2NS42MDRoLTN2LTExaDN2MS43NjVjMS4zOTYtMi41ODYgNy0yLjc3NyA3IDIuNDc2djYuNzU5eiIvPgo8L3N2Zz4="
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
