#!/usr/bin/env python3
"""Get covid cases from MSIS database."""
import datetime

import pandas as pd
from requests_html import HTMLSession


def get_msis_data(municipalities, date=datetime.date.today()):
    url = 'https://statistikk.fhi.no/msis/sykdomshendelser?etter=diagnose&fordeltPaa=geografi&diagnose=713&diagramtype=tabell&maaned=3&kommune=3416,3401'

    # Header for Chrome 83 Windows
    header = {
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://www.google.no/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9"
    }

    session = HTMLSession()
    session.headers = header
    r = session.get(url)
    r.html.render()
    tables = r.html.find('table')
    dfs = pd.read_html(tables[0].html)

    # print(f'Total tables: {len(dfs)}')
    # print(dfs[0])
    return dfs[0]


if __name__ == '__main__':
    get_msis_data({3416})
