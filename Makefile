PREFIX ?= /usr
DESTDIR ?=
LIBDIR = $(PREFIX)/lib/architect-deploy
BINDIR = $(PREFIX)/bin
DATADIR = $(PREFIX)/share
ICONDIR = $(DATADIR)/icons/hicolor/scalable/apps
APPDIR = $(DATADIR)/applications
METADIR = $(DATADIR)/metainfo
CSSDIR = $(DATADIR)/architect-deploy

.PHONY: install uninstall deps

deps:
	# Install system dependencies if pacman is available (Arch/CachyOS)
	@if command -v pacman > /dev/null; then \
		echo "📦 Installing system dependencies..."; \
		pacman -S --needed --noconfirm python-gobject gtk4 libadwaita flatpak librsvg; \
	fi

install: deps
	# Install Python package
	install -dm755 "$(DESTDIR)$(LIBDIR)/architect_deploy"
	install -dm755 "$(DESTDIR)$(LIBDIR)/architect_deploy/backend"
	install -dm755 "$(DESTDIR)$(LIBDIR)/architect_deploy/pages"
	install -dm755 "$(DESTDIR)$(LIBDIR)/architect_deploy/resources"
	install -Dm644 architect_deploy/__init__.py "$(DESTDIR)$(LIBDIR)/architect_deploy/__init__.py"
	install -Dm644 architect_deploy/main.py "$(DESTDIR)$(LIBDIR)/architect_deploy/main.py"
	install -Dm644 architect_deploy/window.py "$(DESTDIR)$(LIBDIR)/architect_deploy/window.py"
	install -Dm644 architect_deploy/backend/__init__.py "$(DESTDIR)$(LIBDIR)/architect_deploy/backend/__init__.py"
	install -Dm644 architect_deploy/backend/installer.py "$(DESTDIR)$(LIBDIR)/architect_deploy/backend/installer.py"
	install -Dm644 architect_deploy/backend/package_data.py "$(DESTDIR)$(LIBDIR)/architect_deploy/backend/package_data.py"
	install -Dm644 architect_deploy/backend/icon_loader.py "$(DESTDIR)$(LIBDIR)/architect_deploy/backend/icon_loader.py"
	install -Dm644 architect_deploy/pages/__init__.py "$(DESTDIR)$(LIBDIR)/architect_deploy/pages/__init__.py"
	install -Dm644 architect_deploy/pages/splash.py "$(DESTDIR)$(LIBDIR)/architect_deploy/pages/splash.py"
	install -Dm644 architect_deploy/pages/welcome.py "$(DESTDIR)$(LIBDIR)/architect_deploy/pages/welcome.py"
	install -Dm644 architect_deploy/pages/bootstrap.py "$(DESTDIR)$(LIBDIR)/architect_deploy/pages/bootstrap.py"
	install -Dm644 architect_deploy/pages/packages.py "$(DESTDIR)$(LIBDIR)/architect_deploy/pages/packages.py"
	install -Dm644 architect_deploy/pages/extras.py "$(DESTDIR)$(LIBDIR)/architect_deploy/pages/extras.py"
	install -Dm644 architect_deploy/pages/progress.py "$(DESTDIR)$(LIBDIR)/architect_deploy/pages/progress.py"
	install -Dm644 architect_deploy/pages/summary.py "$(DESTDIR)$(LIBDIR)/architect_deploy/pages/summary.py"

	# Install CSS
	install -Dm644 architect_deploy/resources/style.css "$(DESTDIR)$(CSSDIR)/style.css"

	# Install binary
	install -Dm755 bin/architect-deploy "$(DESTDIR)$(BINDIR)/architect-deploy"

	# Install desktop file
	install -Dm644 data/com.goodborn.architect.desktop "$(DESTDIR)$(APPDIR)/com.goodborn.architect.desktop"

	# Install icon
	install -Dm644 data/com.goodborn.architect.svg "$(DESTDIR)$(ICONDIR)/com.goodborn.architect.svg"

	# Install metainfo
	install -Dm644 data/com.goodborn.architect.metainfo.xml "$(DESTDIR)$(METADIR)/com.goodborn.architect.metainfo.xml"

uninstall:
	rm -rf "$(DESTDIR)$(LIBDIR)"
	rm -f  "$(DESTDIR)$(BINDIR)/architect-deploy"
	rm -f  "$(DESTDIR)$(APPDIR)/com.goodborn.architect.desktop"
	rm -f  "$(DESTDIR)$(ICONDIR)/com.goodborn.architect.svg"
	rm -f  "$(DESTDIR)$(METADIR)/com.goodborn.architect.metainfo.xml"
	rm -f  "$(DESTDIR)$(CSSDIR)/style.css"
	rmdir --ignore-fail-on-non-empty "$(DESTDIR)$(CSSDIR)" 2>/dev/null || true

run:
	python3 -m architect_deploy
