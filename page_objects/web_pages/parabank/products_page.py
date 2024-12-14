from selenium.webdriver.common.by import By

list_of_products = (By.CSS_SELECTOR, "div[class='b-product']")


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def get_list_of_products(self):
        return self.driver.find_elements(list_of_products[0], list_of_products[1])
