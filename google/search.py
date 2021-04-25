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

        time.sleep(3)
        
    def fetch_results(self):
        result_class_name = 'tF2Cxc'
        result_elements = self._browser.find_elements_by_class_name(result_class_name)

        results = []
        for result_element in result_elements:
            title_element = result_element.find_element_by_tag_name('h3')
            link_element = result_element.find_element_by_tag_name('a')
            results.append({
                'title': title_element.text,
                'url': link_element.href,
            })
        return results

    def next_page(self):
        next_elements = self._browser.find_elements_by_id('pnnext')
        if len(next_elements):
            next_elements[0].click()
            time.sleep(1)
            return True
        return False

    def search(self, text, max_count):
        self.first_search(text)
        ex_results = []
        while True:
            results = self.fetch_results()

            count = len(results) + len(ex_results)
            if max_count >= count:
                ex_results += results
            else:
                ex_results += results[:max_count-len(ex_results)]
                break

            if not self.next_page():
                break
        return ex_results


    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
