import time

import pytest

from pages.home_page import HomePage
from pages.store_page import StorePage


@pytest.mark.usefixtures("driver")
class TestOrderProcessing:
    def test_order_product_as_a_guest(self):
        home_page = HomePage(self.driver).open()
        # home_page.menu.open_store_page()
        # #
        # store_page = StorePage(self.driver).wait_for_page_to_load()
        # store_page.footer.click_dismiss_button()
        # store_page.add_item_to_cart("Belt")
        # time.sleep(5)
