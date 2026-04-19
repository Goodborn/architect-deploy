"""Allow running as `python -m architect_deploy`."""

from .main import main
import sys

sys.exit(main())
