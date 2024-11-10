import pytest
from dl import *

def test_video_download():
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    result = download_video(url)
    assert result is not None  # or other conditions based on expected behavior

def test_invalid_url():
    url = "invalid_url"
    with pytest.raises(ValueError):  # Adjust based on how your code handles invalid URLs
        download_video(url)
