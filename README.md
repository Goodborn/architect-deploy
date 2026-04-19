# 🚀 CKDEPS

**CKDEPS — A personal initial (fresh install) app to get CachyOS KDE ready.**

CKDEPS is a personal initial (fresh install) app to my liking to get CachyOS KDE ready for my personal use.

![CKDEPS](https://img.shields.io/badge/GTK4-Adwaita-a855f7?style=for-the-badge)
![License](https://img.shields.io/badge/license-GPL--3.0-green?style=for-the-badge)
![Arch](https://img.shields.io/badge/CachyOS-Arch_Linux-1793d1?style=for-the-badge)

---

## ✨ Features

| 📦 **Smart Packages** | Personalized list of AUR + Flatpak apps |
| ⚡ **One-Click Bootstrap** | Automates system updates and manager setup |
| 🎨 **Personal Tweaks** | Custom aliases, startup apps, and app configs |
| 📊 **Live Progress** | Real-time installation tracking with log output |

## 📋 Package List

### AUR / Pacman
thefuck, fzf, atuin, zoxide, bazaar, hyprsunset, anydesk-bin, foliate,
libreoffice-still, betterbird, bolt-launcher, haruna, popcorntime,
vmware-workstation, vmware-keymaps, qbittorrent, vesktop, obs-studio,
visual-studio-code-bin, proton-vpn-gtk-app, harmonoid, brave-bin, firefox, eden

### Flatpak
Spotify, Kdenlive, Upscayl, Blanket, Cozy

---

## 🔧 Installation

### ⚡ One-Tap Run (Arch / CachyOS)
Copy and paste this block to launch:
```bash
git clone https://github.com/goodborn/ckdeps-personal.git && \
cd ckdeps-personal && \
make run
```

### 🚀 How to Run
After installing, you can launch the app anytime by:
1. Typing `ckdeps` in your terminal.
2. Searching for **"CKDEPS"** in your application menu.
3. Running `make run` inside the project folder.

### 📦 From AUR (Recommended)
If you prefer using an AUR helper like `yay`:
```bash
yay -S ckdeps
```

### 🛠️ Run from Source (Development)
To test changes without installing to your system:
```bash
git clone https://github.com/goodborn/ckdeps.git
cd ckdeps
python3 -m architect_deploy
```

---

## 🏗️ Dependencies

| Package | Purpose |
|---------|---------|
| `python` | Runtime |
| `python-gobject` | GTK4 bindings (PyGObject) |
| `gtk4` | UI toolkit |
| `libadwaita` | GNOME design language |
| `flatpak` | Flatpak package manager |
| `pacman` | Arch package manager |

**Optional:** `yay` or `paru` for AUR package installation.

---

## 📁 Project Structure

```
ckdeps/
├── ckdeps/
│   ├── __init__.py          # CKDEPS — A personal initial (fresh install) app to get CachyOS KDE ready.
│   ├── main.py              # Application entry point
│   ├── window.py            # Main window + page navigation
│   ├── backend/
│   │   ├── installer.py     # Threaded shell command execution
│   │   └── package_data.py  # Package & extras definitions
│   ├── pages/
│   │   ├── welcome.py       # A personal initial (fresh install) app to my liking to get CachyOS KDE ready for my personal use.
│   │   ├── bootstrap.py     # System preparation page
│   │   ├── packages.py      # Package selection grid
│   │   ├── extras.py        # Configuration extras
│   │   ├── progress.py      # Live installation tracking
│   │   └── summary.py       # Deployment report
│   └── resources/
│       └── style.css        # Premium dark theme CSS
├── bin/
│   └── ckdeps     # CLI entry point
├── data/
│   ├── com.goodborn.architect.desktop
│   ├── com.goodborn.architect.svg
│   └── com.goodborn.architect.metainfo.xml
├── Makefile                 # Install/uninstall targets
├── PKGBUILD                 # AUR build recipe
└── .SRCINFO                 # AUR metadata
```

---

## 🎨 Design

- **Dark theme** with purple/blue gradient backgrounds
- **Glassmorphism** effects with frosted glass cards
- **Staggered fade-in** animations on page transitions
- **Live log output** with monospace terminal styling
- Custom scrollbars, switches, and checkboxes matching the theme

---

## 📄 License

GPL-3.0-or-later — see [LICENSE](LICENSE) for details.

---

**Made with 💜 by Goodborn**
