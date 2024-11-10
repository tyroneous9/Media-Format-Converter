import pytest
from dl import *

def test_successful_download():
    links = ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"]
    path = "/some/path"
    failed_links = download_audio(links, path)
    assert len(failed_links) == 0  # No failed links should be returned

def test_invalid_link():
    links = ["invalid_url"]
    path = "/some/path"
    failed_links = download_audio(links, path)
    assert len(failed_links) > 0  # The invalid link should be added to failed_links
