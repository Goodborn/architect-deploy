"""Architect Deploy — Application entry point."""

import sys
import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw, Gio, GLib

from . import __app_id__, __version__
from .window import ArchitectWindow


class ArchitectApp(Adw.Application):
    """Main GTK4/Adwaita application."""

    def __init__(self):
        super().__init__(
            application_id=__app_id__,
            flags=Gio.ApplicationFlags.DEFAULT_FLAGS,
        )

    def do_activate(self):
        """Create and show the main window."""
        # Correct way to set dark theme in Libadwaita
        style_manager = Adw.StyleManager.get_default()
        style_manager.set_color_scheme(Adw.ColorScheme.PREFER_DARK)

        win = self.props.active_window
        if not win:
            win = ArchitectWindow(self)
        win.present()

    def do_startup(self):
        """Called when the application starts."""
        Adw.Application.do_startup(self)

        # Force dark theme via Adwaita's StyleManager (correct API)
        style_manager = Adw.StyleManager.get_default()
        style_manager.set_color_scheme(Adw.ColorScheme.FORCE_DARK)

        # About action
        about_action = Gio.SimpleAction.new("about", None)
        about_action.connect("activate", self._on_about)
        self.add_action(about_action)

        # Quit action
        quit_action = Gio.SimpleAction.new("quit", None)
        quit_action.connect("activate", lambda *_: self.quit())
        self.add_action(quit_action)
        self.set_accels_for_action("app.quit", ["<Control>q"])

    def _on_about(self, *_args):
        """Show about dialog."""
        about = Adw.AboutWindow(
            transient_for=self.props.active_window,
            application_name="Architect Deploy",
            application_icon="com.goodborn.architect",
            developer_name="Goodborn",
            version=__version__,
            developers=["Goodborn"],
            copyright="© 2026 Goodborn",
            license_type=Gtk.License.GPL_3_0,
            website="https://github.com/goodborn/architect-deploy",
            issue_url="https://github.com/goodborn/architect-deploy/issues",
            comments="Beautiful CachyOS system deployment wizard.\n"
                     "Install packages, configure extras, and bootstrap your system.",
        )
        about.present()


def main():
    """Application main entry point."""
    app = ArchitectApp()
    return app.run(sys.argv)


if __name__ == "__main__":
    sys.exit(main())
