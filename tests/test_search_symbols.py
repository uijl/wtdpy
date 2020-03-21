from datetime import datetime

import pandas as pd
import pytest


@pytest.fixture
def wtdpy():
    import os
    from wtdpy import WTDpy

    return WTDpy(api_token=os.environ["api_key"])


@pytest.mark.parametrize("symbol", [["^AEX"], ["^AEX", "^DAX"]])
def test_search_symbols(symbol, wtdpy):
    """Test search request without additional data"""

    # Symbols are correct so should return `True`
    assert wtdpy.search_available_data(symbol)


@pytest.mark.parametrize("symbol", [["AEX"], ["AEX", "DAX"]])
def test_search_symbols_list_alternative(symbol, wtdpy):
    """Test search request without additional data"""

    # The provided symbols will not be found, return an alternative
    response = wtdpy.search_available_data(symbol, list_alternatives=True)
    assert len(symbol) == len(response)


@pytest.mark.parametrize("symbol", [["AEX"], ["AEX", "DAX"]])
def test_search_symbols_list_alternatives(symbol, wtdpy):
    """Test search request without additional data"""

    # The provided symbols will not be found, return 5 alternatives
    number_of_alternatives = 5
    response = wtdpy.search_available_data(
        symbol, list_alternatives=True, number_of_alternatives=number_of_alternatives
    )

    assert len(symbol) * number_of_alternatives == len(response)
