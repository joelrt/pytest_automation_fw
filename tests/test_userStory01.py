import pytest

from pages.home_page import HomePage
from pages.results_page import ResultPage

def test_search_cruises_with_durationa_and_destination(setup):
    hp = HomePage(setup)
    hp.open_home_page()
    hp.waiting_page_by_title('Cruises | Carnival Cruise Deals: Caribbean, Bahamas, Alaska, Mexico')
    hp.set_sail_to("The Bahamas")
    hp.set_duration("6 to 9 Days")
    hp.select_search_cruises()
    rp = ResultPage(setup)
    rp.waiting_page_by_title('Cruise Search: Find Your Perfect Carnival Cruise')
    rp.result_list_is_retured_in_a_grid()
    rp.set_vacation_budget_by_slide(500, 1000)
    rp.validate_prices()
    rp.sort_result('High to Low')
    assert rp.validate_sort_prices('High to Low') == True, "Result is not properly sorted"
    rp.sort_result('Low to High')
    assert rp.validate_sort_prices('Low to High') == True, "Result is not properly sorted"


    

