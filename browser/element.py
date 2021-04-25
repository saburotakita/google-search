class Element:
    def __init__(self, selenium_element, driver):
        self._driver = driver
        self._selenium_element = selenium_element
        
    @property
    def text(self):
        return self._selenium_element.text
    
    @property
    def href(self):
        return self._selenium_element.get_attribute('href')

    def input_value(self, text):
        self._selenium_element.send_keys(text)

    def click(self):
        try:
            self._selenium_element.click()
        except:
            self._driver.execute_script("arguments[0].click();", self._selenium_element)
            
    def find_element_by_tag_name(self, tag_name):
        return Element(self._selenium_element.find_element_by_tag_name(tag_name), self._driver)
