# -*- coding: utf-8 -*-

from urllib.error import URLError

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.common.exceptions import WebDriverException

from settings import DEFAULT_BROWSER
from utils.webdriver_factory import WebDriverFactory


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--headless", action="store_true", help="Execute tests on headless mode")
    parser.addoption("--localhost", action="store_true", help="Execute tests on localhost")


@pytest.fixture(scope="function")
def setup(request):
    custom_setup = {}
    kwargs = {
        "browser": DEFAULT_BROWSER,
        "localhost": False,
        "headless": False,
    }

    if hasattr(request, "param"):
        kwargs["browser"] = request.param
    if request.config.getoption("localhost"):
        kwargs["localhost"] = True
    if request.config.getoption("headless"):
        kwargs["headless"] = True
    if request.config.getoption("browser"):
        kwargs["browser"] = request.config.getoption("browser")

    kwargs["test_name"] = str(request.node.name)
    setup.f = web_driver_factory = WebDriverFactory(**kwargs)
    setup.a = web_driver = web_driver_factory.get_driver()
    custom_setup["driver"] = web_driver
    custom_setup["web_driver_factory"] = web_driver_factory
    custom_setup["test_name"] = kwargs["test_name"]
    yield custom_setup

    if web_driver is not None:
        try:
            web_driver.quit()
        except WebDriverException as e:
            if "Session not started or terminated" in str(e):
                pass
            else:
                raise e
        except URLError as e:
            if "urlopen error time out" in str(e):
                pass
            else:
                raise e


def screenshot(driver, tc_name):
    allure.attach(
        driver.get_screenshot_as_png(),
        name=tc_name,
        attachment_type=AttachmentType.PNG,
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call":
        try:
            if rep.failed:
                screenshot(setup.a, rep.nodeid.split("::")[-1])
        except:
            pass

