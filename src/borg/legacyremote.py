"""Backward compatibility stub — import from borg.legacy.remote instead.

This stub will be removed in a future release.
"""

from .legacy.remote import *  # noqa: F401,F403
from .legacy.remote import LegacyRemoteRepository  # noqa: F401 — explicit re-export
from .legacy.remote import InvalidRPCMethod, PathNotAllowed  # noqa: F401 — used by tests
