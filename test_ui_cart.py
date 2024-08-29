import allure
from .pages.cart_page import CartPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Check empty cart")
def test_add_product_to_cart(browser):
    browser.get("https://www.chitai-gorod.ru/cart")
    cart_page = CartPage(browser)

    assert cart_page.get_cart_items() == []


@allure.title("Go to catalog")
def test_go_to_catalog_from_cart(browser):
    browser.get("https://www.chitai-gorod.ru/cart")
    browser.set_window_size(1200, 1000)
    browser.implicitly_wait(15)
    cart_page = CartPage(browser)
    catalog_link = cart_page.get_catalog_link()
    browser.execute_script("return arguments[0].scrollIntoView(true);", catalog_link)
    catalog_link.click()
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "app-catalog-page__title"))
    )

    assert "Каталог книг. Литература всех жанров и направлений. Интернет-магазин «Читай-город»" in browser.title
