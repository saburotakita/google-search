import datetime
import pathlib

import eel
from browser.chrome import Chrome
from google.search import GoogleSearch
import pandas as pd

from view import desktop

def main():
    app_name = 'web'
    end_point = 'index.html'
    size = (600, 280)

    desktop.start(app_name, end_point, size)


@eel.expose
def search(text, count):
    if not text.split():
        eel.change_message('error', '検索ワードを入力してください')
        return None

    if not count.isdecimal() or int(count) <= 0:
        eel.change_message('error', '最大取得件数は１以上の数値で入力してください')
        return None

    eel.change_message('running', '実行中です・・・')
    eel.change_search_button('disable')

    count = int(count)
    with GoogleSearch(Chrome(True)) as conn:
        print('='*20)
        print('取得開始')
        now = datetime.datetime.now()
        results = conn.search(text, count)

    df = pd.DataFrame(results)
    df.index = df.index + 1
    
    dir_path = pathlib.Path('results')
    dir_path.mkdir(exist_ok=True)

    file_path = dir_path / f'result_{now.strftime("%Y%m%d_%H%M%S")}.csv'
    df.to_csv(file_path, encoding='utf-8_sig')

    print('='*20)
    print('取得完了')
    print(str(file_path))

    eel.change_message('success', '完了しました')
    eel.change_search_button('enable')


if __name__ == '__main__':
    main()
