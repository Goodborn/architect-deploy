# 🚀 Architect Deploy

**A personal collection of custom system tweaks and package selections for CachyOS / Arch Linux**

Architect is a tailored companion for my fresh-install workflow. It provides a guided, animated GUI wizard to bootstrap my system, install my preferred AUR and Flatpak packages, and apply my specific configuration extras.

![Architect Deploy](https://img.shields.io/badge/GTK4-Adwaita-a855f7?style=for-the-badge)
![License](https://img.shields.io/badge/license-GPL--3.0-green?style=for-the-badge)
![Arch](https://img.shields.io/badge/CachyOS-Arch_Linux-1793d1?style=for-the-badge)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📦 **Smart Packages** | Personalized list of AUR + Flatpak apps |
| ⚡ **One-Click Bootstrap** | Automates system updates and manager setup |
| 🎨 **Personal Tweaks** | Custom aliases, privacy settings, and app configs |
| 📊 **Live Progress** | Real-time installation tracking with log output |
| 🛡️ **Privacy First** | Tweaks to disable tracking and secure your setup |

## 📋 Package List

### AUR / Pacman
thefuck, fzf, atuin, zoxide, bazaar, hyprsunset, anydesk-bin, foliate,
libreoffice-still, betterbird, bolt-launcher, haruna, popcorntime,
vmware-workstation, vmware-keymaps, qbittorrent, vesktop, obs-studio,
visual-studio-code-bin, proton-vpn-gtk-app, solaar, harmonoid, brave-bin, eden

### Flatpak
Spotify, Kdenlive, Upscayl, Blanket, Cozy

---

## 🔧 Installation

### ⚡ Quick Start (Arch / CachyOS)
Copy and paste this block to install and launch:
```bash
git clone https://github.com/goodborn/architect-deploy.git && \
cd architect-deploy && \
sudo make install && \
(architect-deploy & disown) && exit
```

### 🚀 How to Run
After installing, you can launch the app anytime by:
1. Typing `architect-deploy` in your terminal.
2. Searching for **"Architect"** in your application menu.
3. Running `make run` inside the project folder.

### 📦 From AUR (Recommended)
If you prefer using an AUR helper like `yay`:
```bash
yay -S architect-deploy
```

### 🛠️ Run from Source (Development)
To test changes without installing to your system:
```bash
git clone https://github.com/goodborn/architect-deploy.git
cd architect-deploy
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
architect-deploy/
├── architect_deploy/
│   ├── __init__.py          # Package metadata
│   ├── main.py              # Application entry point
│   ├── window.py            # Main window + page navigation
│   ├── backend/
│   │   ├── installer.py     # Threaded shell command execution
│   │   └── package_data.py  # Package & extras definitions
│   ├── pages/
│   │   ├── welcome.py       # Animated welcome screen
│   │   ├── bootstrap.py     # System preparation page
│   │   ├── packages.py      # Package selection grid
│   │   ├── extras.py        # Configuration extras
│   │   ├── progress.py      # Live installation tracking
│   │   └── summary.py       # Deployment report
│   └── resources/
│       └── style.css        # Premium dark theme CSS
├── bin/
│   └── architect-deploy     # CLI entry point
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
