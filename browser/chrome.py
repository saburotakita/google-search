from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

class Chrome:
    def __init__(self, is_headless=True):
        self._driver = None
        self._is_headless = is_headless

    def _set_driver(self):
        # Chromeドライバーの読み込み
        options = ChromeOptions()

        # ヘッドレスモード（画面非表示モード）をの設定
        if self._is_headless:
            options.add_argument('--headless')

        # 起動オプションの設定
        options.add_argument(
            '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument('--incognito')

        # ChromeのWebDriverオブジェクトを作成する。
        return Chrome(ChromeDriverManager().install(), options=options)
    
    def __enter__(self):
        self._driver = self._set_driver()
        
    def __exit__(self, exc_type, exc_value, traceback):
        if self._driver is not None:
            self._driver.quit()
