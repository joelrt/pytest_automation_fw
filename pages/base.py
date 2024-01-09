# -*- coding: utf-8 -*-
import random
import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.common.exceptions import (
    WebDriverException,
    UnexpectedAlertPresentException,
    NoAlertPresentException)
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from settings import WAIT, BASE_URL
from utils.webdriver_factory import WebDriverFactory


class Base(WebDriverFactory):
    main_window = ''

    def __init__(self, setup):
        WebDriverFactory.__init__(self)
        self.driver = setup['driver']

    @allure.step
    def go_page(self, base=BASE_URL, url=""):
        self.driver.get(base + url)
        self.wait_for_complete()

    @allure.step
    def wait_for_complete(self, timeout=WAIT):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

    @allure.step
    def refresh_page(self, timeout=WAIT):
        self.driver.refresh()
        self.wait_for_complete()

    @allure.step
    def waiting_page_by_title(self, title, timeout=WAIT):
        try:
            assert WebDriverWait(self.driver, timeout).until(
                lambda driver: title in driver.execute_script(
                    "return document.title"))
        except WebDriverException:
            pytest.fail(f"{title} =/= {self.current_title()}", True)
    
    @allure.step
    def elements_visible(self, locator, wait=WAIT):
        return WebDriverWait(self.driver, wait).until(ec.visibility_of_any_elements_located(locator))        

    @allure.step
    def verify_element_present(self, locator, wait=3):
        try:
            self.elements_visible(locator, wait)
            return True 
        except:
            return False
        
    @allure.step
    def visible(self, locator, wait=3):
        return WebDriverWait(self.driver, wait).until(ec.presence_of_element_located(locator))
    
    @allure.step
    def clickable(self, locator, wait=3):
        return WebDriverWait(self.driver, wait).until(ec.element_to_be_clickable(locator))
    
    @allure.step
    def get_element(self, locator, wait=3):
        try:
            return self.visible(locator, wait)
        except Exception:
            pytest.fail(f"Element {locator} is not retrieved")

    def get_elements(self, locator, wait=3):
        try:
            return self.elements_visible(locator=locator, wait=wait)
        except Exception:
            pytest.fail(f"Elements {locator} are not retrieved")

    
    @allure.step
    def verify_element_clickable(self, locator, wait=3):
        try:
            self.clickable(locator, wait)
            return True 
        except:
            return False
    
    @allure.step
    def click_on_element_obj(self, element):
        try:
            element.click()
        except Exception:
            pytest.fail(f"Error clicking element")


    @allure.step
    def click_on_element(self, locator, wait=3):
        if self.verify_element_clickable(locator, wait=wait):
            element = self.get_element(locator=locator, wait=wait)
            self.click_on_element_obj(element=element)
        else:
            self.failure_msj("Element is not clickable!!")

    @staticmethod
    @allure.step
    def failure_msj(mjs):
        pytest.fail(mjs)

    @allure.step
    def get_attribute(self, locator:tuple, attribute:str) -> str|None:
        element = self.get_element(locator)
        return element.get_attribute(attribute)

    @allure.step
    def get_text(self, locator:tuple) -> str:
        element = self.get_element(locator)
        return element.text


    @staticmethod
    @allure.step
    def wait(seconds):
        time.sleep(seconds)


    @allure.step
    def current_title(self) -> str:
        return self.driver.title


    @allure.step
    def hadle_slider(self, slider, slider_min, slider_max, min_value, max_value):
        from test_data.locators.result_page import min_price, max_price

        es = self.get_element(locator=slider)
        min = self.get_element(locator=slider_min)
        max = self.get_element(locator=slider_max)
        dim = es.size
        percentage = int(dim['width']) / 15

        move = ActionChains(self.driver)
        while True:
            move.click_and_hold(min).move_by_offset(percentage, 0).release().perform()
            if int(self.get_attribute(min_price, 'value').replace('$','').replace(',','')) == min_value:
                break
        while True:
            move.click_and_hold(max).move_by_offset(-percentage, 0).release().perform()
            if int(self.get_attribute(max_price, 'value').replace('$','').replace(',','')) == max_value:
                break

    @allure.step
    def select_drop_down_by_text(self, locator, text):
        select_option = Select(self.get_element(locator))
        select_option.select_by_visible_text(text)


    @allure.step
    def current_url(self) -> str:
        return self.driver.current_url.lower()
    