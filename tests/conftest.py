import pytest
from selene import browser


@pytest.fixture(autouse=True)
def browser_size():
    browser.config.window_width = 2020
    browser.config.window_height = 800
    browser.open('https://github.com/')
    yield
    browser.quit()
