from nsetools import Nse

from pprint import pprint

from csv import writer

 

nse = Nse()

 

stocks_list = []

 

#top gainers

top_gainers = nse.get_top_gainers()

 

def _get(d, *keys):

    for k in keys:

        if k in d:

            return d[k]

    return None

 

header = ['Stock name', '% change', 'Open price', 'High price', 'Low price', 'Previous price', 'Volume', 'Ltp']

with open('topGainers.csv', 'w', newline='') as f:

    csv_writer = writer(f)

    csv_writer.writerow(header)

    for i in range(min(20, len(top_gainers))):

        r = top_gainers[i]

        stock_name = _get(r, 'symbol')

        pct_change = _get(r, 'perChange', 'pChange', 'percentChange', 'p_change')

        open_price = _get(r, 'openPrice', 'open_price', 'open')

        previous_price = _get(r, 'previousPrice', 'previous_price')

        volume = _get(r, 'tradedQuantity', 'traded_quantity')

        high_price = _get(r, 'highPrice', 'high_price')

        low_price = _get(r, 'lowPrice', 'low_price')

        ltp = _get(r, 'ltp')

        csv_writer.writerow([stock_name, pct_change, open_price, high_price, low_price, previous_price, volume, ltp])

        stocks_list.append(stock_name)

 

#top losers

top_losers = nse.get_top_losers()

 

with open('topLosers.csv', 'w', newline='') as f:

    csv_writer = writer(f)

    csv_writer.writerow(header)

    for i in range(min(20, len(top_losers))):

        r = top_losers[i]

        stock_name = _get(r, 'symbol')

        pct_change = _get(r, 'perChange', 'pChange', 'percentChange', 'p_change')

        open_price = _get(r, 'openPrice', 'open_price', 'open')

        previous_price = _get(r, 'previousPrice', 'previous_price')

        volume = _get(r, 'tradedQuantity', 'traded_quantity')

        high_price = _get(r, 'highPrice', 'high_price')

        low_price = _get(r, 'lowPrice', 'low_price')

        ltp = _get(r, 'ltp')

        csv_writer.writerow([stock_name, pct_change, open_price, high_price, low_price, previous_price, volume, ltp])

        stocks_list.append(stock_name)