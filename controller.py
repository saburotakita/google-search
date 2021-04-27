import datetime
import pathlib

import eel
from browser.chrome import Chrome
from google.search import GoogleSearch
import pandas as pd

from view import desktop

def main():
    # 開始時に最初に呼ばれる関数
    app_name = 'web'
    end_point = 'index.html'
    size = (600, 280)
    desktop.start(app_name, end_point, size)


@eel.expose
def search(text, count):
    """Googleでの検索処理

    Args:
        text (str): 検索ワード
        count (str): 最大検索件数（javascriptからなのでstr型固定）
    """
    # 何も検索ワードが入力されていなければ、エラーを表示して終了
    if not text.split():
        eel.change_message('error', '検索ワードを入力してください')
        return None

    # 1以上の数値が入力されていなければ、エラーを表示して終了
    if not count.isdecimal() or int(count) <= 0:
        eel.change_message('error', '最大取得件数は１以上の数値で入力してください')
        return None

    # メッセージを変更して、検索ボタンを無効化
    eel.change_message('running', '実行中です・・・')
    eel.change_search_button('disable')

    # 開始時間を取得
    start_time = datetime.datetime.now()

    # ブラウザを開いて処理の開始
    with GoogleSearch(Chrome(True)) as conn:
        # 開始ログを表示
        print('='*20)
        print('取得開始')

        # ブラウザの検索処理を呼び出し
        count = int(count)
        results = conn.search(text, count)

    # 出力用ディレクトリの作成
    dir_path = pathlib.Path('results')
    dir_path.mkdir(exist_ok=True)

    # 出力ファイル名の作成
    file_path = dir_path / f'result_{start_time.strftime("%Y%m%d_%H%M%S")}.csv'

    # CSV出力
    df = pd.DataFrame(results)
    df.index = df.index + 1
    df.to_csv(file_path, encoding='utf-8_sig')

    # 終了ログを表示
    print('='*20)
    print('取得完了')
    print(str(file_path))

    # メッセージを変更して、検索ボタンを有効化
    eel.change_message('success', '完了しました')
    eel.change_search_button('enable')


if __name__ == '__main__':
    main()
