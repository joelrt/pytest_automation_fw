# -*- coding: utf-8 -*-
from random import choice
from pages.base import Base
from test_data.locators.result_page import cruise_result, vacation_budget, common_status, slider, slider_minimun, slider_maximun, result_prices, sort_option, view_itinerary, itinerary_section, start_booking

class ResultPage(Base):
    def __init__(self, setup):
        Base.__init__(self, setup)
        self.min_val = None
        self.max_val = None
    
    def result_list_is_retured_in_a_grid(self):
        if not self.verify_element_present(cruise_result):
            self.failure_msj("Cruise result is not returned!!")

    def set_vacation_budget_by_slide(self, minimun:int, maximun:int):
        self.min_val = minimun
        self.max_val = maximun
        if self.get_attribute(vacation_budget, common_status) == "false": 
            self.click_on_element(vacation_budget)
        self.hadle_slider(slider=slider, slider_min=slider_minimun, slider_max=slider_maximun,
                          min_value=minimun, max_value=maximun)
        if self.get_attribute(vacation_budget, common_status) == "true": 
            self.click_on_element(vacation_budget)
    
    def validate_prices(self):
        res_prices = self.get_elements(result_prices)
        for element in res_prices:
            value = int(element.text.replace('\n*',''))
            if not int(self.min_val) <= value <= int(self.max_val):
                self.failure_msj(f"The value {value} is not in the range")
                break
    
    def sort_result(self, option:str):
        self.select_drop_down_by_text(locator=sort_option, text=option)

    def validate_sort_prices (self, option:str):
        res_prices = self.get_elements(result_prices)
        prices = [int(element.text.replace('\n*','')) for element in res_prices]
        if option == 'Low to High':
            return all(prices[i] <= prices[i + 1] for i in range(len(prices) - 1))
        else:
            return all(prices[i] >= prices[i + 1] for i in range(len(prices) - 1))
    
    def select_a_radom_itinerary(self):
        itinerary_list = self.get_elements(locator=view_itinerary)
        self.click_on_element_obj(choice(itinerary_list))
        print('hola')
    
    def itinerary_page_is_displayed(self):
        if self.verify_element_present(itinerary_section):
            return "itinerary" in self.current_url()
        
    def start_booking_button_is_present(self):
        return self.verify_element_present(start_booking)