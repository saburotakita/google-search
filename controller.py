import datetime

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
    count = int(count)
    with GoogleSearch(Chrome(False)) as conn:
        now = datetime.datetime.now()
        results = conn.search(text, count)
        df = pd.DataFrame(results)
        df.index = df.index + 1
        df.to_csv(f'result_{now.strftime("%Y%m%d_%H%M%S")}.csv', encoding='utf-8_sig')


if __name__ == '__main__':
    main()
