from datetime import datetime

import pandas as pd
import pytest


@pytest.fixture
def wtdpy():
    import os
    from wtdpy import WTDpy

    return WTDpy(api_token=os.environ["api_key"])


@pytest.mark.parametrize(
    "symbol", [["Apple Computers"], ["Apple Computers", "Microsoft"]]
)
def test_search(symbol, wtdpy):
    """Test search request without additional data"""

    # Symbols are correct so should return `True`
    response = wtdpy.search(symbol)
    assert len(symbol) == len(response)


@pytest.mark.parametrize(
    "symbol", [["Apple Computers"], ["Apple Computers", "Microsoft"]]
)
def test_search_extended_hits(symbol, wtdpy):
    """Test search request and extend the number of returned hits"""

    # The provided symbols will not be found, return an alternative
    number_of_hits = 10
    response = wtdpy.search(symbol, number_of_hits=number_of_hits)

    for ix, key in enumerate(response.keys()):
        assert key == symbol[ix]
        assert len(response[key]) == number_of_hits
