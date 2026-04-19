# Maintainer: Goodborn <goodborn@users.noreply.github.com>
# Local PKGBUILD — install from current directory (for testing)
pkgname=architect-deploy
pkgver=1.0.0
pkgrel=1
pkgdesc="Beautiful GTK4 system deployment wizard for CachyOS / Arch Linux"
arch=('any')
url="https://github.com/goodborn/architect-deploy"
license=('GPL-3.0-or-later')
depends=(
    'python'
    'python-gobject'
    'gtk4'
    'libadwaita'
    'flatpak'
    'pacman'
)
optdepends=(
    'yay: AUR package installation support'
    'paru: Alternative AUR helper'
)

package() {
    cd "${startdir}"
    make DESTDIR="${pkgdir}" install
}
