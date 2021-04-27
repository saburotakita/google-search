import time


class GoogleSearch:
    """Google検索とその結果を管理"""

    ROOT_URL = 'https://www.google.com'

    def __init__(self, browser):
        """
        Args:
            browser (class): 処理するブラウザ（browserパッケージ）
        """
        self._browser = browser

    def open(self):
        self._browser.get(self.ROOT_URL)

    def close(self):
        self._browser.quit()

    def search(self, text, max_count):
        """検索のメイン処理

        Args:
            text (str): 検索ワード
            max_count (int): 最大検索件数

        Returns:
            [list]: 結果の辞書のリスト
        """
        # 最初の検索処理
        self.first_search(text)

        # すべての結果を格納するリスト
        ex_results = []

        # 最大取得件数を超えるか、ページがなくなるまでループ（breakで抜ける）
        while True:
            # 現在のページの結果を取得
            results = self.fetch_results()

            # すでに取得した件数と、現在のページの件数の合計数を取得
            count = len(results) + len(ex_results)

            # 最大取得件数より合計数のほうが少なければ、すべて追加する
            # 合計数のほうが多ければ、足りない分だけ追加してループを抜ける
            if max_count >= count:
                ex_results += results
                print(f'{len(ex_results)}件取得完了')
            else:
                ex_results += results[:max_count-len(ex_results)]
                print(f'{len(ex_results)}件取得完了')
                break

            # 次のページが無ければループを抜ける
            if not self.next_page():
                break

        return ex_results

    def first_search(self, text):
        """ROOT_URLで検索を実行

        Args:
            text (str): 検索ワード
        """
        # 現在がROOT_URLでなければ戻る
        if self._browser.current_url != self.ROOT_URL:
            self.open()

        # 検索ボックスと検索ボタンを取得
        input_selector = 'body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input'
        input_element = self._browser.find_element_by_css_selector(input_selector)
        input_element.input_value(text)

        btn_selector = 'body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.FPdoLc.tfB0Bf > center > input.gNO89b'
        btn_element = self._browser.find_element_by_css_selector(btn_selector)
        btn_element.click()

        time.sleep(1)

    def fetch_results(self):
        """検索結果を取得

        Returns:
            [list]: 結果の辞書のリスト
        """
        # そのページ内の検索結果をリストで取得
        result_class_name = 'tF2Cxc'
        result_elements = self._browser.find_elements_by_class_name(result_class_name)

        # 各結果から必要な情報を抽出してリストに追加
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
        """次のページに移る

        Returns:
            [bool]: 遷移した:True/次のページが無かった:False
        """
        # エラーにならないよう、次ページをリストで取得し、要素数で判断
        next_elements = self._browser.find_elements_by_id('pnnext')
        if len(next_elements):
            self._browser.get(next_elements[0].href)
            time.sleep(1)
            return True
        return False

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
