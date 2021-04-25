from browser import chrome


def main():
    with chrome.Chrome(False) as conn:
        conn.get('https://www.yahoo.co.jp/')


if __name__ == '__main__':
    main()
