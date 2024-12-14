from selenium.webdriver.common.by import By

btn_zero = (By.NAME, "Zero")
btn_one = (By.NAME, "One")
btn_two = (By.NAME, "Two")
btn_three = (By.NAME, "Three")
btn_four = (By.NAME, "Four")
btn_five = (By.NAME, "Five")
btn_six = (By.NAME, "Six")
btn_seven = (By.NAME, "Seven")
btn_eight = (By.NAME, "Eight")
btn_nine = (By.NAME, "Nine")
btn_plus = (By.NAME, "Plus")
btn_minus = (By.NAME, "Minus")
btn_multiply = (By.NAME, "Multiply by")
btn_divide = (By.NAME, "Divide by")
btn_equals = (By.NAME, "Equals")
btn_clear = (By.NAME, "Clear")
txt_result = (By.XPATH, "//*[@AutomationId='CalculatorResults']")

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def get_btn_one(self):
        return self.driver.find_element(btn_one[0], btn_one[1])

    def get_btn_two(self):
        return self.driver.find_element(btn_two[0], btn_two[1])

    def get_btn_three(self):
        return self.driver.find_element(btn_three[0], btn_three[1])

    def get_btn_four(self):
        return self.driver.find_element(btn_four[0], btn_four[1])

    def get_btn_five(self):
        return self.driver.find_element(btn_five[0], btn_five[1])

    def get_btn_six(self):
        return self.driver.find_element(btn_six[0], btn_six[1])

    def get_btn_seven(self):
        return self.driver.find_element(btn_seven[0], btn_seven[1])

    def get_btn_eight(self):
        return self.driver.find_element(btn_eight[0], btn_eight[1])

    def get_btn_nine(self):
        return self.driver.find_element(btn_nine[0], btn_nine[1])

    def get_btn_zero(self):
        return self.driver.find_element(btn_zero[0], btn_zero[1])

    def get_btn_plus(self):
        return self.driver.find_element(btn_plus[0], btn_plus[1])

    def get_btn_minus(self):
        return self.driver.find_element(btn_minus[0], btn_minus[1])

    def get_btn_multiply(self):
        return self.driver.find_element(btn_multiply[0], btn_multiply[1])

    def get_btn_divide(self):
        return self.driver.find_element(btn_divide[0], btn_divide[1])

    def get_btn_equals(self):
        return self.driver.find_element(btn_equals[0], btn_equals[1])

    def get_btn_clear(self):
        return self.driver.find_element(btn_clear[0], btn_clear[1])

    def get_txt_result(self):
        return self.driver.find_element(txt_result[0], txt_result[1])