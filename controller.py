import datetime

from browser.chrome import Chrome
from google.search import GoogleSearch
import pandas as pd


def main():
    with GoogleSearch(Chrome(True)) as conn:
        now = datetime.datetime.now()
        results = conn.search('ポケモン', 50)
        df = pd.DataFrame(results)
        df.index = df.index + 1
        df.to_csv(f'result_{now.strftime("%Y%m%d_%H%M%S")}.csv', encoding='utf-8_sig')


if __name__ == '__main__':
    main()
