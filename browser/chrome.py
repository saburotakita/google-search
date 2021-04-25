import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from . import element


class Chrome:
    def __init__(self, is_headless=True):
        self._is_headless = is_headless
        self._driver = None

    def get(self, url):
        if self._driver is None:
            self._driver = self._set_driver()
        self._driver.get(url)
        time.sleep(1)
        
    def find_element_by_css_selector(self, selector):
        if self._is_open():
            return element.Element(
                self._driver.find_element_by_css_selector(selector),
                self._driver)

    def execute_script(self, script, element):
        if self._is_open():
            self._driver.execute_script(script, element)

    def quit(self):
        if self._is_open():
            self._driver.quit()

    @property
    def current_url(self):
        if self._is_open():
            return self._driver.current_url
        return None

    def _is_open(self):
        return self._driver is not None

    def _set_driver(self):
        # Chromeドライバーの読み込み
        options = webdriver.ChromeOptions()

        # ヘッドレスモード（画面非表示モード）をの設定
        if self._is_headless:
            options.add_argument('--headless')

        # 起動オプションの設定
        options.add_argument(
            '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                AppleWebKit/537.36 (KHTML, like Gecko) \
                    Chrome/83.0.4103.116 Safari/537.36')

        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument('--incognito')

        # ChromeのWebDriverオブジェクトを作成する。
        return webdriver.Chrome(
            ChromeDriverManager().install(), options=options)
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.quit()
