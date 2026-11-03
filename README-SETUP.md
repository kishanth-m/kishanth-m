# Kishanth M. — GitHub Profile Setup & Architecture Guide

This GitHub profile is engineered using **[`readme-aura`](https://github.com/collectioneur/readme-aura)**, compiling custom JSX components, CSS keyframe animations, and Satori vector layouts directly into GitHub-sanitized static SVGs.

---

## 📁 Repository Blueprint

```text
kishanth-m/
│
├── .github/
│   ├── assets/                             # Pre-rendered SVG compositions
│   │   ├── readme-aura-component-0-*.svg   # Hero Identity & Abstract AI Monogram
│   │   ├── readme-aura-component-1-*.svg   # Technical Focus & Verified Capabilities
│   │   ├── readme-aura-component-2-*.svg   # Featured Architectures / Project Showcase
│   │   ├── readme-aura-component-3-*.svg   # Animated GitHub Button
│   │   ├── readme-aura-component-4-*.svg   # Animated LinkedIn Button
│   │   └── readme-aura-component-5-*.svg   # Animated Email Button
│   │
│   └── workflows/
│       └── readme-aura.yml                 # Official readme-aura CI/CD action
│
├── icons/                                  # Source vector icons for social media buttons
│   ├── github-icon.svg
│   ├── linkedin-icon.svg
│   └── email-icon.svg
│
├── readme.source.md                        # Master source document (edit this!)
├── README.md                               # Public README (compiled by readme-aura)
├── .gitignore                              # Clean repository exclusions
└── README-SETUP.md                         # Architecture and local maintenance guide
```

---

## 🚀 Local Development & Preview Workflow

Whenever you want to modify your bio, skills, or projects, edit `readme.source.md` and rebuild locally:

```bash
# 1. Preview and build components to SVG
npx readme-aura build

# 2. Stage changes
git add readme.source.md README.md .github/assets/

# 3. Commit and push
git commit -m "chore: update profile aura components"
git push origin main
```

---

## 🔄 Automated GitHub Actions Workflow

When you push updates to `readme.source.md`, `.github/workflows/readme-aura.yml` automatically triggers on GitHub's cloud runners:
- It checks out your code.
- Invokes `collectioneur/readme-aura@main`.
- Re-compiles `readme.source.md` into new `.github/assets/*.svg` assets.
- Automatically commits and updates `README.md`.
- Runs on a daily schedule (`0 6 * * *`) to keep dynamic data updated.

---

## 🎨 Visual Design System & Palette

- **Base Void:** `#08080c` (deep obsidian / charcoal)
- **Primary Emerald:** `#10b981` (luminous AI accent)
- **Teal / Cyan:** `#06b6d4` (computational highlight)
- **Cobalt / Sapphire:** `#3b82f6` (frameworks & memory)
- **Violet / Purple:** `#a855f7` (computer vision & neural perception)
- **Typography:** `Inter, sans-serif` rendered via Vercel Satori at build time.
- **Motion:** Restrained, non-distracting CSS `@keyframes` floating radial gradient orbs and 360° rotating holographic gradient borders.
