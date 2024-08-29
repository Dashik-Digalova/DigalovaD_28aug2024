import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def auth_token():
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjUwMjE0NTIsImlhdCI6MTcyNDg1MzQ1MiwiaXNzIjoiL2FwaS92MS9hd" \
            "XRoL2Fub255bW91cyIsInN1YiI6IjFmYWRiNjk1ZmRmMTVmZGJkYWViNTU0NTFjYmNjZDQ0Njc3M2FmYWIyMzdkOTg4NzBjMWQwODU2ZDk" \
            "0MjY0N2EiLCJ0eXBlIjoxMH0.Xp2BiutEtfv6HPH3P5onKIuTsI4NIpBSJavLs1M7anA"
    return token
