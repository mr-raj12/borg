"""Backward compatibility stub — import from borg.legacy.repository instead.

This stub will be removed in a future release.
"""

from .legacy.repository import *  # noqa: F401,F403
from .legacy.repository import LegacyRepository  # noqa: F401 — explicit re-export
from .legacy.repository import LoggedIO  # noqa: F401 — used by tests
from .legacy.repository import MAGIC, MAX_DATA_SIZE, TAG_DELETE, TAG_PUT2, TAG_PUT, TAG_COMMIT  # noqa: F401
