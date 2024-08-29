from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def get_cart_items(self):
        return self.driver.find_elements(By.CSS_SELECTOR, '.cart-item')

    def get_catalog_link(self):
        return self.driver.find_element(By.XPATH, '//a[contains(@href,"catalog")]')
