import tsm
import pytest


def test_get_main_page():
    html = tsm.get_main_page(40972890)
    assert(html.startswith("<!DOCTYPE html>"))


def test_get_main_page_fail():
    with pytest.raises(AssertionError) as e_info:
        html = tsm.get_main_page(None)


def test_get_main_page_channel_not_found():
    with pytest.raises(Exception) as e_info:
        html = tsm.get_main_page(0)
