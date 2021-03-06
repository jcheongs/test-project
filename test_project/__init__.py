"""Test project using cookie cutter"""

# Add imports here
from .test_project import *
from .temp_conversion import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
