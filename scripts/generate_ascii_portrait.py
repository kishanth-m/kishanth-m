#!/usr/bin/env python3
"""
=============================================================================
  MATRIX ASCII PORTRAIT GENERATOR FOR KISHANTH M.
  Generates GitHub-compatible animated SVGs from a photograph:
  1. Standalone Matrix ASCII Portrait (.github/assets/matrix-portrait.svg)
  2. Master Futuristic Hero Banner (.github/assets/hero-banner.svg)
=============================================================================
"""

import sys
import os
import argparse
from collections import deque
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter

# Allowed character glyphs from user specification:
# 01ABCDEFGHIJKLMNOPQRSTUVWXYZ#$%&@<>/{}[]*
GLYPH_HIGHLIGHT = ["@", "%", "#", "&", "M", "W", "8", "B", "$"]
GLYPH_BRIGHT = ["K", "I", "S", "H", "A", "N", "T", "0", "1", "X", "Z"]
GLYPH_MID = ["[", "]", "{", "}", "<", ">", "/", "*", "+", "="]
GLYPH_DARK = ["0", "1", ":", "-", "."]

def load_and_segment(image_path):
    """
    Loads photograph and extracts the person silhouette by isolating the studio background.
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Source photograph not found: {image_path}")
        
    img = Image.open(image_path)
    arr = np.array(img).astype(float)
    h, w, _ = arr.shape
    
    r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]
    brightness = 0.299 * r + 0.587 * g + 0.114 * b
    max_c = np.maximum(np.maximum(r, g), b)
    min_c = np.minimum(np.minimum(r, g), b)
    sat = (max_c - min_c) / (max_c + 1e-5)
    
    # Neutral studio grey background condition
    is_bg_candidate = (sat < 0.12) & (brightness > 55) & (brightness < 130)
    
    # Connected component flood-fill from boundaries
    visited = np.zeros((h, w), dtype=bool)
    is_bg = np.zeros((h, w), dtype=bool)
    q = deque()
    
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
        for ny, nx in ((cy - 1, cx), (cy + 1, cx), (cy, cx - 1), (cy, cx + 1)):
            if 0 <= ny < h and 0 <= nx < w:
                if not visited[ny, nx] and is_bg_candidate[ny, nx]:
                    visited[ny, nx] = True
                    q.append((ny, nx))
                    
    return img, is_bg

def build_ascii_matrix(img_path, cols=48, rows=42):
    """
    Transforms photograph into a structured 2D Matrix character grid with color and luminance data.
    """
    img, is_bg = load_and_segment(img_path)
    w, h = img.size
    
    # Center headshot crop
    crop_box = (45, 30, 915, 920)
    img_cropped = img.crop(crop_box)
    mask_img = Image.fromarray((~is_bg).astype(np.uint8) * 255).crop(crop_box)
    
    small_img = img_cropped.resize((cols, rows), Image.Resampling.LANCZOS)
    small_mask = mask_img.resize((cols, rows), Image.Resampling.BILINEAR)
    
    gray = small_img.convert("L")
    enhancer = ImageEnhance.Contrast(gray)
    gray_enhanced = enhancer.enhance(1.45)
    
    arr_gray = np.array(gray_enhanced).astype(float)
    arr_mask = np.array(small_mask).astype(float) / 255.0
    arr_rgb = np.array(small_img).astype(float)
    
    grid = []
    
    for y in range(rows):
        row = []
        for x in range(cols):
            mask_val = arr_mask[y, x]
            val = arr_gray[y, x]
            r, g, b = arr_rgb[y, x]
            
            if mask_val < 0.35:
                row.append(None)
                continue
                
            is_hair_or_beard = (val < 50) and (y < rows * 0.72)
            is_shirt = (val < 60) and (y >= rows * 0.72)
            is_skin_highlight = (val > 155) and (r > 120)
            is_skin_bright = (val > 120) and not is_hair_or_beard
            is_skin_mid = (val >= 70) and not is_hair_or_beard
            
            if is_skin_highlight:
                char = GLYPH_HIGHLIGHT[(x + y) % len(GLYPH_HIGHLIGHT)]
                color = "#E6FFF2"
                opacity = 1.0
            elif is_skin_bright:
                char = GLYPH_BRIGHT[(x * 3 + y * 7) % len(GLYPH_BRIGHT)]
                color = "#00FF66"
                opacity = 0.95
            elif is_skin_mid:
                char = GLYPH_MID[(x + y * 2) % len(GLYPH_MID)]
                color = "#00CC55"
                opacity = 0.85
            elif is_hair_or_beard:
                char = GLYPH_HIGHLIGHT[(x * 2 + y) % len(GLYPH_HIGHLIGHT)]
                color = "#00662A"
                opacity = 0.80
            elif is_shirt:
                if val > 45 or (abs(x - cols / 2) < 4 and y < rows * 0.85):
                    char = GLYPH_BRIGHT[(x + y) % len(GLYPH_BRIGHT)]
                    color = "#00AA55"
                    opacity = 0.85
                else:
                    char = GLYPH_MID[(x + y) % len(GLYPH_MID)]
                    color = "#003B1E"
                    opacity = 0.65
            else:
                char = GLYPH_DARK[(x + y) % len(GLYPH_DARK)]
                color = "#005522"
                opacity = 0.60
                
            row.append({
                "char": char,
                "color": color,
                "opacity": opacity
            })
        grid.append(row)
        
    return grid, cols, rows

def generate_svg_assets(photo_path, output_dir=".github/assets"):
    os.makedirs(output_dir, exist_ok=True)
    if not os.path.exists(photo_path):
        print(f"Source photograph not found at {photo_path} (kept private). Using pre-rendered SVGs.")
        return
    grid, cols, rows = build_ascii_matrix(photo_path)
    
    # Generate standalone matrix-portrait.svg and hero-banner.svg
    from generate_matrix_portrait_svg import generate_hero_banner_svg, generate_standalone_matrix_portrait_svg
    
    hero_path = os.path.join(output_dir, "hero-banner.svg")
    portrait_path = os.path.join(output_dir, "matrix-portrait.svg")
    
    generate_hero_banner_svg(grid, cols, rows, hero_path)
    generate_standalone_matrix_portrait_svg(grid, cols, rows, portrait_path)
    print(f"Generated: {hero_path}")
    print(f"Generated: {portrait_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Matrix ASCII Portrait Generator")
    parser.add_argument("--image", default="assets/portrait/original-photo.jpg", help="Path to input photo")
    parser.add_argument("--outdir", default=".github/assets", help="Output directory for generated SVGs")
    args = parser.parse_args()
    
    print(f"Processing photo: {args.image} -> {args.outdir}")
    generate_svg_assets(args.image, args.outdir)
    print("Matrix generation complete!")
