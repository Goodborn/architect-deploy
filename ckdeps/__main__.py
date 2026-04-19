"""Allow running as `python -m ckdeps`."""

from .main import main
import sys

sys.exit(main())
