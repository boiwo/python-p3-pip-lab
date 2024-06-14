
import requests
import pytest

def requests_version():
    return requests.__version__

def pytest_version():
    return pytest.__version__

def test_requests_version():
    assert requests_version() == "2.22.0"  # Update expected version to "2.22.0"

def test_pytest_version():
    assert pytest_version() == "8.2.2"  # Update expected version to "8.2.2"

