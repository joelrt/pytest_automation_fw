# -*- coding: utf-8 -*-
from pages.base import Base
from test_data.locators.common import offer_modal, close_offer_modal
from test_data.locators.home_page import sail_to_btn, common_status, destinations, duration_btn, durations, search_cruises_btn


class HomePage(Base):
    def __init__(self, setup):
        Base.__init__(self, setup)
        
        
    def close_offer_modal(self):
        if self.verify_element_present(locator=offer_modal, wait=3):
            self.click_on_element(locator=close_offer_modal)
    
    def open_home_page(self):
        self.go_page()
        self.close_offer_modal()

    def set_sail_to(self, destination:str):
        if self.get_attribute(sail_to_btn, common_status) == "false": 
            self.click_on_element(sail_to_btn)
        self.click_on_element(destinations[str(destination.replace(' ','_')).lower()])

    def set_duration(self, duration:str):
        if self.get_attribute(duration_btn, common_status) == "false": 
            self.click_on_element(duration_btn)
        self.click_on_element(durations[str(duration.replace(' ','_')).lower()])

    def select_search_cruises(self):
        self.click_on_element(search_cruises_btn)
