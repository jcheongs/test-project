"""
Unit and regression test for the test_project package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import test_project


def test_test_project_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "test_project" in sys.modules
