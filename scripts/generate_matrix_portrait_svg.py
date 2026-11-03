#!/usr/bin/env python3
"""
Matrix ASCII Portrait & Hero Banner Generator for Kishanth M.
Produces GitHub-compatible animated SVGs with:
- ASCII portrait of Kishanth M. from uploaded photo
- Multi-speed digital rain waterfalls
- Scanning beam effect
- Developer identity HUD (KISHANTH.M / AI ENGINEER IN PROGRESS)
- Status telemetry
"""

import sys
import os
import math
from collections import deque
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter

def load_and_segment(image_path):
    img = Image.open(image_path)
    arr = np.array(img).astype(float)
    h, w, _ = arr.shape
    
    # Calculate saturation & brightness
    r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]
    brightness = 0.299 * r + 0.587 * g + 0.114 * b
    max_c = np.maximum(np.maximum(r, g), b)
    min_c = np.minimum(np.minimum(r, g), b)
    sat = (max_c - min_c) / (max_c + 1e-5)
    
    # Background in studio shot has low saturation (< 0.12) and brightness between 55 and 130
    is_bg_candidate = (sat < 0.12) & (brightness > 55) & (brightness < 130)
    
    # Flood-fill from borders to only remove connected background
    visited = np.zeros((h, w), dtype=bool)
    is_bg = np.zeros((h, w), dtype=bool)
    q = deque()
    
    # Seed outer border
    for x in range(w):
        if is_bg_candidate[0, x]:
            q.append((0, x))
            visited[0, x] = True
        if is_bg_candidate[h - 1, x]:
            q.append((h - 1, x))
            visited[h - 1, x] = True
            
    for y in range(h):
        if is_bg_candidate[y, 0]:
            q.append((y, 0))
            visited[y, 0] = True
        if is_bg_candidate[y, w - 1]:
            q.append((y, w - 1))
            visited[y, w - 1] = True
            
    while q:
        cy, cx = q.popleft()
        is_bg[cy, cx] = True
        for ny, nx in ((cy-1, cx), (cy+1, cx), (cy, cx-1), (cy, cx+1)):
            if 0 <= ny < h and 0 <= nx < w:
                if not visited[ny, nx] and is_bg_candidate[ny, nx]:
                    visited[ny, nx] = True
                    q.append((ny, nx))
                    
    return img, is_bg, brightness, sat

def build_ascii_matrix(img_path, cols=50, rows=46):
    img, is_bg, _, _ = load_and_segment(img_path)
    w, h = img.size
    
    # Crop to center headshot
    # Original is 957x956. Head and shoulders:
    # Top of hair is y~80, chin is y~580, shoulders reach y~920.
    crop_box = (45, 30, 915, 920)
    img_cropped = img.crop(crop_box)
    
    # Also crop the is_bg mask
    mask_img = Image.fromarray((~is_bg).astype(np.uint8) * 255).crop(crop_box)
    
    # Resize to character grid
    small_img = img_cropped.resize((cols, rows), Image.Resampling.LANCZOS)
    small_mask = mask_img.resize((cols, rows), Image.Resampling.BILINEAR)
    
    # Convert to grayscale & enhance contrast
    gray = small_img.convert("L")
    enhancer = ImageEnhance.Contrast(gray)
    gray_enhanced = enhancer.enhance(1.45)
    
    arr_gray = np.array(gray_enhanced).astype(float)
    arr_mask = np.array(small_mask).astype(float) / 255.0
    arr_rgb = np.array(small_img).astype(float)
    
    # Characters ordered by density and Matrix visual feel
    # Allowed: 01ABCDEFGHIJKLMNOPQRSTUVWXYZ#$%&@<>/{}[]*
    GLYPH_HIGHLIGHT = ["@", "%", "#", "&", "M", "W", "8", "B", "$"]
    GLYPH_BRIGHT = ["K", "I", "S", "H", "A", "N", "T", "0", "1", "X", "Z"]
    GLYPH_MID = ["[", "]", "{", "}", "<", ">", "/", "*", "+", "="]
    GLYPH_DARK = ["0", "1", ":", "-", "."]
    
    grid = []
    
    for y in range(rows):
        row = []
        for x in range(cols):
            mask_val = arr_mask[y, x]
            val = arr_gray[y, x]
            r, g, b = arr_rgb[y, x]
            
            # Is background?
            if mask_val < 0.35:
                row.append(None) # None means background rain channel
                continue
                
            # It's Kishanth!
            # Distinguish hair, beard, skin, shirt, highlights
            is_hair_or_beard = (val < 50) and (y < rows * 0.72)
            is_shirt = (val < 60) and (y >= rows * 0.72)
            is_skin_highlight = (val > 155) and (r > 120)
            is_skin_bright = (val > 120) and not is_hair_or_beard
            is_skin_mid = (val >= 70) and not is_hair_or_beard
            
            if is_skin_highlight:
                # Teeth, nose highlight, forehead center
                char = GLYPH_HIGHLIGHT[(x + y) % len(GLYPH_HIGHLIGHT)]
                color = "#E6FFF2" # Brightest glowing green-white
                opacity = 1.0
                glow = True
            elif is_skin_bright:
                # Cheeks, forehead, chin
                char = GLYPH_BRIGHT[(x * 3 + y * 7) % len(GLYPH_BRIGHT)]
                color = "#00FF66" # Neon Matrix green
                opacity = 0.95
                glow = False
            elif is_skin_mid:
                # Shadows, jawline, under nose
                char = GLYPH_MID[(x + y * 2) % len(GLYPH_MID)]
                color = "#00CC55" # Emerald midtone
                opacity = 0.85
                glow = False
            elif is_hair_or_beard:
                # Hair curls, mustache, beard contour
                char = GLYPH_HIGHLIGHT[(x * 2 + y) % len(GLYPH_HIGHLIGHT)]
                color = "#00662A" # Deep matrix shadow
                opacity = 0.80
                glow = False
            elif is_shirt:
                # Shirt fabric and collar
                if val > 45 or (abs(x - cols/2) < 4 and y < rows * 0.85): # Collar edge & buttons
                    char = GLYPH_BRIGHT[(x + y) % len(GLYPH_BRIGHT)]
                    color = "#00AA55"
                    opacity = 0.85
                    glow = False
                else:
                    char = GLYPH_MID[(x + y) % len(GLYPH_MID)]
                    color = "#003B1E" # Deep cyber navy green
                    opacity = 0.65
                    glow = False
            else:
                char = GLYPH_DARK[(x + y) % len(GLYPH_DARK)]
                color = "#005522"
                opacity = 0.6
                glow = False
                
            row.append({
                "char": char,
                "color": color,
                "opacity": opacity,
                "glow": glow
            })
        grid.append(row)
        
    return grid, cols, rows

print("Module loaded successfully.")

def generate_hero_banner_svg(grid, cols, rows, output_path):
    width = 980
    height = 440
    
    # Portrait placement: left side (x: 35 to 445, y: 35 to 405)
    char_w = 7.5
    char_h = 7.8
    port_start_x = 35
    port_start_y = 50
    
    # Generate portrait text rows
    portrait_svg_elements = []
    
    # We group characters into rows using <text> and <tspan>
    for r_idx, row in enumerate(grid):
        y_pos = port_start_y + r_idx * char_h
        tspans = []
        cur_color = None
        cur_opacity = None
        cur_text = ""
        
        for c_idx, cell in enumerate(row):
            if cell is None:
                if cur_text:
                    tspans.append(f'<tspan fill="{cur_color}" fill-opacity="{cur_opacity}">{cur_text}</tspan>')
                    cur_text = ""
                cur_color = "none"
                cur_opacity = "0"
                cur_text = "&#160;"
                continue
                
            char = cell["char"]
            # XML escape
            if char == "<": char = "&lt;"
            elif char == ">": char = "&gt;"
            elif char == "&": char = "&amp;"
            elif char == '"': char = "&quot;"
            
            c_col = cell["color"]
            c_op = f"{cell['opacity']:.2f}"
            
            if c_col == cur_color and c_op == cur_opacity:
                cur_text += char
            else:
                if cur_text:
                    tspans.append(f'<tspan fill="{cur_color}" fill-opacity="{cur_opacity}">{cur_text}</tspan>')
                cur_color = c_col
                cur_opacity = c_op
                cur_text = char
                
        if cur_text:
            tspans.append(f'<tspan fill="{cur_color}" fill-opacity="{cur_opacity}">{cur_text}</tspan>')
            
        row_content = "".join(tspans)
        portrait_svg_elements.append(
            f'<text x="{port_start_x}" y="{y_pos:.1f}" font-family="JetBrains Mono, Consolas, Monaco, monospace" font-size="7.5" font-weight="700">{row_content}</text>'
        )
        
    portrait_markup = "\n      ".join(portrait_svg_elements)
    
    # Generate vertical rain columns
    rain_cols = []
    # 26 vertical rain streams across the canvas
    rain_x_coords = [15, 45, 80, 120, 160, 200, 240, 280, 320, 360, 400, 430, 460, 490, 520, 560, 600, 640, 680, 720, 760, 800, 840, 880, 920, 955]
    rain_chars = "01010101KISHANTHM101010101RAGAGENTS101010101VECTORLLM101010101"
    
    for i, rx in enumerate(rain_x_coords):
        dur = 2.2 + (i % 5) * 0.7
        delay = (i * 0.3) % 2.5
        slice_len = 16 + (i % 8)
        col_text = rain_chars[i % 20 : (i % 20) + slice_len]
        vertical_text = "".join([f'<tspan x="{rx}" dy="11">{ch}</tspan>' for ch in col_text])
        rain_cols.append(f'''
      <g class="rain-col" opacity="0.32" transform="translate(0, -220)">
        <text x="{rx}" y="0" fill="#00FF66" font-family="JetBrains Mono, Consolas, monospace" font-size="8.5" font-weight="bold">
          {vertical_text}
        </text>
        <animateTransform attributeName="transform" type="translate" from="{rx}, -260" to="{rx}, 480" dur="{dur:.1f}s" begin="{delay:.1f}s" repeatCount="indefinite" />
      </g>''')

    rain_markup = "\n".join(rain_cols)
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto">
  <defs>
    <!-- Matrix glow filters -->
    <filter id="matrixGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
    <filter id="laserGlow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="4" result="blur1" />
      <feGaussianBlur stdDeviation="8" result="blur2" />
      <feMerge>
        <feMergeNode in="blur2" />
        <feMergeNode in="blur1" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
    <linearGradient id="cyberBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00FF66" stop-opacity="0.8" />
      <stop offset="35%" stop-color="#008F39" stop-opacity="0.3" />
      <stop offset="70%" stop-color="#00f5d4" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#00FF66" stop-opacity="0.5" />
    </linearGradient>
    <linearGradient id="scanBeam" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#00FF66" stop-opacity="0" />
      <stop offset="50%" stop-color="#00FF66" stop-opacity="0.85" />
      <stop offset="100%" stop-color="#00FF66" stop-opacity="0" />
    </linearGradient>
    <linearGradient id="hudGradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0a1610" stop-opacity="0.95" />
      <stop offset="100%" stop-color="#050a08" stop-opacity="0.85" />
    </linearGradient>
    
    <style>
      @keyframes portraitMaterialize {{
        0% {{ opacity: 0; filter: blur(6px); }}
        20% {{ opacity: 0.15; filter: blur(4px); }}
        50% {{ opacity: 0.7; filter: blur(1px); }}
        75% {{ opacity: 1; filter: blur(0px); }}
        100% {{ opacity: 1; filter: blur(0px); }}
      }}
      @keyframes scanSweep {{
        0% {{ transform: translateY(30px); opacity: 0; }}
        15% {{ opacity: 0.9; }}
        85% {{ opacity: 0.9; }}
        100% {{ transform: translateY(390px); opacity: 0; }}
      }}
      @keyframes hudFadeIn {{
        0% {{ opacity: 0; transform: translateX(20px); }}
        40% {{ opacity: 0; transform: translateX(20px); }}
        70% {{ opacity: 0.8; transform: translateX(5px); }}
        100% {{ opacity: 1; transform: translateX(0); }}
      }}
      @keyframes pulseBeacon {{
        0%, 100% {{ opacity: 0.4; r: 3.5; }}
        50% {{ opacity: 1; r: 5; }}
      }}
      @keyframes textGlitch {{
        0%, 94%, 100% {{ transform: translate(0, 0); }}
        95% {{ transform: translate(-1.5px, 0.5px); }}
        97% {{ transform: translate(1.5px, -0.5px); }}
      }}
      .portrait-group {{
        animation: portraitMaterialize 6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
      }}
      .hud-group {{
        animation: hudFadeIn 5.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
      }}
      .scanner-beam {{
        animation: scanSweep 4.5s ease-in-out infinite;
      }}
      .glitch-text {{
        animation: textGlitch 7s infinite;
      }}
      .beacon {{
        animation: pulseBeacon 2.2s infinite ease-in-out;
      }}
      .btn:hover {{
        filter: brightness(1.3);
      }}
    </style>
  </defs>

  <!-- Background Void -->
  <rect width="{width}" height="{height}" fill="#050807" rx="14" />
  
  <!-- Subtle CRT Scanlines -->
  <pattern id="scanlines" width="100" height="4" patternUnits="userSpaceOnUse">
    <line x1="0" y1="0" x2="100" y2="0" stroke="#00FF66" stroke-opacity="0.04" stroke-width="1" />
  </pattern>
  <rect width="{width}" height="{height}" fill="url(#scanlines)" rx="14" />
  
  <!-- Outer Matrix Cyber Border -->
  <rect x="2" y="2" width="{width-4}" height="{height-4}" fill="none" stroke="url(#cyberBorder)" stroke-width="1.5" rx="13" />
  
  <!-- Top Corner Cyber Decals -->
  <path d="M 12 2 L 2 12" stroke="#00FF66" stroke-width="2" />
  <path d="M {width-12} 2 L {width-2} 12" stroke="#00FF66" stroke-width="2" />
  <path d="M 12 {height-2} L 2 {height-12}" stroke="#00FF66" stroke-width="2" />
  <path d="M {width-12} {height-2} L {width-2} {height-12}" stroke="#00FF66" stroke-width="2" />
  
  <!-- Top Telemetry Header -->
  <g font-family="JetBrains Mono, Consolas, monospace" font-size="9" fill="#00FF66" opacity="0.8">
    <text x="24" y="22" letter-spacing="1.5">SYS.ID // KISHANTH-M::NODE-01</text>
    <circle cx="280" cy="19" r="4" fill="#00FF66" class="beacon" />
    <text x="292" y="22" fill="#55FF99">STATUS: ONLINE</text>
    <text x="440" y="22" fill="#7a9988">ARCH: NEURAL_RAG::MULTI_AGENT</text>
    <text x="800" y="22" fill="#00f5d4" letter-spacing="1">LOC: CHENNAI_TN [IN]</text>
  </g>
  <line x1="20" y1="28" x2="{width-20}" y2="28" stroke="#00FF66" stroke-opacity="0.25" stroke-width="1" />

  <!-- Background Matrix Rain Waterfall -->
  <g opacity="0.75">
    {rain_markup}
  </g>

  <!-- Left: ASCII Portrait Holographic Bay -->
  <g class="portrait-group">
    <!-- Frame around portrait -->
    <rect x="30" y="38" width="385" height="375" fill="#030604" fill-opacity="0.88" rx="8" stroke="#00FF66" stroke-opacity="0.4" stroke-width="1.2" />
    
    <!-- Hologram Corner Brackets -->
    <path d="M 30 55 L 30 38 L 48 38" fill="none" stroke="#00FF66" stroke-width="2.5" />
    <path d="M 397 38 L 415 38 L 415 55" fill="none" stroke="#00FF66" stroke-width="2.5" />
    <path d="M 30 395 L 30 413 L 48 413" fill="none" stroke="#00FF66" stroke-width="2.5" />
    <path d="M 397 413 L 415 413 L 415 395" fill="none" stroke="#00FF66" stroke-width="2.5" />
    
    <!-- Hologram Title Tag -->
    <rect x="42" y="34" width="130" height="15" fill="#050a08" stroke="#00FF66" stroke-width="1" rx="2" />
    <text x="50" y="44" font-family="JetBrains Mono, Consolas, monospace" font-size="8" fill="#55FF99" font-weight="bold" letter-spacing="1">BIO_SCAN::PORTRAIT</text>
    
    <!-- Actual ASCII Render of Kishanth M. -->
    <g>
      {portrait_markup}
    </g>
    
    <!-- Laser Scanning Beam (Sweeping vertically across the face) -->
    <g class="scanner-beam">
      <rect x="32" y="0" width="381" height="4" fill="url(#scanBeam)" filter="url(#laserGlow)" />
      <line x1="32" y1="2" x2="413" y2="2" stroke="#55FF99" stroke-width="1.8" filter="url(#laserGlow)" />
    </g>
    
    <!-- Portrait Bottom Telemetry -->
    <rect x="38" y="392" width="369" height="16" fill="#040806" fill-opacity="0.9" rx="3" />
    <text x="46" y="403" font-family="JetBrains Mono, Consolas, monospace" font-size="8" fill="#00FF66" opacity="0.9">RESOLUTION: 48x42 ASCII // MESH: VERIFIED // FACE_ID: 100%</text>
  </g>

  <!-- Right: Developer Identity HUD & Mission Control -->
  <g class="hud-group" transform="translate(445, 40)">
    <!-- HUD Panel Card Background -->
    <rect x="0" y="0" width="505" height="375" fill="url(#hudGradient)" rx="8" stroke="#00FF66" stroke-opacity="0.35" stroke-width="1.2" />
    
    <!-- Top HUD Bar -->
    <path d="M 0 0 L 15 0 L 22 14 L 140 14 L 147 0 L 505 0" fill="none" stroke="#00FF66" stroke-opacity="0.5" stroke-width="1" />
    <text x="28" y="11" font-family="JetBrains Mono, Consolas, monospace" font-size="8" fill="#00f5d4" font-weight="bold" letter-spacing="1.5">AI_CORE_SYSTEM::IDENTITY</text>

    <!-- Main Identity Name -->
    <g class="glitch-text" transform="translate(25, 55)">
      <text x="0" y="0" font-family="JetBrains Mono, Consolas, Monaco, monospace" font-size="34" font-weight="900" fill="#00FF66" letter-spacing="3" filter="url(#matrixGlow)">KISHANTH.M</text>
      <!-- Subtitle -->
      <text x="2" y="26" font-family="JetBrains Mono, Consolas, monospace" font-size="13" font-weight="700" fill="#00f5d4" letter-spacing="2.5">AI ENGINEER IN PROGRESS</text>
      <text x="2" y="44" font-family="JetBrains Mono, Consolas, monospace" font-size="10" font-weight="500" fill="#a7f3d0" letter-spacing="1">Aspiring AI Engineer | Generative AI Developer</text>
    </g>

    <!-- Mission Terminal Quote Box -->
    <g transform="translate(25, 125)">
      <rect x="0" y="0" width="455" height="52" fill="#030805" rx="5" stroke="#00FF66" stroke-opacity="0.25" stroke-width="1" />
      <line x1="0" y1="0" x2="3" y2="52" stroke="#00FF66" stroke-width="3" />
      <text x="14" y="20" font-family="JetBrains Mono, Consolas, monospace" font-size="10" font-weight="700" fill="#55FF99" letter-spacing="1">&gt; MISSION_OBJECTIVE:</text>
      <text x="14" y="38" font-family="JetBrains Mono, Consolas, monospace" font-size="11" font-weight="600" fill="#E6FFF2" letter-spacing="0.5">"BUILDING INTELLIGENCE, ONE MODEL AT A TIME."</text>
    </g>

    <!-- Tech Grid Badges -->
    <g transform="translate(25, 195)">
      <text x="0" y="0" font-family="JetBrains Mono, Consolas, monospace" font-size="9" fill="#7a9988" font-weight="700" letter-spacing="1">CORE ARCHITECTURE DOMAINS:</text>
      
      <!-- Row 1 -->
      <g transform="translate(0, 10)">
        <rect x="0" y="0" width="138" height="22" fill="#08140e" rx="4" stroke="#00FF66" stroke-opacity="0.4" stroke-width="1" />
        <text x="10" y="14" font-family="JetBrains Mono, Consolas, monospace" font-size="8.5" fill="#00FF66" font-weight="600">⚡ LLMs &amp; GenAI</text>

        <rect x="148" y="0" width="155" height="22" fill="#08140e" rx="4" stroke="#00FF66" stroke-opacity="0.4" stroke-width="1" />
        <text x="158" y="14" font-family="JetBrains Mono, Consolas, monospace" font-size="8.5" fill="#00FF66" font-weight="600">🧠 Multi-Agent Systems</text>

        <rect x="313" y="0" width="142" height="22" fill="#08140e" rx="4" stroke="#00FF66" stroke-opacity="0.4" stroke-width="1" />
        <text x="323" y="14" font-family="JetBrains Mono, Consolas, monospace" font-size="8.5" fill="#00FF66" font-weight="600">🔍 RAG Architecture</text>
      </g>
      
      <!-- Row 2 -->
      <g transform="translate(0, 38)">
        <rect x="0" y="0" width="138" height="22" fill="#08140e" rx="4" stroke="#00f5d4" stroke-opacity="0.4" stroke-width="1" />
        <text x="10" y="14" font-family="JetBrains Mono, Consolas, monospace" font-size="8.5" fill="#00f5d4" font-weight="600">🌐 LangGraph / LangChain</text>

        <rect x="148" y="0" width="155" height="22" fill="#08140e" rx="4" stroke="#00f5d4" stroke-opacity="0.4" stroke-width="1" />
        <text x="158" y="14" font-family="JetBrains Mono, Consolas, monospace" font-size="8.5" fill="#00f5d4" font-weight="600">🎯 Computer Vision (YOLO)</text>

        <rect x="313" y="0" width="142" height="22" fill="#08140e" rx="4" stroke="#00f5d4" stroke-opacity="0.4" stroke-width="1" />
        <text x="323" y="14" font-family="JetBrains Mono, Consolas, monospace" font-size="8.5" fill="#00f5d4" font-weight="600">🗄️ Vector DBs (Chroma)</text>
      </g>
    </g>

    <!-- Real-time Telemetry & Education -->
    <g transform="translate(25, 275)" font-family="JetBrains Mono, Consolas, monospace" font-size="9">
      <line x1="0" y1="0" x2="455" y2="0" stroke="#00FF66" stroke-opacity="0.2" stroke-width="1" />
      <text x="0" y="16" fill="#7a9988">DEGREE:</text>
      <text x="65" y="16" fill="#E6FFF2" font-weight="600">B.Tech Artificial Intelligence &amp; Data Science</text>
      <text x="0" y="32" fill="#7a9988">COLLEGE:</text>
      <text x="65" y="32" fill="#55FF99">Adhiyamaan College of Engineering</text>
    </g>

    <!-- Interactive Navigation Link Buttons -->
    <g transform="translate(25, 325)">
      <!-- GitHub Button -->
      <a href="https://github.com/kishanth-m" target="_blank" class="btn">
        <rect x="0" y="0" width="140" height="30" fill="#0d2417" rx="5" stroke="#00FF66" stroke-width="1.2" />
        <text x="18" y="19" font-family="JetBrains Mono, Consolas, monospace" font-size="10" font-weight="700" fill="#00FF66">⚡ GITHUB PROFILE</text>
      </a>

      <!-- LinkedIn Button -->
      <a href="https://www.linkedin.com/in/kishanth-m-aa055b2a3/" target="_blank" class="btn">
        <rect x="155" y="0" width="145" height="30" fill="#081d26" rx="5" stroke="#00f5d4" stroke-width="1.2" />
        <text x="172" y="19" font-family="JetBrains Mono, Consolas, monospace" font-size="10" font-weight="700" fill="#00f5d4">🌐 LINKEDIN</text>
      </a>
      
      <!-- Terminal Status Beacon -->
      <g transform="translate(325, 10)">
        <circle cx="0" cy="5" r="4" fill="#00FF66" class="beacon" />
        <text x="10" y="9" font-family="JetBrains Mono, Consolas, monospace" font-size="9" fill="#55FF99" font-weight="bold">AI LAB ACTIVE</text>
      </g>
    </g>

  </g>
</svg>'''

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Hero banner SVG written to: {output_path}")

def generate_standalone_matrix_portrait_svg(grid, cols, rows, output_path):
    width = 460
    height = 520
    
    char_w = 7.8
    char_h = 9.2
    start_x = 35
    start_y = 65
    
    portrait_svg_elements = []
    
    for r_idx, row in enumerate(grid):
        y_pos = start_y + r_idx * char_h
        tspans = []
        cur_color = None
        cur_opacity = None
        cur_text = ""
        
        for c_idx, cell in enumerate(row):
            if cell is None:
                if cur_text:
                    tspans.append(f'<tspan fill="{cur_color}" fill-opacity="{cur_opacity}">{cur_text}</tspan>')
                    cur_text = ""
                cur_color = "none"
                cur_opacity = "0"
                cur_text = "&#160;"
                continue
                
            char = cell["char"]
            if char == "<": char = "&lt;"
            elif char == ">": char = "&gt;"
            elif char == "&": char = "&amp;"
            elif char == '"': char = "&quot;"
            
            c_col = cell["color"]
            c_op = f"{cell['opacity']:.2f}"
            
            if c_col == cur_color and c_op == cur_opacity:
                cur_text += char
            else:
                if cur_text:
                    tspans.append(f'<tspan fill="{cur_color}" fill-opacity="{cur_opacity}">{cur_text}</tspan>')
                cur_color = c_col
                cur_opacity = c_op
                cur_text = char
                
        if cur_text:
            tspans.append(f'<tspan fill="{cur_color}" fill-opacity="{cur_opacity}">{cur_text}</tspan>')
            
        row_content = "".join(tspans)
        portrait_svg_elements.append(
            f'<text x="{start_x}" y="{y_pos:.1f}" font-family="JetBrains Mono, Consolas, Monaco, monospace" font-size="8" font-weight="bold">{row_content}</text>'
        )
        
    portrait_markup = "\n      ".join(portrait_svg_elements)
    
    # Rains
    rain_x_coords = [15, 35, 60, 90, 130, 170, 210, 250, 290, 330, 370, 405, 435]
    rain_chars = "0101KISHANTHM10101RAG10101AGENT1010101"
    rain_cols = []
    for i, rx in enumerate(rain_x_coords):
        dur = 2.4 + (i % 4) * 0.6
        delay = (i * 0.4) % 2.0
        vertical_text = "".join([f'<tspan x="{rx}" dy="12">{ch}</tspan>' for ch in rain_chars[i % 15 : (i % 15) + 16]])
        rain_cols.append(f'''
      <g opacity="0.35" transform="translate(0, -220)">
        <text x="{rx}" y="0" fill="#00FF66" font-family="JetBrains Mono, Consolas, monospace" font-size="9" font-weight="bold">
          {vertical_text}
        </text>
        <animateTransform attributeName="transform" type="translate" from="{rx}, -240" to="{rx}, 540" dur="{dur:.1f}s" begin="{delay:.1f}s" repeatCount="indefinite" />
      </g>''')
    rain_markup = "\n".join(rain_cols)
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="auto">
  <defs>
    <filter id="matrixGlowP" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
    <filter id="laserGlowP" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="4" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
    <linearGradient id="scanBeamP" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#00FF66" stop-opacity="0" />
      <stop offset="50%" stop-color="#00FF66" stop-opacity="0.9" />
      <stop offset="100%" stop-color="#00FF66" stop-opacity="0" />
    </linearGradient>
    <linearGradient id="portraitBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00FF66" stop-opacity="0.9" />
      <stop offset="50%" stop-color="#004d1f" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#00f5d4" stop-opacity="0.9" />
    </linearGradient>
    <style>
      @keyframes portraitAppear {{
        0% {{ opacity: 0; filter: blur(5px); }}
        30% {{ opacity: 0.2; }}
        70% {{ opacity: 0.85; filter: blur(1px); }}
        100% {{ opacity: 1; filter: blur(0); }}
      }}
      @keyframes scanSweepP {{
        0% {{ transform: translateY(45px); opacity: 0; }}
        10% {{ opacity: 0.95; }}
        90% {{ opacity: 0.95; }}
        100% {{ transform: translateY(470px); opacity: 0; }}
      }}
      @keyframes beaconPulse {{
        0%, 100% {{ opacity: 0.3; }}
        50% {{ opacity: 1; }}
      }}
      .p-group {{
        animation: portraitAppear 5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
      }}
      .scanner {{
        animation: scanSweepP 4s ease-in-out infinite;
      }}
      .beacon-p {{
        animation: beaconPulse 2s infinite ease-in-out;
      }}
    </style>
  </defs>

  <rect width="{width}" height="{height}" fill="#050807" rx="12" />
  <rect x="2" y="2" width="{width-4}" height="{height-4}" fill="none" stroke="url(#portraitBorder)" stroke-width="1.5" rx="11" />
  
  <!-- Corner Tech Accents -->
  <path d="M 10 2 L 2 10" stroke="#00FF66" stroke-width="2" />
  <path d="M {width-10} 2 L {width-2} 10" stroke="#00FF66" stroke-width="2" />
  <path d="M 10 {height-2} L 2 {height-10}" stroke="#00FF66" stroke-width="2" />
  <path d="M {width-10} {height-2} L {width-2} {height-10}" stroke="#00FF66" stroke-width="2" />
  
  <!-- HUD Header -->
  <g font-family="JetBrains Mono, Consolas, monospace" font-size="8.5" fill="#00FF66">
    <text x="20" y="22" letter-spacing="1.5" font-weight="bold">TARGET // KISHANTH_M</text>
    <circle cx="340" cy="19" r="3.5" fill="#00FF66" class="beacon-p" />
    <text x="350" y="22" fill="#55FF99">SCAN: COMPLETE</text>
  </g>
  <line x1="16" y1="28" x2="{width-16}" y2="28" stroke="#00FF66" stroke-opacity="0.3" stroke-width="1" />

  <!-- Background Rain -->
  <g opacity="0.6">
    {rain_markup}
  </g>

  <!-- Portrait Container -->
  <g class="p-group">
    <g>
      {portrait_markup}
    </g>

    <!-- Scanning beam -->
    <g class="scanner">
      <rect x="25" y="0" width="{width-50}" height="4" fill="url(#scanBeamP)" filter="url(#laserGlowP)" />
      <line x1="25" y1="2" x2="{width-25}" y2="2" stroke="#55FF99" stroke-width="1.6" filter="url(#laserGlowP)" />
    </g>
  </g>

  <!-- Footer Tag -->
  <rect x="20" y="{height-30}" width="{width-40}" height="18" fill="#040806" fill-opacity="0.95" rx="4" stroke="#00FF66" stroke-opacity="0.3" stroke-width="1" />
  <text x="30" y="{height-18}" font-family="JetBrains Mono, Consolas, monospace" font-size="8" fill="#55FF99" letter-spacing="1">
    ASCII NEURAL RECONSTRUCTION // 01001011 01001101
  </text>
</svg>'''

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Standalone matrix portrait SVG written to: {output_path}")

if __name__ == "__main__":
    photo_path = os.path.join("assets", "portrait", "original-photo.jpg")
    assets_dir = os.path.join(".github", "assets")
    os.makedirs(assets_dir, exist_ok=True)
    
    if not os.path.exists(photo_path):
        print(f"Portrait photo {photo_path} is kept private and not present. Skipping regeneration.")
        sys.exit(0)

    print("Building ASCII matrix from photograph...")
    grid, cols, rows = build_ascii_matrix(photo_path, cols=48, rows=42)
    
    hero_path = os.path.join(assets_dir, "hero-banner.svg")
    portrait_path = os.path.join(assets_dir, "matrix-portrait.svg")
    
    generate_hero_banner_svg(grid, cols, rows, hero_path)
    generate_standalone_matrix_portrait_svg(grid, cols, rows, portrait_path)
    print("All Matrix SVG assets successfully generated!")
