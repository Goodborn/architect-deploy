"""Bootstrap page — system preparation with live progress."""

import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw, GLib


BOOTSTRAP_STEPS = [
    ("System Update", "Running pacman -Syu to update all packages"),
    ("Base Dependencies", "Installing git, base-devel, and flatpak"),
    ("Yay AUR Helper", "Ensuring the AUR helper is available"),
    ("Flathub Repository", "Adding the Flathub remote for Flatpak"),
]


class BootstrapPage(Gtk.Box):
    """System bootstrap page with live step tracking and log output."""

    def __init__(self, installer, on_complete: callable):
        super().__init__(orientation=Gtk.Orientation.VERTICAL)
        self.add_css_class("page-container")
        self.installer = installer
        self.on_complete = on_complete
        self._step_rows = []
        self._complete = False

        # ─── Header ──────────────────────────────────
        title = Gtk.Label(label="System Bootstrap")
        title.add_css_class("page-title")
        title.set_halign(Gtk.Align.START)
        self.append(title)

        subtitle = Gtk.Label(label="Preparing your system for deployment")
        subtitle.add_css_class("page-subtitle")
        subtitle.set_halign(Gtk.Align.START)
        self.append(subtitle)

        # ─── Steps List ──────────────────────────────
        steps_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        steps_box.set_margin_bottom(16)

        for i, (name, desc) in enumerate(BOOTSTRAP_STEPS):
            row = self._create_step_row(name, desc, i)
            steps_box.append(row)

        self.append(steps_box)

        # ─── Spinner + Status ────────────────────────
        status_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        status_box.set_halign(Gtk.Align.CENTER)
        status_box.set_margin_top(8)
        status_box.set_margin_bottom(12)

        self._spinner = Gtk.Spinner()
        self._spinner.add_css_class("spinner-large")
        self._spinner.set_spinning(True)
        status_box.append(self._spinner)

        self._status_label = Gtk.Label(label="Initializing...")
        self._status_label.add_css_class("progress-status")
        status_box.append(self._status_label)

        self.append(status_box)

        # ─── Continue Button (hidden until done) ─────
        self._continue_btn = Gtk.Button(label="Continue  →")
        self._continue_btn.add_css_class("nav-button-primary")
        self._continue_btn.set_halign(Gtk.Align.END)
        self._continue_btn.set_margin_top(16)
        self._continue_btn.set_visible(False)
        self._continue_btn.connect("clicked", lambda _: self.on_complete())
        self.append(self._continue_btn)

    def _create_step_row(self, name, desc, index):
        """Create a single bootstrap step row."""
        row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        row.add_css_class("bootstrap-step")
        row.add_css_class("bootstrap-step-pending")

        # Step number
        num = Gtk.Label(label=f"{index + 1}")
        num.set_size_request(28, 28)
        num.add_css_class("step-status")
        row.append(num)

        # Info
        info_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        info_box.set_hexpand(True)

        title = Gtk.Label(label=name)
        title.add_css_class("step-title")
        title.add_css_class("step-title-pending")
        title.set_halign(Gtk.Align.START)
        info_box.append(title)

        description = Gtk.Label(label=desc)
        description.add_css_class("feature-desc")
        description.set_halign(Gtk.Align.START)
        info_box.append(description)

        row.append(info_box)

        # Status indicator
        status = Gtk.Label(label="⏳")
        status.add_css_class("step-status")
        row.append(status)

        self._step_rows.append({
            "row": row,
            "title": title,
            "status": status,
            "num": num,
        })

        return row

    def start_bootstrap(self):
        """Begin the bootstrap process."""
        self.installer.bootstrap_system(
            on_step=self._on_step,
            on_output=self._on_output,
            on_complete=self._on_all_complete,
        )

    def _on_step(self, message, step_index):
        """Called when a new bootstrap step begins."""
        self._status_label.set_text(message)

        # Update previous step as done
        if step_index > 0:
            prev = self._step_rows[step_index - 1]
            prev["row"].remove_css_class("bootstrap-step-active")
            prev["row"].add_css_class("bootstrap-step-done")
            prev["title"].remove_css_class("step-title-active")
            prev["title"].add_css_class("step-title-done")
            prev["status"].set_text("✓")

        # Mark current step as active
        if step_index < len(self._step_rows):
            current = self._step_rows[step_index]
            current["row"].remove_css_class("bootstrap-step-pending")
            current["row"].add_css_class("bootstrap-step-active")
            current["title"].remove_css_class("step-title-pending")
            current["title"].add_css_class("step-title-active")
            current["status"].set_text("⚙️")

    def _on_output(self, line):
        """Send output to global log."""
        window = self.get_root()
        if hasattr(window, "append_log"):
            window.append_log(line)

    def _on_all_complete(self, results):
        """Called when all bootstrap steps are done."""
        self._spinner.set_spinning(False)
        self._spinner.set_visible(False)

        # Mark final step
        if self._step_rows:
            last = self._step_rows[-1]
            last["row"].remove_css_class("bootstrap-step-active")
            last["row"].add_css_class("bootstrap-step-done")
            last["title"].remove_css_class("step-title-active")
            last["title"].add_css_class("step-title-done")
            last["status"].set_text("✓")

        # Check results
        all_ok = all(s for _, s in results)
        if all_ok:
            self._status_label.set_text("✨ System bootstrap complete!")
        else:
            failed = [n for n, s in results if not s]
            self._status_label.set_text(f"⚠ Some steps had issues: {', '.join(failed)}")

        self._continue_btn.set_visible(True)
        self._complete = True
