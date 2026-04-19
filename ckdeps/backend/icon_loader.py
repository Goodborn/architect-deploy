import threading
import urllib.request
import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, GdkPixbuf, GLib, Gio

class IconLoader:
    def __init__(self):
        self._cache = {}

    def load_icon_async(self, url: str, fallback_icon_name: str, size: int, callback):
        """Asynchronously loads an icon from a URL and calls the callback with a Pixbuf/Texture."""
        if url in self._cache:
            GLib.idle_add(callback, self._cache[url])
            return

        def _work():
            try:
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=5) as response:
                    data = response.read()
                
                # Load image from bytes
                bytes_data = GLib.Bytes.new(data)
                stream = Gio.MemoryInputStream.new_from_bytes(bytes_data)
                pixbuf = GdkPixbuf.Pixbuf.new_from_stream_at_scale(stream, size, size, True, None)
                
                self._cache[url] = pixbuf
                GLib.idle_add(callback, pixbuf)
            except Exception as e:
                print(f"Failed to load icon from {url}: {e}")
                GLib.idle_add(callback, None)

        threading.Thread(target=_work, daemon=True).start()

icon_loader = IconLoader()
