import time


from browser.chrome import Chrome
from google.search import GoogleSearch

def main():
    with GoogleSearch(Chrome(False)) as conn:
        conn.first_search('千葉県')


if __name__ == '__main__':
    main()
