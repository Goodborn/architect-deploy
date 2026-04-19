"""Progress page — animated installation progress with live output."""

import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw, GLib


class ProgressPage(Gtk.Box):
    """Live installation progress page with per-package tracking."""

    def __init__(self, installer, on_complete: callable):
        super().__init__(orientation=Gtk.Orientation.VERTICAL)
        self.add_css_class("progress-container")
        self.installer = installer
        self.on_complete = on_complete
        self._results = []

        # ─── Header ──────────────────────────────────
        title = Gtk.Label(label="Installing Packages")
        title.add_css_class("page-title")
        title.set_halign(Gtk.Align.START)
        self.append(title)

        subtitle = Gtk.Label(label="Sit back while your system is being configured")
        subtitle.add_css_class("page-subtitle")
        subtitle.set_halign(Gtk.Align.START)
        self.append(subtitle)

        # ─── Counter + Current Package ────────────────
        center_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        center_box.set_halign(Gtk.Align.CENTER)
        center_box.set_margin_top(16)
        center_box.set_margin_bottom(12)

        self._counter_label = Gtk.Label(label="0 / 0")
        self._counter_label.add_css_class("progress-counter")
        center_box.append(self._counter_label)

        progress_label = Gtk.Label(label="PACKAGES")
        progress_label.add_css_class("progress-label")
        center_box.append(progress_label)

        self.append(center_box)

        # ─── Current Package Name ─────────────────────
        self._current_pkg_label = Gtk.Label(label="Preparing...")
        self._current_pkg_label.add_css_class("progress-current-pkg")
        self._current_pkg_label.set_halign(Gtk.Align.CENTER)
        self.append(self._current_pkg_label)

        # ─── Overall Progress Bar ─────────────────────
        self._progress_bar = Gtk.ProgressBar()
        self._progress_bar.set_margin_top(12)
        self._progress_bar.set_margin_bottom(8)
        self._progress_bar.add_css_class("progress-overall-bar")
        self._progress_bar.set_show_text(False)
        self.append(self._progress_bar)

        # ─── Status Text ─────────────────────────────
        self._status_label = Gtk.Label(label="Initializing...")
        self._status_label.add_css_class("progress-status")
        self._status_label.set_halign(Gtk.Align.CENTER)
        self.append(self._status_label)

        # ─── Detailed Result List ────────────────────
        self._result_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self._result_box.set_margin_top(12)

        result_scroll = Gtk.ScrolledWindow()
        result_scroll.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        result_scroll.set_vexpand(True)
        result_scroll.set_child(self._result_box)
        self.append(result_scroll)

        self.append(result_scroll)

        # ─── Continue Button (hidden until done) ──────
        self._continue_btn = Gtk.Button(label="Continue to Summary  →")
        self._continue_btn.add_css_class("nav-button-primary")
        self._continue_btn.set_halign(Gtk.Align.END)
        self._continue_btn.set_margin_top(16)
        self._continue_btn.set_visible(False)
        self._continue_btn.connect("clicked", lambda _: self.on_complete(self._results))
        self.append(self._continue_btn)

    def start_installation(self, packages):
        """Begin installing the selected packages."""
        if not packages:
            self._status_label.set_text("No packages to install")
            self._continue_btn.set_visible(True)
            return

        self._total = len(packages)
        self._counter_label.set_text(f"0 / {self._total}")

        self.installer.install_packages_sequential(
            packages=packages,
            on_package_start=self._on_package_start,
            on_output=self._on_output,
            on_package_complete=self._on_package_complete,
            on_all_complete=self._on_all_complete,
        )

    def _on_package_start(self, pkg, index, total):
        """Called when a package installation begins."""
        display = pkg.display_name
        if pkg.source == "flatpak":
            display += " (Flatpak)"

        self._current_pkg_label.set_text(display)
        self._status_label.set_text(f"Installing {display}...")
        self._counter_label.set_text(f"{index + 1} / {total}")

        # Pulse progress
        fraction = index / total
        self._progress_bar.set_fraction(fraction)

    def _on_output(self, line):
        """Send output to global log."""
        window = self.get_root()
        if hasattr(window, "append_log"):
            window.append_log(line)

    def _on_package_complete(self, pkg, status, index, total):
        """Called when a package finishes installing."""
        self._results.append((pkg, status))

        # Create detailed result card
        row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=16)
        row.add_css_class("package-card")
        row.set_margin_start(4)
        row.set_margin_end(4)

        # Status icon
        if status == "installed":
            icon_text = "✓"
            css_class = "status-installed"
        elif status == "skipped":
            icon_text = "↷"
            css_class = "status-skipped"
        else:
            icon_text = "✗"
            css_class = "status-failed"

        icon = Gtk.Label(label=icon_text)
        icon.add_css_class(css_class)
        icon.set_valign(Gtk.Align.CENTER)
        row.append(icon)

        # Package icon
        pkg_icon = Gtk.Image()
        pkg_icon.set_pixel_size(32)
        pkg_icon.set_valign(Gtk.Align.CENTER)
        pkg_icon.set_from_icon_name(pkg.icon_name)
        row.append(pkg_icon)

        # Info Box (Name + Description)
        info_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        info_box.set_valign(Gtk.Align.CENTER)
        info_box.set_hexpand(True)

        name = Gtk.Label(label=pkg.display_name)
        name.add_css_class("summary-pkg-name")
        name.set_halign(Gtk.Align.START)
        info_box.append(name)

        desc = Gtk.Label(label=pkg.description)
        desc.add_css_class("package-desc")
        desc.set_halign(Gtk.Align.START)
        info_box.append(desc)
        row.append(info_box)

        # Right side box (Source + Status)
        right_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        right_box.set_valign(Gtk.Align.CENTER)

        status_label = Gtk.Label(label=status.upper())
        status_label.add_css_class(css_class)
        status_label.set_halign(Gtk.Align.END)
        right_box.append(status_label)

        source_badge = Gtk.Label(label="AUR" if pkg.source == "aur" else "FLATPAK")
        source_badge.add_css_class("package-source-badge")
        source_badge.add_css_class("badge-aur" if pkg.source == "aur" else "badge-flatpak")
        source_badge.set_halign(Gtk.Align.END)
        right_box.append(source_badge)

        row.append(right_box)

        self._result_box.append(row)

        # Update progress
        fraction = (index + 1) / total
        self._progress_bar.set_fraction(fraction)

    def _on_all_complete(self, results):
        """Called when all packages are done."""
        self._results = results
        self._progress_bar.set_fraction(1.0)
        self._current_pkg_label.set_text("Complete!")
        self._status_label.set_text(
            f"✨ {len(results)} packages processed"
        )
        self._continue_btn.set_visible(True)
