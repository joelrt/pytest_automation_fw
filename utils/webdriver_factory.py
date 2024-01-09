# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from settings import WAIT


class WebDriverFactory:

    def __init__(self, **kwargs):
        self.driver = None
        self.test_name = kwargs.get("test_name", "")
        self.environment = ""
        if kwargs:
            self.kwargs = kwargs
            self.browser_name = kwargs["browser"]
            self.on_localhost = kwargs["localhost"]

    def get_driver(self):
        if self.on_localhost:
            return self.get_local_web_driver()
        else:
            raise "None Browser has been selected"

    def get_local_web_driver(self):
        path = '/drivers/'       
        if self.browser_name == 'chrome':
            options = Options()
            options.binary_location = path + "chromedriver"
            options.page_load_strategy = 'eager'
            self.driver = webdriver.Chrome(options=options)

        else:
            self.driver = WebDriverFactory(**self.kwargs).get_local_web_driver()

        self.driver.implicitly_wait(WAIT)
        self.driver.maximize_window()
        self.environment = "local"
        return self.driver
