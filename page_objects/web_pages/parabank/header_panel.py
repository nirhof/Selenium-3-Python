from selenium.webdriver.common.by import By

btn_home = (By.LINK_TEXT, "home")
btn_about_us = (By.LINK_TEXT, "about")
btn_contact = (By.LINK_TEXT, "contact")
menu_solutions = (By.LINK_TEXT, "Solutions")
menu_about_us = (By.LINK_TEXT, "About Us")
menu_services = (By.LINK_TEXT, "Services")
menu_products = (By.LINK_TEXT, "Products")
menu_locations = (By.LINK_TEXT, "Locations")


class HeaderPanel:
    def __init__(self, driver):
        self.driver = driver

    def get_btn_home(self):
        return self.driver.find_element(btn_home[0], btn_home[1])

    def get_btn_about_us(self):
        return self.driver.find_element(btn_about_us[0], btn_about_us[1])

    def get_btn_contact(self):
        return self.driver.find_element(btn_contact[0], btn_contact[1])

    def get_menu_solutions(self):
        return self.driver.find_element(menu_solutions[0], menu_solutions[1])

    def get_menu_products(self):
        return self.driver.find_element(menu_products[0], menu_products[1])

    def get_menu_about_us(self):
        return self.driver.find_element(menu_about_us[0], menu_about_us[1])

    def get_menu_services(self):
        return self.driver.find_element(menu_services[0], menu_services[1])

    def get_menu_products(self):
        return self.driver.find_element(menu_products[0], menu_products[1])

    def get_menu_locations(self):
        return self.driver.find_element(menu_locations[0], menu_locations[1])
