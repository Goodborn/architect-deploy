"""Package definitions for Architect Deploy."""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Package:
    """Represents a single installable package."""
    name: str
    display_name: str
    description: str
    icon_name: str
    category: str
    source: str  # "aur" or "flatpak"
    domain: Optional[str] = None
    flatpak_id: Optional[str] = None
    installed: bool = False
    selected: bool = False


@dataclass
class ExtraConfig:
    """Represents a system configuration extra."""
    key: str
    title: str
    description: str
    icon_name: str
    selected: bool = False
    status: str = ""


# ---------- AUR / Pacman Packages ----------
AUR_PACKAGES = [
    Package("thefuck", "TheFuck", "Corrects console commands", "utilities-terminal", "Terminal Tools", "aur", domain="github.com"),
    Package("fzf", "FZF", "Fuzzy finder for the terminal", "edit-find", "Terminal Tools", "aur", domain="github.com"),
    Package("atuin", "Atuin", "Magical shell history manager", "appointment-soon", "Terminal Tools", "aur", domain=None),
    Package("zoxide", "Zoxide", "Smarter cd command", "folder", "Terminal Tools", "aur", domain="github.com"),
    Package("bazaar", "Bazaar", "Version control system", "git", "Terminal Tools", "aur", domain="gnu.org"),
    Package("anydesk-bin", "AnyDesk", "Remote desktop", "preferences-desktop-remote-desktop", "Remote & Networking", "aur", domain=None),
    Package("foliate", "Foliate", "Modern e-book reader", "x-office-document", "Productivity", "aur", domain=None),
    Package("libreoffice-still", "LibreOffice", "Office suite", "libreoffice-main", "Productivity", "aur", domain="libreoffice.org"),
    Package("betterbird", "Betterbird", "Email client", "mail-client", "Productivity", "aur", domain="betterbird.eu"),
    Package("bolt-launcher", "Bolt Launcher", "RuneScape launcher", "applications-games", "Gaming", "aur", domain="runescape.com"),
    Package("haruna", "Haruna", "KDE media player", "haruna", "Media", "aur", domain="haruna.kde.org"),
    Package("popcorntime", "Popcorn Time", "Stream movies", "video-display", "Media", "aur", domain="popcorntime.app"),
    Package("vmware-workstation", "VMware Workstation", "Virtual machine platform", "computer", "Development", "aur", domain="vmware.com"),
    Package("vmware-keymaps", "VMware Keymaps", "Keyboard mappings for VMware", "input-keyboard", "Development", "aur", domain="vmware.com"),
    Package("qbittorrent", "qBittorrent", "BitTorrent client", "qbittorrent", "Networking", "aur", domain="qbittorrent.org"),
    Package("vesktop", "Vesktop", "Custom Discord client", "internet-chat", "Communication", "aur", domain="discord.com"),
    Package("obs-studio", "OBS Studio", "Live streaming", "obs", "Media", "aur", domain="obsproject.com"),
    Package("visual-studio-code-bin", "VS Code", "Modern code editor", "visual-studio-code", "Development", "aur", domain="code.visualstudio.com"),
    Package("proton-vpn-gtk-app", "Proton VPN", "Secure VPN application", "network-vpn", "Networking", "aur", domain="protonvpn.com"),
    Package("harmonoid", "Harmonoid", "Beautiful music player", "multimedia-audio-player", "Media", "aur", domain="harmonoid.com"),
    Package("brave-bin", "Brave Browser", "Privacy-focused web browser", "brave-browser", "Internet", "aur", domain="brave.com"),
    Package("firefox", "Firefox", "Fast, private, and open-source web browser", "firefox", "Internet", "aur", domain="firefox.com"),
    Package("eden", "Eden", "Modern development tool", "applications-development", "Development", "aur", domain="github.com"),
]

# ---------- Flatpak Packages ----------
FLATPAK_PACKAGES = [
    Package("spotify", "Spotify", "Music streaming service", "com.spotify.Client", "Media", "flatpak", domain="spotify.com",
            flatpak_id="com.spotify.Client"),
    Package("kdenlive", "Kdenlive", "Professional video editor", "org.kde.kdenlive", "Media", "flatpak", domain="kdenlive.org",
            flatpak_id="org.kde.kdenlive"),
    Package("upscayl", "Upscayl", "AI image upscaler", "org.upscayl.Upscayl", "Media", "flatpak", domain="upscayl.org",
            flatpak_id="org.upscayl.Upscayl"),
    Package("blanket", "Blanket", "Ambient sound player", "com.rafaelmardojai.Blanket", "Media", "flatpak", domain=None,
            flatpak_id="com.rafaelmardojai.Blanket"),
    Package("cozy", "Cozy", "Audiobook player", "com.github.geigi.cozy", "Media", "flatpak", domain=None,
            flatpak_id="com.github.geigi.cozy"),
]

ALL_PACKAGES = AUR_PACKAGES + FLATPAK_PACKAGES

# ---------- Extras ----------
EXTRAS = [
    ExtraConfig("aliases", "Custom Aliases", "Install ~/CustomScripts/aliases.zsh with useful shortcuts",
                "utilities-terminal"),
    ExtraConfig("haruna_folders", "Haruna Folders", "Create playlist/resume support directories",
                "folder-videos"),
    ExtraConfig("disable_recent", "Disable Recent Files", "Turn off GNOME recent file tracking for privacy",
                "preferences-system-privacy"),
]

# ---------- Category Colors (for UI) ----------
CATEGORY_COLORS = {
    "Terminal Tools": "#a855f7",
    "Desktop": "#6366f1",
    "Remote & Networking": "#0ea5e9",
    "Productivity": "#10b981",
    "Gaming": "#f59e0b",
    "Media": "#ec4899",
    "Development": "#8b5cf6",
    "Networking": "#06b6d4",
    "Communication": "#6366f1",
    "Hardware": "#f97316",
    "Internet": "#ef4444",
}
