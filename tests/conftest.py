"""Fixtures for all tests for the WTDpy package."""

import os

import pytest

from wtdpy import WTDpy


@pytest.fixture
def wtdpy():
    """Return an initialised WTDpy class."""

    return WTDpy(api_token=os.environ["api_key"])
