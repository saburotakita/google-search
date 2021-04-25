class Element:
    def __init__(self, selenium_element, driver):
        self._driver = driver
        self._selenium_element = selenium_element

    def input_value(self, text):
        self._selenium_element.send_keys(text)

    def click(self):
        try:
            self._selenium_element.click()
        except:
            self._driver.execute_script("arguments[0].click();", self._selenium_element)
