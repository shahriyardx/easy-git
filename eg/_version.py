from collections import namedtuple

__version__ = "1.0.0"
VersionInfo = namedtuple("VersionInfo", "major minor macro release")
version_info = VersionInfo(*__version__.split("."), "stable")
