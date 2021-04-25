import time


class GoogleSearch:
    ROOT_URL = 'https://www.google.com'
    
    def __init__(self, browser):
        self._browser = browser

    def open(self):
        self._browser.get(self.ROOT_URL)

    def close(self):
        self._browser.quit()
        
    def first_search(self, text):
        if self._browser.current_url != self.ROOT_URL:
            self.open()

        input_selector = 'body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input'
        input_element = self._browser.find_element_by_css_selector(input_selector)
        input_element.input_value(text)
        
        btn_selector = 'body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.FPdoLc.tfB0Bf > center > input.gNO89b'
        btn_element = self._browser.find_element_by_css_selector(btn_selector)
        btn_element.click()
#        self._browser.execute_script("arguments[0].click();", btn_element)

        time.sleep(3)

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
