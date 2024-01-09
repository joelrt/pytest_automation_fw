import pytest

from pages.home_page import HomePage
from pages.results_page import ResultPage

def test_itinerary_and_start_booking_are_displayed(setup):
    hp = HomePage(setup)
    hp.open_home_page()
    hp.waiting_page_by_title('Cruises | Carnival Cruise Deals: Caribbean, Bahamas, Alaska, Mexico')
    hp.set_sail_to("The Bahamas")
    hp.set_duration("6 to 9 Days")
    hp.select_search_cruises()
    rp = ResultPage(setup)
    rp.waiting_page_by_title('Cruise Search: Find Your Perfect Carnival Cruise')
    rp.select_a_radom_itinerary()
    assert rp.itinerary_page_is_displayed() == True, "Itierary page is not loaded"
    assert rp.start_booking_button_is_present() == True, 'Start Booking Button is not preset'
