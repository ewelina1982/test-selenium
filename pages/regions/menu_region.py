import time

from selenium.webdriver.common.by import By

from pages.regions.base_region import BaseRegion


class MenuRegion(BaseRegion):
    _root_locator = (By.CSS_SELECTOR, "div[class='storefront-primary-navigation']")
    _store_button = (By.XPATH, ".//li[@id='menu-item-102']//a[contains(text(),'Sklep')]")
    _amount_pay = (By.CSS_SELECTOR, "a[class='cart-contents'] span[class*='Price-amount amount']")

    def amount(self):
        time.sleep(5)
        value = self.find_element(*self._amount_pay).text
        return value[1:]

    def open_store_page(self):
        self.find_element(*self._store_button).click()
        return self
