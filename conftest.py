import pytest
from selenium import webdriver

@pytest.fixture(params=[True, False])
def button_top(request):
    return request.param